-- ctmp_a.simboli definition

-- Drop table

-- DROP TABLE ctmp_a.simboli;

CREATE TABLE ctmp_a.simboli (
    id int4 NOT NULL, -- Identificativo univoco della tabella
    comune varchar(4) NOT NULL, -- Codice catastale del Comune
    sezione varchar(1) NOT NULL, -- Codice sezione censuaria
    foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
    allegato varchar(1) NULL, -- Eventuale codice allegato
    sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
    codice int4 NOT NULL, -- Codice del tipo di simbolo
    -- Angolo in gradi che il simbolo forma con l'asse orizzontale
    angolo numeric(12, 2) NULL,
    -- Indica se l'elemento si trova all'esterno del confine della mappa
    esterno int4 NOT NULL,
    geom geometry NOT NULL, -- Punto di inserimento del simbolo
    data_gen varchar(10) NOT NULL, -- Data di generazione della mappa
    stato int4 NOT NULL, -- Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione
    data_crea timestamp NOT NULL, -- Data di creazione del record
    CONSTRAINT simboli_pkey PRIMARY KEY (id, stato)
);
CREATE INDEX simboli_i1 ON ctmp_a.simboli USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
CREATE INDEX simboli_si1 ON ctmp_a.simboli USING gist(geom);
COMMENT ON TABLE ctmp_a.simboli IS 'Simboli';

-- Column comments

COMMENT ON COLUMN ctmp_a.simboli.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp_a.simboli.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp_a.simboli.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp_a.simboli.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp_a.simboli.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp_a.simboli.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp_a.simboli.codice IS 'Codice del tipo di simbolo';
COMMENT ON COLUMN ctmp_a.simboli.angolo IS 'Angolo in gradi che il simbolo forma con l''asse orizzontale';
COMMENT ON COLUMN ctmp_a.simboli.esterno IS 'Indica se l''elemento si trova all''esterno del confine della mappa';
COMMENT ON COLUMN ctmp_a.simboli.geom IS 'Punto di inserimento del simbolo';
COMMENT ON COLUMN ctmp_a.simboli.data_gen IS 'Data di generazione della mappa';
COMMENT ON COLUMN ctmp_a.simboli.stato IS 'Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione';
COMMENT ON COLUMN ctmp_a.simboli.data_crea IS 'Data di creazione del record';
