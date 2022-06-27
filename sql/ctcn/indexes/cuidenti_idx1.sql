CREATE INDEX cuidenti_idx1 ON ctcn.cuidenti USING btree(
    codice, sezione, immobile, tipo_imm, progressiv
);
