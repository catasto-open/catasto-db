-- ctcn.ctnonfis definition

-- Drop table

-- DROP TABLE ctcn.ctnonfis;

CREATE TABLE ctcn.ctnonfis (
    codice varchar(4) NOT NULL,
    sezione varchar(1) NOT NULL,
    soggetto int8 NOT NULL,
    tipo_sog varchar(1) NOT NULL,
    denominaz varchar(150) NULL,
    sede varchar(4) NULL,
    codfiscale varchar(11) NULL,
    CONSTRAINT ctnonfis_pkey PRIMARY KEY (codice, sezione, soggetto, tipo_sog)
);
CREATE INDEX ctnonfis_i1 ON ctcn.ctnonfis USING btree(
    denominaz varchar_pattern_ops
);
CREATE INDEX ctnonfis_i2 ON ctcn.ctnonfis USING btree(
    codfiscale varchar_pattern_ops
);
