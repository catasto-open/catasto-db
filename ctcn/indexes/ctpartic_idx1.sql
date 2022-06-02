CREATE INDEX ctpartic_idx1 ON ctcn.ctpartic USING btree(
    codice, sezione, foglio, numero
);
