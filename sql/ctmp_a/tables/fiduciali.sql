-- ctmp_a.fiduciali definition

-- Drop table

-- DROP TABLE ctmp_a.fiduciali;

CREATE TABLE ctmp_a.fiduciali (
    id int4 NOT NULL, -- Identificativo univoco della tabella
    comune varchar(4) NOT NULL, -- Codice catastale del Comune
    sezione varchar(1) NOT NULL, -- Codice sezione censuaria
    foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
    allegato varchar(1) NULL, -- Eventuale codice allegato
    sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
    prog int4 NOT NULL, -- Numero identificativo del fiduciale
    codice int4 NOT NULL, -- Codice del tipo di fiduciale
    -- Indica se l'elemento si trova all'esterno del confine della mappa
    esterno int4 NOT NULL,
    -- Punto di inserimento del numero identificativo associato al fiduciale
    t_pt_ins geometry NULL,
    geom geometry NOT NULL, -- Punto di inserimento del fiduciale
    data_gen varchar(10) NOT NULL, -- Data di generazione della mappa
    stato int4 NOT NULL, -- Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione
    data_crea timestamp NOT NULL, -- Data di creazione del record
    CONSTRAINT fiduciali_pkey PRIMARY KEY (id, stato)
);
CREATE INDEX fiduciali_i1 ON ctmp_a.fiduciali USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
CREATE INDEX fiduciali_si1 ON ctmp_a.fiduciali USING gist(geom);
CREATE INDEX fiduciali_si2 ON ctmp_a.fiduciali USING gist(t_pt_ins);
COMMENT ON TABLE ctmp_a.fiduciali IS 'Punti fiduciali';

-- Column comments

COMMENT ON COLUMN ctmp_a.fiduciali.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp_a.fiduciali.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp_a.fiduciali.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp_a.fiduciali.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp_a.fiduciali.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp_a.fiduciali.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp_a.fiduciali.prog IS 'Numero identificativo del fiduciale';
COMMENT ON COLUMN ctmp_a.fiduciali.codice IS 'Codice del tipo di fiduciale';
COMMENT ON COLUMN ctmp_a.fiduciali.esterno IS 'Indica se l''elemento si trova all''esterno del confine della mappa';
COMMENT ON COLUMN ctmp_a.fiduciali.t_pt_ins IS 'Punto di inserimento del numero identificativo associato al fiduciale';
COMMENT ON COLUMN ctmp_a.fiduciali.geom IS 'Punto di inserimento del fiduciale';
COMMENT ON COLUMN ctmp_a.fiduciali.data_gen IS 'Data di generazione della mappa';
COMMENT ON COLUMN ctmp_a.fiduciali.stato IS 'Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione';
COMMENT ON COLUMN ctmp_a.fiduciali.data_crea IS 'Data di creazione del record';
