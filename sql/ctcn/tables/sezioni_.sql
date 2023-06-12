-- ctcn.sezioni_ definition

-- Drop table

-- DROP TABLE ctcn.sezioni_;

CREATE TABLE ctcn.sezioni_ (
    codice varchar(4) NOT NULL,
    sezione varchar(1) NOT NULL,
    comune varchar(1000) NOT NULL,
    catasto varchar(1) NOT NULL,
    stato varchar(1000) NOT NULL
);
