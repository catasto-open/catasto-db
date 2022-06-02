-- ctcn.cucodtop definition

-- Drop table

-- DROP TABLE ctcn.cucodtop;

CREATE TABLE ctcn.cucodtop (
    codice int4 NOT NULL,
    toponimo varchar(30) NOT NULL,
    CONSTRAINT cucodtop_pkey PRIMARY KEY (codice)
);
