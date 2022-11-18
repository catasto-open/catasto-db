-- ctcn.version definition

-- Drop table

-- DROP TABLE ctcn.version;

CREATE TABLE ctcn.version (
    codice varchar(64) NOT NULL,
    data_aggiornamento date NOT NULL,
    CONSTRAINT version_pkey PRIMARY KEY (codice)
);
