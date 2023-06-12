CREATE INDEX acque_i1 ON ctmp_a.acque USING btree(
    comune, sezione, foglio, allegato, sviluppo, numero
);
