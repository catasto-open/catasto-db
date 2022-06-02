CREATE INDEX testi_i1 ON ctmp.testi USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
