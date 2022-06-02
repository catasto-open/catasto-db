CREATE INDEX fiduciali_i1 ON ctmp_a.fiduciali USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
