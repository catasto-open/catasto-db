"""Added catasto db map SP

Revision ID: 609c563e08c9
Revises: cfd6fafbf3bc
Create Date: 2022-07-07 12:56:17.205433

"""
from alembic import op
from app.utils.alembic import ReplaceableObject

# revision identifiers, used by Alembic.
revision = '609c563e08c9'
down_revision = 'cfd6fafbf3bc'
branch_labels = None
depends_on = None

add_archive_map_sp = ReplaceableObject(
    "ctmp.archivia_mappa(comune text, sezione text, foglio text, allegato text, sviluppo text, stato integer)",
    """
    RETURNS void
    LANGUAGE plpgsql
    AS $function$
    declare
    fname       varchar(64) := 'archivia_mappa';
    sql_text    text;
    -- cursore di appoggio per le selezioni
    r           record;
    -- variabile per i controlli con le count
    controllo   integer;
    -- nomi delle tabelle da archiviare
    table_names text[];
    table_name  text;
    -- nome della mappa
    l_mappa     text;
    -- data di aggiornamento della mappa
    l_data_gen  text;
    -- stato di archiviazione
    l_stato     integer;
    begin
    -- ***************************************************************************
    -- Descrizione:
    --   Salva tutti gli elementi della mappa nello schema di archivio. Se la 
    --   mappa e' stata gia' archiviata non esegue nessuna operazione.
    -- Parametri:
    --   comune: comune del foglio da elaborare.
    --   sezione: sezione del foglio da elaborare.
    --   foglio: numero del foglio da elaborare.
    --   allegato: allegato del foglio da elaborare.
    --   sviluppo: sviluppo del foglio da elaborare.
    --   stato: stato dell'archiviazione, valori: 1, 2; 1 per nuova importazione,  
    --   2 per trasformazione.
    -- ***************************************************************************
    raise info 'archivia_mappa(%, %, %, %, %, %)', comune, sezione, foglio, allegato, sviluppo, stato;

      table_names := ARRAY['fogli', 'particelle', 'acque', 'strade', 'fabbricati',
        'linee_vest', 'simboli', 'fiduciali', 'testi', 'quadri_unione', 'libretti',
        'raster'
      ];

      l_mappa := comune || sezione || lpad(foglio, 4, '0') || allegato || sviluppo;
      l_stato := stato;

      -- controllo se esiste la mappa da archiviare 
      -- selezionanto la data_gen che mi servira' per l'archiviazione
      l_data_gen := '';
      for r in (
        select t.data_gen
          from ctmp.metadati t
         where t.nome_mappa = l_mappa
      )
      loop
        l_data_gen = r.data_gen;
      end loop;
      --raise info 'controllo esistenza mappa (data_gen): %', l_data_gen;

      if l_data_gen <> '' then -- se esiste la mappa
        -- controllo se questo foglio e' stato gia' archiviato con questa data e 
        -- questo stato 
        select count(*)
          from ctmp_a.metadati t
          into controllo
          where t.nome_mappa = l_mappa
          and t.data_gen = l_data_gen
          and t.stato = l_stato;
        --raise info 'controllo mappa archiviata: %', controllo;
        --if controllo = 1 then
        --  raise exception 'Il foglio % % % % % e'' stato gia'' archiviato!', cm, sz, fg, ag, sv;
        --end if;
        -- qui non ho bisogno di mettere > 0 perche' mappa, data e stato sono chiave
        if controllo = 0 then -- se non esiste in archivio
          -- inserisco i metadati in archivio
          --raise info 'archiviazione tabella metadati';
          insert into ctmp_a.metadati
               select t.*, l_stato, current_timestamp 
                 from ctmp.metadati t
                where t.nome_mappa = l_mappa;
          foreach table_name in array table_names
          loop -- loop nomi tabelle
            --raise info 'archiviazione tabella %', table_name;
            -- solo per il debug
            --sql_text := format(
            --              'INSERT INTO ctmp_a."%s" ' ||
            --              'SELECT t.*, %L, %s, current_timestamp ' ||
            --              'FROM ctmp."%s" t ' ||
            --              'WHERE t.comune = %L AND t.sezione = %L AND t.foglio = %L ' ||
            --              'AND t.allegato = %L AND t.sviluppo = %L',
            --              table_name, l_data_gen, l_stato, table_name, comune, sezione, foglio, allegato, sviluppo
            --            );
            --raise info 'sql_text: %', sql_text;
            sql_text := format(
                          'INSERT INTO ctmp_a."%s" ' ||
                          'SELECT t.*, $1, $2, current_timestamp ' ||
                          'FROM ctmp."%s" t ' ||
                          'WHERE t.comune = $3 AND t.sezione = $4 AND t.foglio = $5 ' ||
                          'AND t.allegato = $6 AND t.sviluppo = $7',
                          table_name, table_name
                        );
            --raise info 'sql_text: %', sql_text;
            execute sql_text using l_data_gen, l_stato, comune, sezione, foglio, allegato, sviluppo;
          end loop; -- loop nomi tabelle
        end if; -- se non esiste in archivio
        -- se sto facendo una nuova importazione allora elimino i vecchi record
        if l_stato = 1 then
          perform ctmp.cancella_mappa(comune, sezione, foglio, allegato, sviluppo, l_data_gen, false);
        end if;
      end if; -- se esiste la mappa
      --raise exception 'rollback per i test';
    end $function$;
    """
)

