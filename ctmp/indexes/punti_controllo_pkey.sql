CREATE UNIQUE INDEX punti_controllo_pkey ON ctmp.punti_controllo USING btree(
    comune, sezione, foglio, n_gruppo, n_punto
);
