CREATE INDEX simboli_i1 ON ctmp_a.simboli USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
