-- ctcn.ctporzio definition

-- Drop table

-- DROP TABLE ctcn.ctporzio;

CREATE TABLE ctcn.ctporzio (
    codice varchar(4) NOT NULL,
    sezione varchar(1) NOT NULL,
    immobile int8 NOT NULL,
    tipo_imm varchar(1) NOT NULL,
    progressiv int4 NOT NULL,
    porzione varchar(2) NULL,
    qualita int4 NULL,
    classe varchar(2) NULL,
    ettari int4 NULL,
    are int4 NULL,
    centiare int4 NULL,
    dominic_e varchar(12) NULL,
    agrario_e varchar(11) NULL
);
CREATE INDEX ctporzio_idx1 ON ctcn.ctporzio USING btree(
    codice, sezione, immobile, tipo_imm, progressiv
);
