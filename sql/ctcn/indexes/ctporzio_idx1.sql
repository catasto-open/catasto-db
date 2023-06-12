CREATE INDEX ctporzio_idx1 ON ctcn.ctporzio USING btree(
    codice, sezione, immobile, tipo_imm, progressiv
);
