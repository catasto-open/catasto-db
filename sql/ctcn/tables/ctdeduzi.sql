-- ctcn.ctdeduzi definition

-- Drop table

-- DROP TABLE ctcn.ctdeduzi;

CREATE TABLE ctcn.ctdeduzi (
    codice varchar(4) NOT NULL,
    sezione varchar(1) NOT NULL,
    immobile int8 NOT NULL,
    tipo_imm varchar(1) NOT NULL,
    progressiv int4 NOT NULL,
    deduzione varchar(6) NULL
);
CREATE INDEX ctdeduzi_idx1 ON ctcn.ctdeduzi USING btree(
    codice, sezione, immobile, tipo_imm, progressiv
);
