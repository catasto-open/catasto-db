-- ctcn.cuindiri definition

-- Drop table

-- DROP TABLE ctcn.cuindiri;

CREATE TABLE ctcn.cuindiri (
    codice varchar(4) NOT NULL,
    sezione varchar(1) NOT NULL,
    immobile int8 NOT NULL,
    tipo_imm varchar(1) NOT NULL,
    progressiv int4 NOT NULL,
    toponimo int4 NULL,
    indirizzo varchar(50) NULL,
    civico1 varchar(6) NULL,
    civico2 varchar(6) NULL,
    civico3 varchar(6) NULL,
    cod_strada varchar(5) NULL
);
CREATE INDEX cuindiri_idx1 ON ctcn.cuindiri USING btree(
    codice, sezione, immobile, tipo_imm, progressiv
);
