CREATE INDEX fogli_i1 ON ctmp.fogli USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
