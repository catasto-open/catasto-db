-- ctcn.ctriserv definition

-- Drop table

-- DROP TABLE ctcn.ctriserv;

CREATE TABLE ctcn.ctriserv (
    codice varchar(4) NOT NULL,
    sezione varchar(1) NOT NULL,
    immobile int8 NOT NULL,
    tipo_imm varchar(1) NOT NULL,
    progressiv int4 NOT NULL,
    riserva varchar(1) NULL,
    iscrizione varchar(7) NULL
);
CREATE INDEX ctriserv_idx1 ON ctcn.ctriserv USING btree(
    codice, sezione, immobile, tipo_imm, progressiv
);
