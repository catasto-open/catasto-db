-- ctmp_a.linee_vest definition

-- Drop table

-- DROP TABLE ctmp_a.linee_vest;

CREATE TABLE ctmp_a.linee_vest (
    id int4 NOT NULL, -- Identificativo univoco della tabella
    comune varchar(4) NOT NULL, -- Codice catastale del Comune
    sezione varchar(1) NOT NULL, -- Codice sezione censuaria
    foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
    allegato varchar(1) NULL, -- Eventuale codice allegato
    sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
    codice int4 NOT NULL, -- Codice del tipo di tratto
    -- Indica se l'elemento si trova all'esterno del confine della mappa
    esterno int4 NOT NULL,
    geom geometry NOT NULL, -- Geometria della linea
    data_gen varchar(10) NOT NULL, -- Data di generazione della mappa
    stato int4 NOT NULL, -- Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione
    data_crea timestamp NOT NULL, -- Data di creazione del record
    CONSTRAINT linee_vest_pkey PRIMARY KEY (id, stato)
);
CREATE INDEX linee_vest_i1 ON ctmp_a.linee_vest USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
CREATE INDEX linee_vest_si1 ON ctmp_a.linee_vest USING gist(geom);
COMMENT ON TABLE ctmp_a.linee_vest IS 'Linee di vestizione';

-- Column comments

COMMENT ON COLUMN ctmp_a.linee_vest.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp_a.linee_vest.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp_a.linee_vest.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp_a.linee_vest.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp_a.linee_vest.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp_a.linee_vest.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp_a.linee_vest.codice IS 'Codice del tipo di tratto';
COMMENT ON COLUMN ctmp_a.linee_vest.esterno IS 'Indica se l''elemento si trova all''esterno del confine della mappa';
COMMENT ON COLUMN ctmp_a.linee_vest.geom IS 'Geometria della linea';
COMMENT ON COLUMN ctmp_a.linee_vest.data_gen IS 'Data di generazione della mappa';
COMMENT ON COLUMN ctmp_a.linee_vest.stato IS 'Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione';
COMMENT ON COLUMN ctmp_a.linee_vest.data_crea IS 'Data di creazione del record';
