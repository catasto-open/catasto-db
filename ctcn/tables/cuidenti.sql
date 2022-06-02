-- ctcn.cuidenti definition

-- Drop table

-- DROP TABLE ctcn.cuidenti;

CREATE TABLE ctcn.cuidenti (
    codice varchar(4) NOT NULL,
    sezione varchar(1) NOT NULL,
    immobile int8 NOT NULL,
    tipo_imm varchar(1) NOT NULL,
    progressiv int4 NOT NULL,
    sez_urbana varchar(3) NULL,
    foglio varchar(4) NULL,
    numero varchar(5) NULL,
    denominato int4 NULL,
    subalterno varchar(4) NULL,
    edificiale varchar(1) NULL
);
CREATE INDEX cuidenti_idx1 ON ctcn.cuidenti USING btree(
    codice, sezione, immobile, tipo_imm, progressiv
);
CREATE INDEX cuidenti_idx2 ON ctcn.cuidenti USING btree(
    codice, sezione, foglio, numero
);
COMMENT ON TABLE ctcn.cuidenti IS 'identificativi dell''unita'' immobiliare';
