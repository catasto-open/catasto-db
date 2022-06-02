CREATE INDEX curiserv_idx1 ON ctcn.curiserv USING btree(
    codice, sezione, immobile, tipo_imm, progressiv
);
