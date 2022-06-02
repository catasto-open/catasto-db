CREATE INDEX fabbricati_i1 ON ctmp_a.fabbricati USING btree(
    comune, sezione, foglio, allegato, sviluppo, numero
);
