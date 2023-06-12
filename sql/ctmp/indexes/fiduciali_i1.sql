CREATE INDEX fiduciali_i1 ON ctmp.fiduciali USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
