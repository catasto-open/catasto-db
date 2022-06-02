CREATE INDEX ctriserv_idx1 ON ctcn.ctriserv USING btree(
    codice, sezione, immobile, tipo_imm, progressiv
);
