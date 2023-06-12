-- ctcn.curiserv definition

-- Drop table

-- DROP TABLE ctcn.curiserv;

CREATE TABLE ctcn.curiserv (
    codice varchar(4) NOT NULL,
    sezione varchar(1) NOT NULL,
    immobile int8 NOT NULL,
    tipo_imm varchar(1) NOT NULL,
    progressiv int4 NOT NULL,
    riserva varchar(1) NULL,
    iscrizione varchar(7) NULL
);
CREATE INDEX curiserv_idx1 ON ctcn.curiserv USING btree(
    codice, sezione, immobile, tipo_imm, progressiv
);
