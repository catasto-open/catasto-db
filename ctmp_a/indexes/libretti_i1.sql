CREATE INDEX libretti_i1 ON ctmp_a.libretti USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
