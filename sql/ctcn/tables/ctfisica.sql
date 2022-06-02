-- ctcn.ctfisica definition

-- Drop table

-- DROP TABLE ctcn.ctfisica;

CREATE TABLE ctcn.ctfisica (
    codice varchar(4) NOT NULL,
    sezione varchar(1) NOT NULL,
    soggetto int8 NOT NULL,
    tipo_sog varchar(1) NOT NULL,
    cognome varchar(50) NULL,
    nome varchar(50) NULL,
    sesso varchar(1) NULL,
    data varchar(10) NULL,
    luogo varchar(4) NULL,
    codfiscale varchar(16) NULL,
    supplement varchar(100) NULL,
    CONSTRAINT ctfisica_pkey PRIMARY KEY (codice, sezione, soggetto, tipo_sog)
);
CREATE INDEX ctfisica_i1 ON ctcn.ctfisica USING btree(
    cognome varchar_pattern_ops, nome varchar_pattern_ops
);
CREATE INDEX ctfisica_i2 ON ctcn.ctfisica USING btree(
    codfiscale varchar_pattern_ops
);
CREATE INDEX ctfisica_i3 ON ctcn.ctfisica USING btree(
    ((((cognome)::text || ' '::text) || (nome)::text)) varchar_pattern_ops
);
CREATE INDEX ctfisica_index01 ON ctcn.ctfisica USING btree(luogo);
