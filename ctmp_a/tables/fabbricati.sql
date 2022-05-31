-- ctmp_a.fabbricati definition

-- Drop table

-- DROP TABLE ctmp_a.fabbricati;

CREATE TABLE ctmp_a.fabbricati (
	id int4 NOT NULL, -- Identificativo univoco della tabella
	comune varchar(4) NOT NULL, -- Codice catastale del Comune
	sezione varchar(1) NOT NULL, -- Codice sezione censuaria
	foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
	allegato varchar(1) NULL, -- Eventuale codice allegato
	sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
	numero varchar(9) NULL, -- Codice identificativo della particella contenente il fabbricato
	t_altezza numeric(12, 2) NULL, -- Altezza in metri del testo associato
	t_angolo numeric(12, 2) NULL, -- Angolo in gradi che il testo associato forma con l'asse orizzontale
	t_pt_ins geometry NULL, -- Punto di inserimento del testo associato
	t_ln_anc geometry NULL, -- Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno al fabbricato
	geom geometry NOT NULL, -- Geometria del fabbricato
	data_gen varchar(10) NOT NULL, -- Data di generazione della mappa
	stato int4 NOT NULL, -- Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione
	data_crea timestamp NOT NULL, -- Data di creazione del record
	CONSTRAINT fabbricati_pkey PRIMARY KEY (id, stato)
);
CREATE INDEX fabbricati_i1 ON ctmp_a.fabbricati USING btree (comune, sezione, foglio, allegato, sviluppo, numero);
CREATE INDEX fabbricati_si1 ON ctmp_a.fabbricati USING gist (geom);
CREATE INDEX fabbricati_si2 ON ctmp_a.fabbricati USING gist (t_pt_ins);
CREATE INDEX fabbricati_si3 ON ctmp_a.fabbricati USING gist (t_ln_anc);
COMMENT ON TABLE ctmp_a.fabbricati IS 'Fabbricati';

-- Column comments

COMMENT ON COLUMN ctmp_a.fabbricati.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp_a.fabbricati.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp_a.fabbricati.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp_a.fabbricati.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp_a.fabbricati.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp_a.fabbricati.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp_a.fabbricati.numero IS 'Codice identificativo della particella contenente il fabbricato';
COMMENT ON COLUMN ctmp_a.fabbricati.t_altezza IS 'Altezza in metri del testo associato';
COMMENT ON COLUMN ctmp_a.fabbricati.t_angolo IS 'Angolo in gradi che il testo associato forma con l''asse orizzontale';
COMMENT ON COLUMN ctmp_a.fabbricati.t_pt_ins IS 'Punto di inserimento del testo associato';
COMMENT ON COLUMN ctmp_a.fabbricati.t_ln_anc IS 'Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno al fabbricato';
COMMENT ON COLUMN ctmp_a.fabbricati.geom IS 'Geometria del fabbricato';
COMMENT ON COLUMN ctmp_a.fabbricati.data_gen IS 'Data di generazione della mappa';
COMMENT ON COLUMN ctmp_a.fabbricati.stato IS 'Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione';
COMMENT ON COLUMN ctmp_a.fabbricati.data_crea IS 'Data di creazione del record';