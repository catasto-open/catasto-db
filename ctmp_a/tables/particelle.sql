-- ctmp_a.particelle definition

-- Drop table

-- DROP TABLE ctmp_a.particelle;

CREATE TABLE ctmp_a.particelle (
    id int4 NOT NULL, -- Identificativo univoco della tabella
    comune varchar(4) NOT NULL, -- Codice catastale del Comune
    sezione varchar(1) NOT NULL, -- Codice sezione censuaria
    foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
    allegato varchar(1) NULL, -- Eventuale codice allegato
    sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
    numero varchar(9) NULL, -- Codice identificativo della particella
    t_altezza numeric(12, 2) NULL, -- Altezza in metri del testo associato
    -- Angolo in gradi che il testo associato forma con l'asse orizzontale
    t_angolo numeric(12, 2) NULL,
    t_pt_ins geometry NULL, -- Punto di inserimento del testo associato
    t_ln_anc geometry NULL, -- Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno alla particella
    geom geometry NOT NULL, -- Geometria della particella
    data_gen varchar(10) NOT NULL, -- Data di generazione della mappa
    stato int4 NOT NULL, -- Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione
    data_crea timestamp NOT NULL, -- Data di creazione del record
    CONSTRAINT particelle_pkey PRIMARY KEY (id, stato)
);
CREATE INDEX particelle_i1 ON ctmp_a.particelle USING btree(
    comune, sezione, foglio, allegato, sviluppo, numero
);
CREATE INDEX particelle_si1 ON ctmp_a.particelle USING gist(geom);
CREATE INDEX particelle_si2 ON ctmp_a.particelle USING gist(t_pt_ins);
CREATE INDEX particelle_si3 ON ctmp_a.particelle USING gist(t_ln_anc);
COMMENT ON TABLE ctmp_a.particelle IS 'Particelle';

-- Column comments

COMMENT ON COLUMN ctmp_a.particelle.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp_a.particelle.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp_a.particelle.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp_a.particelle.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp_a.particelle.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp_a.particelle.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp_a.particelle.numero IS 'Codice identificativo della particella';
COMMENT ON COLUMN ctmp_a.particelle.t_altezza IS 'Altezza in metri del testo associato';
COMMENT ON COLUMN ctmp_a.particelle.t_angolo IS 'Angolo in gradi che il testo associato forma con l''asse orizzontale';
COMMENT ON COLUMN ctmp_a.particelle.t_pt_ins IS 'Punto di inserimento del testo associato';
COMMENT ON COLUMN ctmp_a.particelle.t_ln_anc IS 'Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno alla particella';
COMMENT ON COLUMN ctmp_a.particelle.geom IS 'Geometria della particella';
COMMENT ON COLUMN ctmp_a.particelle.data_gen IS 'Data di generazione della mappa';
COMMENT ON COLUMN ctmp_a.particelle.stato IS 'Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione';
COMMENT ON COLUMN ctmp_a.particelle.data_crea IS 'Data di creazione del record';
