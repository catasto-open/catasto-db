-- ctcn.comuni_ definition

-- Drop table

-- DROP TABLE ctcn.comuni_;

CREATE TABLE ctcn.comuni_ (
    codice varchar(4) NOT NULL,
    provincia varchar(2) NOT NULL,
    comune varchar(1000) NOT NULL,
    comune_straniero varchar(1000) NULL,
    codice_catastale varchar(5) NULL,
    ufficio_terreni varchar(2) NULL,
    ufficio_catasto varchar(2) NULL,
    conservatoria varchar(5) NULL,
    istat varchar(10) NULL,
    data_inizio date NULL,
    data_variazione date NULL,
    tipo varchar(1) NULL
);

CREATE INDEX comuni__index01 ON ctcn.comuni_ USING btree(
    codice,
    provincia,
    comune,
    data_inizio,
    data_variazione
);
