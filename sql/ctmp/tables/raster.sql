-- ctmp.raster definition

-- Drop table

-- DROP TABLE ctmp.raster;

CREATE TABLE ctmp.raster (
    id serial4 NOT NULL, -- Identificativo univoco della tabella
    comune varchar(4) NOT NULL, -- Codice catastale del Comune
    sezione varchar(1) NOT NULL, -- Codice sezione censuaria
    foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
    allegato varchar(1) NULL, -- Eventuale codice allegato
    sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
    nome_file varchar(80) NULL, -- Nome del file raster
    geom geometry NOT NULL, -- Geometria del riquadro rappresentante il posizionamento georiferito del raster
    CONSTRAINT raster_pkey PRIMARY KEY (id)
);
CREATE INDEX raster_i1 ON ctmp.raster USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
CREATE INDEX raster_si1 ON ctmp.raster USING gist(geom);
COMMENT ON TABLE ctmp.raster IS 'File raster';

-- Column comments

COMMENT ON COLUMN ctmp.raster.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp.raster.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp.raster.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp.raster.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp.raster.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp.raster.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp.raster.nome_file IS 'Nome del file raster';
COMMENT ON COLUMN ctmp.raster.geom IS 'Geometria del riquadro rappresentante il posizionamento georiferito del raster';
