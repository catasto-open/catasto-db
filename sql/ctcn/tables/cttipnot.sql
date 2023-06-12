-- ctcn.cttipnot definition

-- Drop table

-- DROP TABLE ctcn.cttipnot;

CREATE TABLE ctcn.cttipnot (
    tipo_nota varchar(1) NOT NULL,
    descrizion varchar(65) NOT NULL,
    CONSTRAINT cttipnot_pkey PRIMARY KEY (tipo_nota)
);
