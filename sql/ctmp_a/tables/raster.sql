-- ctmp_a.raster definition

-- Drop table

-- DROP TABLE ctmp_a.raster;

CREATE TABLE ctmp_a.raster (
    id int4 NOT NULL, -- Identificativo univoco della tabella
    comune varchar(4) NOT NULL, -- Codice catastale del Comune
    sezione varchar(1) NOT NULL, -- Codice sezione censuaria
    foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
    allegato varchar(1) NULL, -- Eventuale codice allegato
    sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
    nome_file varchar(80) NULL, -- Nome del file raster
    geom geometry NOT NULL, -- Geometria del riquadro rappresentante il posizionamento georiferito del raster
    data_gen varchar(10) NOT NULL, -- Data di generazione della mappa
    stato int4 NOT NULL, -- Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione
    data_crea timestamp NOT NULL, -- Data di creazione del record
    CONSTRAINT raster_pkey PRIMARY KEY (id, stato)
);
CREATE INDEX raster_i1 ON ctmp_a.raster USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
CREATE INDEX raster_si1 ON ctmp_a.raster USING gist(geom);
COMMENT ON TABLE ctmp_a.raster IS 'File raster';

-- Column comments

COMMENT ON COLUMN ctmp_a.raster.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp_a.raster.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp_a.raster.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp_a.raster.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp_a.raster.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp_a.raster.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp_a.raster.nome_file IS 'Nome del file raster';
COMMENT ON COLUMN ctmp_a.raster.geom IS 'Geometria del riquadro rappresentante il posizionamento georiferito del raster';
COMMENT ON COLUMN ctmp_a.raster.data_gen IS 'Data di generazione della mappa';
COMMENT ON COLUMN ctmp_a.raster.stato IS 'Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione';
COMMENT ON COLUMN ctmp_a.raster.data_crea IS 'Data di creazione del record';
