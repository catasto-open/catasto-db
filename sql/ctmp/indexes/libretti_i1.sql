CREATE INDEX libretti_i1 ON ctmp.libretti USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
