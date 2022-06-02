-- ctcn.cuarcuiu definition

-- Drop table

-- DROP TABLE ctcn.cuarcuiu;

CREATE TABLE ctcn.cuarcuiu (
    codice varchar(4) NOT NULL,
    sezione varchar(1) NOT NULL,
    immobile int8 NOT NULL,
    tipo_imm varchar(1) NOT NULL,
    progressiv int4 NOT NULL,
    zona varchar(3) NULL,
    categoria varchar(3) NULL,
    classe varchar(2) NULL,
    consistenz varchar(7) NULL,
    superficie varchar(5) NULL,
    rendita_l varchar(15) NULL,
    rendita_e varchar(18) NULL,
    lotto varchar(2) NULL,
    edificio varchar(2) NULL,
    scala varchar(2) NULL,
    interno_1 varchar(3) NULL,
    interno_2 varchar(3) NULL,
    piano_1 varchar(4) NULL,
    piano_2 varchar(4) NULL,
    piano_3 varchar(4) NULL,
    piano_4 varchar(4) NULL,
    gen_eff varchar(10) NULL,
    gen_regist varchar(10) NULL,
    gen_tipo varchar(1) NULL,
    gen_numero varchar(6) NULL,
    gen_progre varchar(3) NULL,
    gen_anno varchar(4) NULL,
    con_eff varchar(10) NULL,
    con_regist varchar(10) NULL,
    con_tipo varchar(1) NULL,
    con_numero varchar(6) NULL,
    con_progre varchar(3) NULL,
    con_anno varchar(4) NULL,
    partita varchar(7) NULL,
    annotazion varchar(200) NULL,
    mutaz_iniz int4 NULL,
    mutaz_fine int4 NULL,
    prot_notif varchar(18) NULL,
    data_notif varchar(8) NULL,
    gen_causa varchar(3) NULL,
    gen_descr varchar(100) NULL,
    con_causa varchar(3) NULL,
    con_descr varchar(100) NULL,
    flag_class varchar(1) NULL,
    CONSTRAINT cuarcuiu_pkey PRIMARY KEY (
        codice, sezione, immobile, tipo_imm, progressiv
    )
);
COMMENT ON TABLE ctcn.cuarcuiu IS 'caratteristiche dell''unita'' immobiliare';
