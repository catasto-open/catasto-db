CREATE INDEX quadri_unione_i1 ON ctmp.quadri_unione USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
