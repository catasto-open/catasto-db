-- ctmp_a.libretti definition

-- Drop table

-- DROP TABLE ctmp_a.libretti;

CREATE TABLE ctmp_a.libretti (
    id int4 NOT NULL, -- Identificativo univoco della tabella
    comune varchar(4) NOT NULL, -- Codice catastale del Comune
    sezione varchar(1) NOT NULL, -- Codice sezione censuaria
    foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
    allegato varchar(1) NULL, -- Eventuale codice allegato
    sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
    protocollo varchar(80) NULL, -- Numero di protocollo del libretto
    codice int4 NOT NULL, -- Codice del tipo di tratto della linea
    geom geometry NOT NULL, -- Geometria del libretto
    data_gen varchar(10) NOT NULL, -- Data di generazione della mappa
    stato int4 NOT NULL, -- Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione
    data_crea timestamp NOT NULL, -- Data di creazione del record
    CONSTRAINT libretti_pkey PRIMARY KEY (id, stato)
);
CREATE INDEX libretti_i1 ON ctmp_a.libretti USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
CREATE INDEX libretti_si1 ON ctmp_a.libretti USING gist(geom);
COMMENT ON TABLE ctmp_a.libretti IS 'Libretti';

-- Column comments

COMMENT ON COLUMN ctmp_a.libretti.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp_a.libretti.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp_a.libretti.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp_a.libretti.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp_a.libretti.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp_a.libretti.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp_a.libretti.protocollo IS 'Numero di protocollo del libretto';
COMMENT ON COLUMN ctmp_a.libretti.codice IS 'Codice del tipo di tratto della linea';
COMMENT ON COLUMN ctmp_a.libretti.geom IS 'Geometria del libretto';
COMMENT ON COLUMN ctmp_a.libretti.data_gen IS 'Data di generazione della mappa';
COMMENT ON COLUMN ctmp_a.libretti.stato IS 'Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione';
COMMENT ON COLUMN ctmp_a.libretti.data_crea IS 'Data di creazione del record';
