-- ctmp_a.quadri_unione definition

-- Drop table

-- DROP TABLE ctmp_a.quadri_unione;

CREATE TABLE ctmp_a.quadri_unione (
    id int4 NOT NULL, -- Identificativo univoco della tabella
    comune varchar(4) NOT NULL, -- Codice catastale del Comune
    sezione varchar(1) NOT NULL, -- Codice sezione censuaria
    foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
    allegato varchar(1) NULL, -- Eventuale codice allegato
    sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
    t_altezza numeric(12, 2) NULL, -- Altezza in metri del testo associato
    -- Angolo in gradi che il testo associato forma con l'asse orizzontale
    t_angolo numeric(12, 2) NULL,
    t_pt_ins geometry NULL, -- Punto di inserimento del testo associato
    t_ln_anc geometry NULL, -- Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno al foglio
    geom geometry NOT NULL, -- Geometria del foglio
    data_gen varchar(10) NOT NULL, -- Data di generazione della mappa
    stato int4 NOT NULL, -- Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione
    data_crea timestamp NOT NULL, -- Data di creazione del record
    CONSTRAINT quadri_unione_pkey PRIMARY KEY (id, stato)
);
CREATE INDEX quadri_unione_i1 ON ctmp_a.quadri_unione USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
CREATE INDEX quadri_unione_si1 ON ctmp_a.quadri_unione USING gist(geom);
CREATE INDEX quadri_unione_si2 ON ctmp_a.quadri_unione USING gist(t_pt_ins);
CREATE INDEX quadri_unione_si3 ON ctmp_a.quadri_unione USING gist(t_ln_anc);
COMMENT ON TABLE ctmp_a.quadri_unione IS 'Fogli';

-- Column comments

COMMENT ON COLUMN ctmp_a.quadri_unione.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp_a.quadri_unione.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp_a.quadri_unione.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp_a.quadri_unione.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp_a.quadri_unione.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp_a.quadri_unione.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp_a.quadri_unione.t_altezza IS 'Altezza in metri del testo associato';
COMMENT ON COLUMN ctmp_a.quadri_unione.t_angolo IS 'Angolo in gradi che il testo associato forma con l''asse orizzontale';
COMMENT ON COLUMN ctmp_a.quadri_unione.t_pt_ins IS 'Punto di inserimento del testo associato';
COMMENT ON COLUMN ctmp_a.quadri_unione.t_ln_anc IS 'Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno al foglio';
COMMENT ON COLUMN ctmp_a.quadri_unione.geom IS 'Geometria del foglio';
COMMENT ON COLUMN ctmp_a.quadri_unione.data_gen IS 'Data di generazione della mappa';
COMMENT ON COLUMN ctmp_a.quadri_unione.stato IS 'Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione';
COMMENT ON COLUMN ctmp_a.quadri_unione.data_crea IS 'Data di creazione del record';
