CREATE INDEX cttitola_soggetto_idx ON ctcn.cttitola USING btree(
    soggetto, tipo_sog
);
