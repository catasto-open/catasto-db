-- ctcn.ctpartic definition

-- Drop table

-- DROP TABLE ctcn.ctpartic;

CREATE TABLE ctcn.ctpartic (
    codice varchar(4) NOT NULL,
    sezione varchar(1) NOT NULL,
    immobile int8 NOT NULL,
    tipo_imm varchar(1) NOT NULL,
    progressiv int4 NOT NULL,
    foglio int4 NULL,
    numero varchar(5) NULL,
    denominato int4 NULL,
    subalterno varchar(4) NULL,
    edificiale varchar(1) NULL,
    qualita int4 NULL,
    classe varchar(2) NULL,
    ettari int4 NULL,
    are int4 NULL,
    centiare int4 NULL,
    flag_redd varchar(1) NULL,
    flag_porz varchar(1) NULL,
    flag_deduz varchar(1) NULL,
    dominic_l varchar(9) NULL,
    agrario_l varchar(8) NULL,
    dominic_e varchar(12) NULL,
    agrario_e varchar(11) NULL,
    gen_eff varchar(10) NULL,
    gen_regist varchar(10) NULL,
    gen_tipo varchar(1) NULL,
    gen_numero varchar(6) NULL,
    gen_progre varchar(3) NULL,
    gen_anno int4 NULL,
    con_eff varchar(10) NULL,
    con_regist varchar(10) NULL,
    con_tipo varchar(1) NULL,
    con_numero varchar(6) NULL,
    con_progre varchar(3) NULL,
    con_anno int4 NULL,
    partita varchar(7) NULL,
    annotazion varchar(200) NULL,
    mutaz_iniz int4 NULL,
    mutaz_fine int4 NULL,
    gen_causa varchar(3) NULL,
    gen_descr varchar(100) NULL,
    con_causa varchar(3) NULL,
    con_descr varchar(100) NULL,
    CONSTRAINT ctpartic_pkey PRIMARY KEY (
        codice, sezione, immobile, tipo_imm, progressiv
    )
);
CREATE INDEX ctpartic_idx1 ON ctcn.ctpartic USING btree(
    codice, sezione, foglio, numero
);
