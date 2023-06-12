"""added functions

Revision ID: f7c7baa76adf
Revises: 347ca562f469
Create Date: 2022-12-05 16:22:41.140963

"""
from alembic import op
from app.utils.alembic import ReplaceableObject


# revision identifiers, used by Alembic.
revision = 'f7c7baa76adf'
down_revision = '347ca562f469'
branch_labels = None
depends_on = None

add_ctcn_svuota_fabbricati = ReplaceableObject(
    "ctcn.svuota_fabbricati(p_comune text, p_sezione text)",
    """
    RETURNS void
    LANGUAGE plpgsql
    AS $function$
    declare
    i         int;
    begin
    -- ***************************************************************************
    -- Descrizione:
    --   Elimina tutti gli elementi dalle tabelle relative ai terreni.
    -- Parametri:
    --   comune: comune da elaborare.
    --   sezione: sezione del comune.
    -- ***************************************************************************

    -- metadati

    delete from ctcn.metadati where comune = p_comune and sezione = p_sezione and lower(tipo_estr) like '%fabbricati%';
    get diagnostics i = row_count;
    raise info 'cancellate % righe da metadati', i;

    if i > 0 then
    
        -- fabbricati

        delete from ctcn.cuarcuiu where codice = p_comune and sezione = p_sezione;
        get diagnostics i = row_count;
        raise info 'cancellate % righe da cuarcuiu', i;

        delete from ctcn.cuidenti where codice = p_comune and sezione = p_sezione;
        get diagnostics i = row_count;
        raise info 'cancellate % righe da cuidenti', i;

        delete from ctcn.cuindiri where codice = p_comune and sezione = p_sezione;
        get diagnostics i = row_count;
        raise info 'cancellate % righe da cuindiri', i;

        truncate table ctcn.cuutilit cascade;
        delete from ctcn.cuutilit where codice = p_comune and sezione = p_sezione;
        get diagnostics i = row_count;
        raise info 'cancellate % righe da cuutilit', i;

        delete from ctcn.curiserv where codice = p_comune and sezione = p_sezione;
        get diagnostics i = row_count;
        raise info 'cancellate % righe da curiserv', i;

        -- titolari

        delete from ctcn.ctfisica s
            where s.codice = p_comune and s.sezione = p_sezione
                and exists (
                    select soggetto from ctcn.cttitola t where t.codice = s.codice and t.sezione = s.sezione and t.soggetto = s.soggetto and t.tipo_sog = s.tipo_sog and tipo_imm = 'F'
                    -- escludo quelli che sono anche titolari di un terreno
                    except 
                    select soggetto from ctcn.cttitola t where t.codice = s.codice and t.sezione = s.sezione and t.soggetto = s.soggetto and t.tipo_sog = s.tipo_sog and tipo_imm = 'T'
                    );
        get diagnostics i = row_count;
        raise info 'cancellate % righe da ctfisica', i;

        delete from ctcn.ctnonfis s
            where s.codice = p_comune and s.sezione = p_sezione
                and exists (
                    select soggetto from ctcn.cttitola t where t.codice = s.codice and t.sezione = s.sezione and t.soggetto = s.soggetto and t.tipo_sog = s.tipo_sog and tipo_imm = 'F'
                    -- escludo quelli che sono anche titolari di un terreno
                    except 
                    select soggetto from ctcn.cttitola t where t.codice = s.codice and t.sezione = s.sezione and t.soggetto = s.soggetto and t.tipo_sog = s.tipo_sog and tipo_imm = 'T'
                    );
        get diagnostics i = row_count;
        raise info 'cancellate % righe da ctnonfis', i;

        delete from ctcn.cttitola where codice = p_comune and sezione = p_sezione and tipo_imm = 'F';
        get diagnostics i = row_count;
        raise info 'cancellate % righe da cttitola', i;

    end if;
    --raise exception 'rollback per il test';
    end $function$;
    """
)

