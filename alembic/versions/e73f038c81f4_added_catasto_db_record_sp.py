"""Added catasto db record SP

Revision ID: e73f038c81f4
Revises: 609c563e08c9
Create Date: 2022-07-07 12:56:34.881613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from app.utils.alembic import ReplaceableObject

revision = 'e73f038c81f4'
down_revision = '609c563e08c9'
branch_labels = None
depends_on = None


add_process_subj_record = ReplaceableObject(
    "ctcn.elabora_record_sog(record_text text, sez_filler text DEFAULT ' '::text)",
    """
    RETURNS integer
    LANGUAGE plpgsql
    AS $function$
    declare
      fname      varchar(64) := 'elabora_record_sog';
      a          text[];
      r          record;
      tipo_rec   text;
      rp         ctcn.ctfisica%rowtype;
      rg         ctcn.ctnonfis%rowtype;
      tot_elab   integer;
    begin
      tot_elab := 0;
      begin
        -- se la stringa e' vuota esco direttamente
        if coalesce(record_text, '') = '' then return 0; end if;
    
        a := string_to_array(record_text, '|', '');
    
        -- ricordarsi che l'ultimo separatore delimita solo la fine del record
        tipo_rec := a[4]; -- tipo soggetto
        --raise info '[%] tipo_rec: %', fname, tipo_rec;
        --for i in 1 .. cardinality(a) loop
        --  raise info '%: %', i, a[i];
        --end loop;
    
        if tipo_rec = 'P' then
          rp.codice := a[1];
          rp.sezione := coalesce(a[2], sez_filler);
          rp.soggetto := a[3];
          rp.tipo_sog := a[4];
          rp.cognome := substr(trim(a[5]), 1, 50);
          rp.nome := substr(trim(a[6]), 1, 50);
          rp.sesso := a[7];
          rp.data := a[8];
          rp.luogo := a[9];
          rp.codfiscale := substr(trim(a[10]), 1, 16);
          rp.supplement := substr(trim(a[11]), 1, 100);
    
          -- prima provo ad aggiornare, in caso esista gia'
          update ctcn.ctfisica 
             set cognome = rp.cognome, 
                 nome = rp.nome, 
                 sesso = rp.sesso, 
                 data = data, 
                 luogo = rp.luogo, 
                 codfiscale = rp.codfiscale, 
                 supplement = rp.supplement
           where codice = rp.codice
             and sezione = rp.sezione
             and soggetto = rp.soggetto
             and tipo_sog = rp.tipo_sog;
          -- variabile speciale found
          if not found then
            insert into ctcn.ctfisica values (rp.*);
          end if;
          tot_elab := tot_elab + 1;
        elsif tipo_rec = 'G' then
          rg.codice := a[1];
          rg.sezione := coalesce(a[2], sez_filler);
          rg.soggetto := a[3];
          rg.tipo_sog := a[4];
          rg.denominaz := substr(trim(a[5]), 1, 150);
          rg.sede := a[6];
          rg.codfiscale := substr(trim(a[7]), 1, 16);
    
          -- prima provo ad aggiornare, in caso esista gia'
          update ctcn.ctnonfis 
             set denominaz = rg.denominaz, 
                 sede = rg.sede, 
                 codfiscale = rg.codfiscale
           where codice = rg.codice
             and sezione = rg.sezione
             and soggetto = rg.soggetto
             and tipo_sog = rg.tipo_sog;
          -- variabile speciale found
          if not found then
            insert into ctcn.ctnonfis values (rg.*);
          end if;
          tot_elab := tot_elab + 1;
        else
          raise exception 'tipo soggetto non valido';
        end if;
      --exception
      --  when others then
      --    perform ctcn.log_message(format('[%s] errore elaborazione riga: ' ||
      --      '%s - %s %s ', fname, record_text, sqlstate, sqlerrm));
      end;
      return tot_elab;
    end $function$;
    """
)

add_process_land_record = ReplaceableObject(
    "ctcn.elabora_record_ter(record_text text, sez_filler text "
    "DEFAULT ' '::text, interscambio boolean DEFAULT false)",
    """
    RETURNS integer
    LANGUAGE plpgsql
    AS $function$
    declare
      fname      varchar(64) := 'importa_ter';
      a          text[];
      r          record;
      tipo_rec   text;
      r1         ctcn.ctpartic%rowtype;
      r2         ctcn.ctdeduzi%rowtype;
      r3         ctcn.ctriserv%rowtype;
      r4         ctcn.ctporzio%rowtype;
      -- +1 per il tipo record
      n_chiave   integer := 5 + 1;
      n_val      integer;
      n_val_rip  integer;
      n_rip      integer;
      ioff       integer;
      tot_elab   integer;
    begin
      tot_elab := 0;
      begin
        -- se la stringa e' vuota esco direttamente
        if coalesce(record_text, '') = '' then return 0; end if;
    
        a := string_to_array(record_text, '|', '');
    
        -- ricordarsi che dalle tabelle manca tipo_rec (indice 6) e che 
        -- l'ultimo separatore delimita solo la fine del record
        tipo_rec := a[6]; -- tipo record
        --raise info '[%] tipo_rec: %', fname, tipo_rec;
        --for i in 1 .. cardinality(a) loop
        --  raise info '%: %', i, a[i];
        --end loop;
    
        -- * TIPO RECORD 1: PARTICELLE
        if tipo_rec = '1' then
          r1.codice := a[1];
          r1.sezione := coalesce(a[2], sez_filler);
          r1.immobile := a[3];
          r1.tipo_imm := a[4];
          r1.progressiv := a[5];
          r1.foglio := a[7];
          r1.numero := a[8];
          r1.denominato := a[9];
          r1.subalterno := a[10];
          r1.edificiale := a[11];
          r1.qualita := a[12];
          r1.classe := a[13];
          r1.ettari := a[14];
          r1.are := a[15];
          r1.centiare := a[16];
          r1.flag_redd := a[17];
          r1.flag_porz := a[18];
          r1.flag_deduz := a[19];
          r1.dominic_l := a[20];
          r1.agrario_l := a[21];
          r1.dominic_e := a[22];
          r1.agrario_e := a[23];
          r1.gen_eff := a[24];
          r1.gen_regist := a[25];
          r1.gen_tipo := a[26];
          r1.gen_numero := a[27];
          r1.gen_progre := a[28];
          r1.gen_anno := a[29];
          r1.con_eff := a[30];
          r1.con_regist := a[31];
          r1.con_tipo := a[32];
          r1.con_numero := a[33];
          r1.con_progre := a[34];
          r1.con_anno := a[35];
          r1.partita := a[36];
          r1.annotazion := a[37];
          r1.mutaz_iniz := a[38];
          r1.mutaz_fine := a[39];
          r1.gen_causa := a[40];
          r1.gen_descr := substr(trim(a[41]), 1, 100);
          r1.con_causa := a[42];
          r1.con_descr := substr(trim(a[43]), 1, 100);
    
          -- in caso mi venga passato un record esistente per l'aggiornamento delle 
          -- date di registrazione, cancello quello vecchio.
          delete from ctcn.ctpartic 
                where codice = r1.codice 
                  and sezione = r1.sezione 
                  and immobile = r1.immobile
                  and tipo_imm = r1.tipo_imm
                  and progressiv = r1.progressiv;
          -- se lo trovo, allora devo cancellare anche quelli correlati, in questo
          -- modo li cancello solo se viene ripetuta la particella
          if found then
            delete from ctcn.ctdeduzi 
                  where codice = r1.codice 
                    and sezione = r1.sezione 
                    and immobile = r1.immobile
                    and tipo_imm = r1.tipo_imm
                    and progressiv = r1.progressiv;
            delete from ctcn.ctriserv 
                  where codice = r1.codice 
                    and sezione = r1.sezione 
                    and immobile = r1.immobile
                    and tipo_imm = r1.tipo_imm
                    and progressiv = r1.progressiv;
            delete from ctcn.ctporzio 
                  where codice = r1.codice 
                    and sezione = r1.sezione 
                    and immobile = r1.immobile
                    and tipo_imm = r1.tipo_imm
                    and progressiv = r1.progressiv;
          end if;
    
          insert into ctcn.ctpartic values (r1.*);
          tot_elab := tot_elab + 1;
          -- se il progressivo è maggiore di 1 aggiorno la mutazione finale 
          -- del progressivo precedente
          if r1.progressiv > 1 then
            update ctcn.ctpartic 
               set con_eff = r1.gen_eff, 
                   con_regist = r1.gen_regist, 
                   con_tipo = r1.gen_tipo, 
                   con_numero = r1.gen_numero, 
                   con_progre = r1.gen_progre, 
                   con_anno = r1.gen_anno, 
                   mutaz_fine = r1.mutaz_iniz
             where codice = r1.codice
               and sezione = r1.sezione
               and immobile = r1.immobile
               and tipo_imm = r1.tipo_imm
               and progressiv = r1.progressiv - 1;
          end if;
        -- * TIPO RECORD 2: DEDUZIONI
        elsif tipo_rec = '2' then
          r2.codice := a[1];
          r2.sezione := coalesce(a[2], sez_filler);
          r2.immobile := a[3];
          r2.tipo_imm := a[4];
          r2.progressiv := a[5];
    
          -- questo sarebbe piu' robusto, ma e' una cancellazione per ogni inserimento
          -- delete from ctcn.ctdeduzi 
          --       where codice = r2.codice 
          --         and sezione = r2.sezione 
          --         and immobile = r2.immobile
          --         and tipo_imm = r2.tipo_imm
          --         and progressiv = r2.progressiv;
    
          -- inserimento valori ripetuti
          -- -1 per l'ultimo separatore
          n_val := cardinality(a) - 1;
          n_val_rip := 1;
          n_rip := (n_val - n_chiave) / n_val_rip;
          for i in 1 .. n_rip loop
            ioff := n_val_rip * (i - 1);
            r2.deduzione := a[7 + ioff];
    
            insert into ctcn.ctdeduzi values (r2.*);
            tot_elab := tot_elab + 1;
          end loop;
        -- * TIPO RECORD 3: RISERVE
        elsif tipo_rec = '3' then
          r3.codice := a[1];
          r3.sezione := coalesce(a[2], sez_filler);
          r3.immobile := a[3];
          r3.tipo_imm := a[4];
          r3.progressiv := a[5];
    
          -- questo sarebbe piu' robusto, ma e' una cancellazione per ogni inserimento
          -- delete from ctcn.ctriserv 
          --       where codice = r3.codice 
          --         and sezione = r3.sezione 
          --         and immobile = r3.immobile
          --         and tipo_imm = r3.tipo_imm
          --         and progressiv = r3.progressiv;
    
          -- inserimento valori ripetuti
          -- -1 per l'ultimo separatore
          n_val := cardinality(a) - 1;
          n_val_rip := 2;
          n_rip := (n_val - n_chiave) / n_val_rip;
          for i in 1 .. n_rip loop
            ioff := n_val_rip * (i - 1);
            r3.riserva := a[7 + ioff];
            r3.iscrizione := a[8 + ioff];
    
            insert into ctcn.ctriserv values (r3.*);
            tot_elab := tot_elab + 1;
          end loop;
        -- * TIPO RECORD 4: PORZIONI
        elsif tipo_rec = '4' then
          r4.codice := a[1];
          r4.sezione := coalesce(a[2], sez_filler);
          r4.immobile := a[3];
          r4.tipo_imm := a[4];
          r4.progressiv := a[5];
    
          -- questo sarebbe piu' robusto, ma e' una cancellazione per ogni inserimento
          -- delete from ctcn.ctporzio 
          --       where codice = r4.codice 
          --         and sezione = r4.sezione 
          --         and immobile = r4.immobile
          --         and tipo_imm = r4.tipo_imm
          --         and progressiv = r4.progressiv;
    
          -- inserimento valori ripetuti
          -- -1 per l'ultimo separatore
          n_val := cardinality(a) - 1;
          n_val_rip := 6 + case interscambio when true then 2 else 0 end;
          n_rip := (n_val - n_chiave) / n_val_rip;
          for i in 1 .. n_rip loop
            ioff := n_val_rip * (i - 1);
            r4.porzione := a[7 + ioff];
            r4.qualita := a[8 + ioff];
            r4.classe := a[9 + ioff];
            r4.ettari := a[10 + ioff];
            r4.are := a[11 + ioff];
            r4.centiare := a[12 + ioff];
            if interscambio then
              -- ATTENZIONE: questi due campi sono presenti solo per le 
              --             esportazioni da sistema di interscambio
              r4.dominic_e := a[13 + ioff];
              r4.agrario_e := a[14 + ioff];
            end if;
    
            insert into ctcn.ctporzio values (r4.*);
            tot_elab := tot_elab + 1;
          end loop;
        else
          raise exception 'tipo record non valido';
        end if;
      --exception
      --  when others then
      --    perform ctcn.log_message(format('[%s] errore elaborazione riga: ' ||
      --      '%s - %s %s ', fname, record_text, sqlstate, sqlerrm));
      end;
      return tot_elab;
      end $function$;

    """
)

add_process_building_record = ReplaceableObject(
    "ctcn.elabora_record_fab(record_text text, sez_filler text DEFAULT ' '::text)",
    """
    RETURNS integer
    LANGUAGE plpgsql
    AS $function$
    declare
      fname      varchar(64) := 'elabora_record_fab';
      a          text[];
      r          record;
      tipo_rec   text;
      r1         ctcn.cuarcuiu%rowtype;
      r2         ctcn.cuidenti%rowtype;
      r3         ctcn.cuindiri%rowtype;
      r4         ctcn.cuutilit%rowtype;
      r5         ctcn.curiserv%rowtype;
      -- +1 per il tipo record
      n_chiave   integer := 5 + 1;
      n_val      integer;
      n_val_rip  integer;
      n_rip      integer;
      ioff       integer;
      tot_elab   integer;
    begin
      tot_elab := 0;
      --for r in execute 'select content from ' || file_table loop
      begin
        -- se la stringa e' vuota esco direttamente
        if coalesce(record_text, '') = '' then return 0; end if;
    
        a := string_to_array(record_text, '|', '');
    
        -- ricordarsi che dalle tabelle manca tipo_rec (indice 6) e che 
        -- l'ultimo separatore delimita solo la fine del record
        tipo_rec := a[6]; -- tipo record
        --raise info '[%] tipo_rec: %', fname, tipo_rec;
        --for i in 1 .. cardinality(a) loop
        --  raise info '%: %', i, a[i];
        --end loop;
    
        -- * TIPO RECORD 1: FABBRICATI
        if tipo_rec = '1' then
          r1.codice := a[1];
          r1.sezione := coalesce(a[2], sez_filler);
          r1.immobile := a[3];
          r1.tipo_imm := a[4];
          r1.progressiv := a[5];
          r1.zona := a[7];
          r1.categoria := a[8];
          r1.classe := a[9];
          r1.consistenz := a[10];
          r1.superficie := a[11];
          r1.rendita_l := a[12];
          r1.rendita_e := a[13];
          r1.lotto := a[14];
          r1.edificio := a[15];
          r1.scala := a[16];
          r1.interno_1 := a[17];
          r1.interno_2 := a[18];
          r1.piano_1 := a[19];
          r1.piano_2 := a[20];
          r1.piano_3 := a[21];
          r1.piano_4 := a[22];
          r1.gen_eff := a[23];
          r1.gen_regist := a[24];
          r1.gen_tipo := a[25];
          r1.gen_numero := a[26];
          r1.gen_progre := a[27];
          r1.gen_anno := a[28];
          r1.con_eff := a[29];
          r1.con_regist := a[30];
          r1.con_tipo := a[31];
          r1.con_numero := a[32];
          r1.con_progre := a[33];
          r1.con_anno := a[34];
          r1.partita := a[35];
          r1.annotazion := substr(trim(a[36]), 1, 200);
          r1.mutaz_iniz := a[37];
          r1.mutaz_fine := a[38];
          r1.prot_notif := a[39];
          r1.data_notif := a[40];
          r1.gen_causa := a[41];
          r1.gen_descr := substr(trim(a[42]), 1, 100);
          r1.con_causa := a[43];
          r1.con_descr := substr(trim(a[44]), 1, 100);
          r1.flag_class := a[45];
    
          -- in caso mi venga passato un record esistente per l'aggiornamento delle 
          -- date di registrazione, cancello quello vecchio.
          delete from ctcn.cuarcuiu 
                where codice = r1.codice 
                  and sezione = r1.sezione 
                  and immobile = r1.immobile
                  and tipo_imm = r1.tipo_imm
                  and progressiv = r1.progressiv;
          -- se lo trovo, allora devo cancellare anche quelli correlati, in questo
          -- modo li cancello solo se viene ripetuta la particella
          if found then
            delete from ctcn.cuidenti 
                  where codice = r1.codice 
                    and sezione = r1.sezione 
                    and immobile = r1.immobile
                    and tipo_imm = r1.tipo_imm
                    and progressiv = r1.progressiv;
            delete from ctcn.cuindiri 
                  where codice = r1.codice 
                    and sezione = r1.sezione 
                    and immobile = r1.immobile
                    and tipo_imm = r1.tipo_imm
                    and progressiv = r1.progressiv;
            delete from ctcn.cuutilit 
                  where codice = r1.codice 
                    and sezione = r1.sezione 
                    and immobile = r1.immobile
                    and tipo_imm = r1.tipo_imm
                    and progressiv = r1.progressiv;
            delete from ctcn.curiserv 
                  where codice = r1.codice 
                    and sezione = r1.sezione 
                    and immobile = r1.immobile
                    and tipo_imm = r1.tipo_imm
                    and progressiv = r1.progressiv;
          end if;
    
          insert into ctcn.cuarcuiu values (r1.*);
          tot_elab := tot_elab + 1;
          -- se il progressivo è maggiore di 1 aggiorno la mutazione finale 
          -- del progressivo precedente
          if r1.progressiv > 1 then
            update ctcn.cuarcuiu 
               set con_eff = r1.gen_eff, 
                   con_regist = r1.gen_regist, 
                   con_tipo = r1.gen_tipo, 
                   con_numero = r1.gen_numero, 
                   con_progre = r1.gen_progre, 
                   con_anno = r1.gen_anno, 
                   mutaz_fine = r1.mutaz_iniz
             where codice = r1.codice
               and sezione = r1.sezione
               and immobile = r1.immobile
               and tipo_imm = r1.tipo_imm
               and progressiv = r1.progressiv - 1;
          end if;
        -- * TIPO RECORD 2: IDENTIFICATIVI
        elsif tipo_rec = '2' then
          r2.codice := a[1];
          r2.sezione := coalesce(a[2], sez_filler);
          r2.immobile := a[3];
          r2.tipo_imm := a[4];
          r2.progressiv := a[5];
    
          -- questo sarebbe piu' robusto, ma e' una cancellazione per ogni inserimento
          -- delete from ctcn.cuidenti 
          --       where codice = r2.codice 
          --         and sezione = r2.sezione 
          --         and immobile = r2.immobile
          --         and tipo_imm = r2.tipo_imm
          --         and progressiv = r2.progressiv;
    
          -- inserimento valori ripetuti
          -- -1 per l'ultimo separatore
          n_val := cardinality(a) - 1;
          n_val_rip := 6;
          n_rip := (n_val - n_chiave) / n_val_rip;
          for i in 1 .. n_rip loop
            ioff := n_val_rip * (i - 1);
            r2.sez_urbana := a[7 + ioff];
            r2.foglio := a[8 + ioff];
            r2.numero := a[9 + ioff];
            r2.denominato := a[10 + ioff];
            r2.subalterno := a[11 + ioff];
            begin
              r2.edificiale := a[12 + ioff];
              insert into ctcn.cuidenti values (r2.*);
    			    exception
                when SQLSTATE '22001' then
    				      r2.subalterno := a[12 + ioff];
    	    		    r2.edificiale := a[11 + ioff];
    	    	      insert into ctcn.cuidenti values (r2.*);
    	            insert into ctis.error_insert_fab(data) values(record_text);
    		    end;
            tot_elab := tot_elab + 1;
          end loop;
        -- * TIPO RECORD 3: INDIRIZZI
        elsif tipo_rec = '3' then
          r3.codice := a[1];
          r3.sezione := coalesce(a[2], sez_filler);
          r3.immobile := a[3];
          r3.tipo_imm := a[4];
          r3.progressiv := a[5];
    
          -- questo sarebbe piu' robusto, ma e' una cancellazione per ogni inserimento
          -- delete from ctcn.cuindiri 
          --       where codice = r3.codice 
          --         and sezione = r3.sezione 
          --         and immobile = r3.immobile
          --         and tipo_imm = r3.tipo_imm
          --         and progressiv = r3.progressiv;
    
          -- inserimento valori ripetuti
          -- -1 per l'ultimo separatore
          n_val := cardinality(a) - 1;
          n_val_rip := 6;
          n_rip := (n_val - n_chiave) / n_val_rip;
          for i in 1 .. n_rip loop
            ioff := n_val_rip * (i - 1);
            r3.toponimo := a[7 + ioff];
            r3.indirizzo := substr(trim(a[8 + ioff]), 1, 50);
            r3.civico1 := a[9 + ioff];
            r3.civico2 := a[10 + ioff];
            r3.civico3 := a[11 + ioff];
            r3.cod_strada := a[12 + ioff];
    
            insert into ctcn.cuindiri values (r3.*);
            tot_elab := tot_elab + 1;
          end loop;
        -- * TIPO RECORD 4: UTILITA' COMUNI
        elsif tipo_rec = '4' then
          r4.codice := a[1];
          r4.sezione := coalesce(a[2], sez_filler);
          r4.immobile := a[3];
          r4.tipo_imm := a[4];
          r4.progressiv := a[5];
    
          -- questo sarebbe piu' robusto, ma e' una cancellazione per ogni inserimento
          -- delete from ctcn.cuutilit 
          --       where codice = r4.codice 
          --         and sezione = r4.sezione 
          --         and immobile = r4.immobile
          --         and tipo_imm = r4.tipo_imm
          --         and progressiv = r4.progressiv;
    
          -- inserimento valori ripetuti
          -- -1 per l'ultimo separatore
          n_val := cardinality(a) - 1;
          n_val_rip := 5;
          n_rip := (n_val - n_chiave) / n_val_rip;
          for i in 1 .. n_rip loop
            ioff := n_val_rip * (i - 1);
            r4.sez_urbana := a[7 + ioff];
            r4.foglio := a[8 + ioff];
            r4.numero := a[9 + ioff];
            r4.denominato := a[10 + ioff];
            r4.subalterno := a[11 + ioff];
    
            insert into ctcn.cuutilit values (r4.*);
            tot_elab := tot_elab + 1;
          end loop;
        -- * TIPO RECORD 5: RISERVE
        elsif tipo_rec = '5' then
          r5.codice := a[1];
          r5.sezione := coalesce(a[2], sez_filler);
          r5.immobile := a[3];
          r5.tipo_imm := a[4];
          r5.progressiv := a[5];
    
          -- questo sarebbe piu' robusto, ma e' una cancellazione per ogni inserimento
          -- delete from ctcn.curiserv 
          --       where codice = r5.codice 
          --         and sezione = r5.sezione 
          --         and immobile = r5.immobile
          --         and tipo_imm = r5.tipo_imm
          --         and progressiv = r5.progressiv;
    
          -- inserimento valori ripetuti
          -- -1 per l'ultimo separatore
          n_val := cardinality(a) - 1;
          n_val_rip := 2;
          n_rip := (n_val - n_chiave) / n_val_rip;
          for i in 1 .. n_rip loop
            ioff := n_val_rip * (i - 1);
            r5.riserva := a[7 + ioff];
            r5.iscrizione := a[8 + ioff];
    
            insert into ctcn.curiserv values (r5.*);
            tot_elab := tot_elab + 1;
          end loop;
        else
          raise exception 'tipo record non valido';
        end if;
      --exception
      --  when others then
      --    perform ctcn.log_message(format('[%s] errore elaborazione riga: ' ||
      --      '%s - %s %s ', fname, record_text, sqlstate, sqlerrm));
      end;
    
      --end loop;
    
      return tot_elab;
    end $function$;
    """
)

add_process_owner_record = ReplaceableObject(
    "ctcn.elabora_record_tit(record_text text, sez_filler text DEFAULT ' '::text)",
    """
    RETURNS integer
    LANGUAGE plpgsql
    AS $function$
    declare
      fname      varchar(64) := 'elabora_record_tit';
      a          text[];
      r          record;
      rt         ctcn.cttitola%rowtype;
      tot_elab   integer;
    begin
      tot_elab := 0;
      begin
        -- se la stringa e' vuota esco direttamente
        if coalesce(record_text, '') = '' then return 0; end if;
    
        a := string_to_array(record_text, '|', '');
    
        -- ricordarsi che l'ultimo separatore delimita solo la fine del record
        --for i in 1 .. cardinality(a) loop
        --  raise info '%: %', i, a[i];
        --end loop;
    
        rt.codice := a[1];
        rt.sezione := coalesce(a[2], sez_filler);
        rt.soggetto := a[3];
        rt.tipo_sog := a[4];
        rt.immobile := a[5];
        rt.tipo_imm := a[6];
        rt.diritto := a[7];
        rt.titolo := substr(trim(a[8]), 1, 200);
        rt.numeratore := a[9];
        rt.denominato := a[10];
        rt.regime := a[11];
        rt.rif_regime := a[12];
        rt.gen_valida := a[13];
        rt.gen_nota := a[14];
        rt.gen_numero := a[15];
        rt.gen_progre := a[16];
        rt.gen_anno := a[17];
        rt.gen_regist := a[18];
        rt.partita := a[19];
        rt.con_valida := a[20];
        rt.con_nota := a[21];
        rt.con_numero := a[22];
        rt.con_progre := a[23];
        rt.con_anno := a[24];
        rt.con_regist := a[25];
        rt.mutaz_iniz := a[26];
        rt.mutaz_fine := a[27];
        rt.identifica := a[28];
        rt.gen_causa := a[29];
        rt.gen_descr := substr(trim(a[30]), 1, 100);
        rt.con_causa := a[31];
        rt.con_descr := substr(trim(a[32]), 1, 100);
    
        -- prima provo ad aggiornare, in caso esista gia'
        update ctcn.cttitola t
           set con_valida = rt.con_valida, 
               con_nota = rt.con_nota, 
               con_numero = rt.con_numero, 
               con_progre = rt.con_progre, 
               con_anno = rt.con_anno, 
               con_regist = rt.con_regist, 
               mutaz_fine = rt.mutaz_fine 
         where t.codice = rt.codice
           and t.sezione = rt.sezione
           and t.identifica = rt.identifica;
        -- variabile speciale found
        if not found then
          insert into ctcn.cttitola values (rt.*);
        end if;
        tot_elab := tot_elab + 1;
      --exception
      --  when others then
      --    perform ctcn.log_message(format('[%s] errore elaborazione riga: ' ||
      --      '%s - %s %s ', fname, record_text, sqlstate, sqlerrm));
      end;
      return tot_elab;
    end $function$;
    """
)


def upgrade() -> None:
    op.create_sp(add_process_subj_record)
    op.create_sp(add_process_land_record)
    op.create_sp(add_process_building_record)
    op.create_sp(add_process_owner_record)


def downgrade() -> None:
    op.drop_sp(add_process_subj_record)
    op.drop_sp(add_process_land_record)
    op.drop_sp(add_process_building_record)
    op.drop_sp(add_process_owner_record)
