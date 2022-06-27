-- ctcn.cttitoli definition

-- Drop table

-- DROP TABLE ctcn.cttitoli;

CREATE TABLE ctcn.cttitoli (
    codice varchar(3) NOT NULL,
    titolo varchar(53) NOT NULL,
    CONSTRAINT cttitoli_pkey PRIMARY KEY (codice)
);
