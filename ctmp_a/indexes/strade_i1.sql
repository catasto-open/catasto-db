CREATE INDEX strade_i1 ON ctmp_a.strade USING btree(
    comune, sezione, foglio, allegato, sviluppo, numero
);
