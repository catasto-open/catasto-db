CREATE INDEX cttitola_idx2 ON ctcn.cttitola USING btree(
    codice, sezione, immobile, tipo_imm
);
