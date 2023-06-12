CREATE INDEX testi_i1 ON ctmp_a.testi USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