add_ctcn_svuota_terreni = ReplaceableObject(
    "ctcn.svuota_terreni(p_comune text, p_sezione text)",
    """
    RETURNS void
    LANGUAGE plpgsql
    AS $function$
    declare
    i         int;
    begin
    -- ***************************************************************************
    -- Descrizione:
    --   Elimina tutti gli elementi dalle tabelle relative ai terreni.
    -- Parametri:
    --   comune: comune da elaborare.
    --   sezione: sezione del comune.
    -- ***************************************************************************

    -- metadati
    delete from ctcn.metadati where comune = p_comune and sezione = p_sezione and lower(tipo_estr) like '%terreni%';
    get diagnostics i = row_count;
    raise info 'cancellate % righe da metadati', i;

    if i > 0 then
    
        -- terreni
        
        delete from ctcn.ctpartic where codice = p_comune and sezione = p_sezione;
        get diagnostics i = row_count;
        raise info 'cancellate % righe da ctpartic', i;
        
        delete from ctcn.ctdeduzi where codice = p_comune and sezione = p_sezione;
        get diagnostics i = row_count;
        raise info 'cancellate % righe da ctdeduzi', i;
        
        delete from ctcn.ctriserv where codice = p_comune and sezione = p_sezione;
        get diagnostics i = row_count;
        raise info 'cancellate % righe da ctriserv', i;
        
        delete from ctcn.ctporzio where codice = p_comune and sezione = p_sezione;
        get diagnostics i = row_count;
        raise info 'cancellate % righe da ctporzio', i;
        
        -- titolari
        
        delete from ctcn.ctfisica s
            where s.codice = p_comune and s.sezione = p_sezione
                and exists (
                    select soggetto from ctcn.cttitola t where t.codice = s.codice and t.sezione = s.sezione and t.soggetto = s.soggetto and t.tipo_sog = s.tipo_sog and tipo_imm = 'T'
                    -- escludo quelli che sono anche titolari di un fabbricato
                    except 
                    select soggetto from ctcn.cttitola t where t.codice = s.codice and t.sezione = s.sezione and t.soggetto = s.soggetto and t.tipo_sog = s.tipo_sog and tipo_imm = 'F'
                    );
        get diagnostics i = row_count;
        raise info 'cancellate % righe da ctfisica', i;
        
        delete from ctcn.ctnonfis s
            where s.codice = p_comune and s.sezione = p_sezione
                and exists (
                    select soggetto from ctcn.cttitola t where t.codice = s.codice and t.sezione = s.sezione and t.soggetto = s.soggetto and t.tipo_sog = s.tipo_sog and tipo_imm = 'T'
                    -- escludo quelli che sono anche titolari di un fabbricato
                    except 
                    select soggetto from ctcn.cttitola t where t.codice = s.codice and t.sezione = s.sezione and t.soggetto = s.soggetto and t.tipo_sog = s.tipo_sog and tipo_imm = 'F'
                    );
        get diagnostics i = row_count;
        raise info 'cancellate % righe da ctnonfis', i;
        
        delete from ctcn.cttitola where codice = p_comune and sezione = p_sezione and tipo_imm = 'T';
        get diagnostics i = row_count;
        raise info 'cancellate % righe da cttitola', i;
    end if;

    --raise exception 'rollback per il test';
    end $function$
    ;
    """
)

