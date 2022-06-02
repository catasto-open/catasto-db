CREATE INDEX linee_vest_i1 ON ctmp.linee_vest USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
