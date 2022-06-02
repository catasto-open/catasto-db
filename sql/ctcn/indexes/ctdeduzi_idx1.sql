CREATE INDEX ctdeduzi_idx1 ON ctcn.ctdeduzi USING btree(
    codice, sezione, immobile, tipo_imm, progressiv
);
