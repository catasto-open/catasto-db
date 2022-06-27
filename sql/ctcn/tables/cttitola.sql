-- ctcn.cttitola definition

-- Drop table

-- DROP TABLE ctcn.cttitola;

CREATE TABLE ctcn.cttitola (
    codice varchar(4) NOT NULL,
    sezione varchar(1) NOT NULL,
    soggetto int8 NOT NULL,
    tipo_sog varchar(1) NOT NULL,
    immobile int8 NOT NULL,
    tipo_imm varchar(1) NOT NULL,
    diritto varchar(3) NULL,
    titolo varchar(200) NULL,
    numeratore int4 NULL,
    denominato int4 NULL,
    regime varchar(1) NULL,
    rif_regime int4 NULL,
    gen_valida varchar(10) NULL,
    gen_nota varchar(1) NULL,
    gen_numero varchar(6) NULL,
    gen_progre varchar(3) NULL,
    gen_anno varchar(4) NULL,
    gen_regist varchar(10) NULL,
    partita varchar(7) NULL,
    con_valida varchar(10) NULL,
    con_nota varchar(1) NULL,
    con_numero varchar(6) NULL,
    con_progre varchar(3) NULL,
    con_anno varchar(4) NULL,
    con_regist varchar(10) NULL,
    mutaz_iniz int4 NULL,
    mutaz_fine int4 NULL,
    identifica int4 NOT NULL,
    gen_causa varchar(3) NULL,
    gen_descr varchar(100) NULL,
    con_causa varchar(3) NULL,
    con_descr varchar(100) NULL,
    CONSTRAINT cttitola_pkey PRIMARY KEY (codice, sezione, identifica)
);
CREATE INDEX cttitola_idx1 ON ctcn.cttitola USING btree(
    codice, sezione, soggetto, tipo_sog
);
CREATE INDEX cttitola_idx2 ON ctcn.cttitola USING btree(
    codice, sezione, immobile, tipo_imm
);
CREATE INDEX cttitola_soggetto_idx ON ctcn.cttitola USING btree(
    soggetto, tipo_sog
);
