CREATE INDEX particelle_i1 ON ctmp.particelle USING btree(
    comune, sezione, foglio, allegato, sviluppo, numero
);
