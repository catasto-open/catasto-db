CREATE INDEX acque_i1 ON ctmp.acque USING btree(
    comune, sezione, foglio, allegato, sviluppo, numero
);
