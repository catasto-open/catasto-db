-- ctcn.ctqualit definition

-- Drop table

-- DROP TABLE ctcn.ctqualit;

CREATE TABLE ctcn.ctqualit (
    codice int4 NOT NULL,
    qualita varchar(12) NOT NULL,
    CONSTRAINT ctqualit_pkey PRIMARY KEY (codice)
);
