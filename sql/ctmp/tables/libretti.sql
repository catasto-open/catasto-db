-- ctmp.libretti definition

-- Drop table

-- DROP TABLE ctmp.libretti;

CREATE TABLE ctmp.libretti (
    id serial4 NOT NULL, -- Identificativo univoco della tabella
    comune varchar(4) NOT NULL, -- Codice catastale del Comune
    sezione varchar(1) NOT NULL, -- Codice sezione censuaria
    foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
    allegato varchar(1) NULL, -- Eventuale codice allegato
    sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
    protocollo varchar(80) NULL, -- Numero di protocollo del libretto
    codice int4 NOT NULL, -- Codice del tipo di tratto della linea
    geom geometry NOT NULL, -- Geometria del libretto
    CONSTRAINT libretti_pkey PRIMARY KEY (id)
);
CREATE INDEX libretti_i1 ON ctmp.libretti USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
CREATE INDEX libretti_si1 ON ctmp.libretti USING gist(geom);
COMMENT ON TABLE ctmp.libretti IS 'Libretti';

-- Column comments

COMMENT ON COLUMN ctmp.libretti.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp.libretti.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp.libretti.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp.libretti.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp.libretti.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp.libretti.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp.libretti.protocollo IS 'Numero di protocollo del libretto';
COMMENT ON COLUMN ctmp.libretti.codice IS 'Codice del tipo di tratto della linea';
COMMENT ON COLUMN ctmp.libretti.geom IS 'Geometria del libretto';
