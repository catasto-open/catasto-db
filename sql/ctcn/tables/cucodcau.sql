-- ctcn.cucodcau definition

-- Drop table

-- DROP TABLE ctcn.cucodcau;

CREATE TABLE ctcn.cucodcau (
    cod_causa varchar(1) NOT NULL,
    descrizion varchar(65) NOT NULL,
    CONSTRAINT ctcodcau_pkey PRIMARY KEY (cod_causa)
);