add_ctmp_trasforma_mappa = ReplaceableObject(
    "ctmp.trasforma_mappa(comune text, sezione text, foglio text, allegato text, sviluppo text)",
    """
    RETURNS void
    LANGUAGE plpgsql
    AS $function$
    declare
    fname       varchar(64) := 'trasforma_mappa';
    -- variabili di appoggio per i parametri
    l_comune    text;
    l_sezione   text;
    l_foglio    text;
    l_allegato  text;
    l_sviluppo  text;
    -- stato trasformazione
    st_trasf    integer := 2;
    -- variabili di appoggio per le trasformazioni
    cp          double precision[];
    m           double precision[];
    tipo_trasf  text;
    table_names text[];
    a           text[];
    l           text;
    s           text;
    table_name  text;
    id_name     text;
    sql_text    text;
    func_name   text;
    func_pars   text;
    
    arch_from   text;
    arch_where  text;
    tab_alias   text;
    
    i           integer;
    r           record;
    begin
    -- ***************************************************************************
    -- Descrizione:
    --   Esegue la trasformazione delle geometrie di tutti gli elementi di un 
    --   foglio. La tipologia e la matrice vengono prese dalla tabella 
    --   trasformazioni ed eseguite in ordine. Se in archivio non esiste una 
    --   copia del foglio, prima dell'elaborazione il foglio viene archiviato.
    -- Parametri:
    --   comune: comune del foglio da elaborare.
    --   sezione: sezione del foglio da elaborare.
    --   foglio: numero del foglio da elaborare.
    --   allegato: allegato del foglio da elaborare.
    --   sviluppo: sviluppo del foglio da elaborare.
    -- ***************************************************************************
    raise info '%(%, %, %, %, %)', fname, comune, sezione, foglio, allegato, sviluppo;

    -- trasformazioni
    l_comune := comune;
    l_sezione := sezione;
    l_foglio := foglio;
    l_allegato := allegato;
    l_sviluppo := sviluppo;
    -- imposto gli elementi per la seleziona dall'archivio della prima trasformazione
    arch_from := 'from ctmp_a.fogli a ';
    arch_where := ' and t.id = a.id and a.stato = ' || st_trasf;
    tab_alias := 'a';
    -- cerco le trasformazioni
    for r in (
        select t.comune, t.sezione, t.foglio, t.allegato, t.sviluppo, t.n_trasf, 
            t.tipo_trasf, t.punti_contr, t.matrice_trasf
        from ctmp.trasformazioni t
        where t.comune = l_comune
        and t.sezione = l_sezione
        and t.foglio = l_foglio
        and t.allegato = l_allegato
        and t.sviluppo = l_sviluppo
        order by t.n_trasf
    )
    loop -- trasformazioni
        raise info 'trovata trasformazione % %', r.n_trasf, r.tipo_trasf;

        -- archiviazione
        perform ctmp.archivia_mappa(comune, sezione, foglio, allegato, sviluppo, st_trasf);

        cp := r.punti_contr;
        m := r.matrice_trasf;
        tipo_trasf := r.tipo_trasf;
        -- eseguo la trasformazione
        table_names := ARRAY[
        'fogli,id,t_pt_ins,t_ln_anc,geom',
        'particelle,id,t_pt_ins,t_ln_anc,geom',
        'acque,id,t_pt_ins,t_ln_anc,geom',
        'strade,id,t_pt_ins,t_ln_anc,geom',
        'fabbricati,id,t_pt_ins,t_ln_anc,geom',
        'linee_vest,id,geom',
        'simboli,id,geom',
        'fiduciali,id,t_pt_ins,geom',
        'testi,id,geom'
        ];
        if tipo_trasf = 'tps' then
        func_name := 'tps_transform';
        func_pars := '$1, $2';
        elsif tipo_trasf = 'affine' then
        func_name := 'affine_transform';
        func_pars := '$1';
        elsif tipo_trasf = 'move' then
        func_name := 'move_transform';
        func_pars := '$1';
        end if;
        foreach l in array table_names
        loop -- tabelle
        a := string_to_array(l, ',');
        table_name := a[1];
        raise info 'trasformazione tabella %', table_name;
        sql_text := '';
        foreach s in array a[3:array_upper(a, 1)]
        loop
            sql_text := sql_text || format('%s = ctmp.%s(%s.%s, %s), ', s, func_name, tab_alias, s, func_pars);
        end loop;
        sql_text := left(sql_text, -2);
        sql_text := format(
            'update ctmp.%s t set '
            || sql_text || ' '
            || arch_from
            || 'where t.comune = %L and t.sezione = %L and t.foglio = %L '
            || 'and t.allegato = %L and t.sviluppo = %L'
            || arch_where,
            table_name, l_comune, l_sezione, l_foglio, l_allegato, l_sviluppo
        );
        raise info 'sql_text: %', sql_text;

        if tipo_trasf = 'tps' then
            execute sql_text using cp, m; 
        else
            execute sql_text using m;
        end if;
        end loop; -- tabelle
        -- reimposto le variabili per le succesive trasformazioni
        if arch_from <> '' then
        arch_from := '';
        arch_where := '';
        tab_alias := 't';
        end if;
    end loop; -- trasformazioni  

    --raise exception 'rollback per i test';
    end $function$
    ;
    """
)


def upgrade() -> None:
    op.create_sp(add_ctcn_svuota_terreni)
    op.create_sp(add_ctcn_svuota_fabbricati)
    op.create_sp(add_ctmp_trasforma_mappa)


def downgrade() -> None:
    op.drop_sp(add_ctcn_svuota_terreni)
    op.drop_sp(add_ctcn_svuota_fabbricati)
    op.drop_sp(add_ctmp_trasforma_mappa)