add_delete_map_sp = ReplaceableObject(
    "ctmp.cancella_mappa(comune text, sezione text, "
    "foglio text, allegato text, sviluppo text, "
    "data_gen text, ricorsivo boolean DEFAULT false)",
    """
    RETURNS void
    LANGUAGE plpgsql
    AS $function$
    declare
      fname       varchar(64) := 'cancella_mappa';
      sql_text    text;
      -- variabile per i controlli con le count
      controllo   integer;
      -- nomi delle tabelle da eliminare
      table_names text[];
      table_name  text;
      -- nome della mappa
      l_mappa     text;
      -- data di aggiornamento della mappa
      l_data_gen  text;
    begin
      -- ***************************************************************************
      -- Descrizione:
      --   Cancella tutti gli elementi associati ad una mappa, se ricorsivo anche
      --   dall'archivio.
      -- Parametri:
      --   comune: comune del foglio da elaborare.
      --   sezione: sezione del foglio da elaborare.
      --   foglio: numero del foglio da elaborare.
      --   allegato: allegato del foglio da elaborare.
      --   sviluppo: sviluppo del foglio da elaborare.
      --   data_gen: data di generazione della mappa. 
      --   ricorsivo: se la cancellazione deve essere ricorsiva, cioe' anche 
      --              nell'archivio.
      -- ***************************************************************************
      raise info 'cancella_mappa(%, %, %, %, %, %, %)', comune, sezione,
       foglio, allegato, sviluppo, data_gen, ricorsivo;

      table_names := ARRAY['fogli', 'particelle', 'acque', 'strade', 'fabbricati',
        'linee_vest', 'simboli', 'fiduciali', 'testi', 'quadri_unione', 'libretti',
        'raster'
      ];

      l_mappa := comune || sezione || lpad(foglio, 4, '0') || allegato || sviluppo;
      l_data_gen := data_gen;

      -- controllo se esiste la mappa da cancellare
      select count(*) as tot
        into controllo
        from ctmp.metadati t
       where t.nome_mappa = l_mappa
         and t.data_gen = l_data_gen;
      --raise info 'controllo esistenza mappa: %', controllo;
      --if controllo = 1 then -- se esiste la mappa
      -- questa condizione e' piu' volta a sistemare ogni cosa nel caso in cui mi 
      -- ritrovi piu' mappe inserite magari per sbaglio 
      if controllo > 0 then -- se esiste la mappa
        -- cancello dalle tabelle dati
        foreach table_name in array table_names
        loop -- loop tabelle ctmp
          --raise info 'cancellazione dalla tabella ctmp.%', table_name;
          -- solo per il debug
          --sql_text := format(
          --              'DELETE FROM ctmp."%s" ' ||
          --              'WHERE comune = %L AND sezione = %L AND foglio = %L ' ||
          --              'AND allegato = %L AND sviluppo = %L',
          --              table_name, comune, sezione, foglio, allegato, sviluppo
          --            );
          --raise info 'sql_text: %', sql_text;
          -- fine solo per il debug
          sql_text := format(
                        'DELETE FROM ctmp."%s" ' ||
                        'WHERE comune = $1 AND sezione = $2 AND foglio = $3 ' ||
                        'AND allegato = $4 AND sviluppo = $5',
                        table_name
                      );
          --raise info 'sql_text: %', sql_text;
          execute sql_text using comune, sezione, foglio, allegato, sviluppo;
        end loop; -- loop tabelle ctmp
        -- cancello dai metadati
        --raise info 'cancellazione dalla tabella ctmp.metadati';
        delete from ctmp.metadati 
              where ctmp.metadati.nome_mappa = l_mappa
                and ctmp.metadati.data_gen = l_data_gen;
      end if; -- se esiste la mappa

      -- se voglio la cancellazione ricorsiva devo cancellare anche dall'archivio
      if ricorsivo then -- se la cancellazione e' ricorsiva
        -- controllo se esiste la mappa da cancellare in archivio
        select count(*) as tot
          into controllo
          from ctmp_a.metadati t
         where t.nome_mappa = l_mappa
           and t.data_gen = l_data_gen;
        --raise info 'controllo esistenza mappa in archivio: %', controllo;
        -- qui non ho bisogno di mettere > 0 perche' mappa, data e stato sono chiave
        if controllo = 1 then -- se esiste la mappa
          -- cancello dalle tabelle dati
          foreach table_name in array table_names
          loop -- loop tabelle ctmp_a
            --raise info 'cancellazione dalla tabella ctmp_a.%', table_name;
            -- solo per il debug
            --sql_text := format(
            --              'DELETE FROM ctmp_a."%s" ' ||
            --              'WHERE comune = %L AND sezione = %L AND foglio = %L ' ||
            --              'AND allegato = %L AND sviluppo = %L AND data_gen = %L',
            --              table_name, comune, sezione, foglio, allegato, sviluppo, 
            --              data_gen
            --            );
            --raise info 'sql_text: %', sql_text;
            -- fine solo per il debug
            sql_text := format(
                          'DELETE FROM ctmp_a."%s" ' ||
                          'WHERE comune = $1 AND sezione = $2 AND foglio = $3 ' ||
                          'AND allegato = $4 AND sviluppo = $5 AND data_gen = $6',
                          table_name
                        );
            --raise info 'sql_text: %', sql_text;
            execute sql_text using comune, sezione, foglio, allegato, sviluppo, l_data_gen;
          end loop; -- loop tabelle ctmp_a
          -- cancello dai metadati
          --raise info 'cancellazione dalla tabella ctmp_a.metadati';
          delete from ctmp_a.metadati 
                where ctmp_a.metadati.nome_mappa = l_mappa
                  and ctmp_a.metadati.data_gen = l_data_gen;
        end if; -- se esiste la mappa  
      end if; -- se la cancellazione e' ricorsiva
      --raise exception 'rollback per i test';
    end $function$;
    """
)


def upgrade() -> None:
    op.create_sp(add_archive_map_sp)
    op.create_sp(add_delete_map_sp)


def downgrade() -> None:
    op.drop_sp(add_archive_map_sp)
    op.drop_sp(add_delete_map_sp)
