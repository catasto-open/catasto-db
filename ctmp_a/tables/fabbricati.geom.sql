-- ctmp_a."fabbricati.geom" definition

-- Drop table

-- DROP TABLE ctmp_a."fabbricati.geom";

CREATE TABLE ctmp_a."fabbricati.geom" (
	id_0 serial4 NOT NULL,
	geom geometry(polygon, 25833) NULL,
	id int4 NULL, -- Identificativo univoco della tabella
	comune varchar(4) NULL, -- Codice catastale del Comune
	sezione varchar(1) NULL, -- Codice sezione censuaria
	foglio varchar(4) NULL, -- Codice identificativo del foglio
	allegato varchar(1) NULL, -- Eventuale codice allegato
	sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
	numero varchar(9) NULL, -- Codice identificativo della particella contenente il fabbricato
	t_altezza float8 NULL, -- Altezza in metri del testo associato
	t_angolo float8 NULL, -- Angolo in gradi che il testo associato forma con l'asse orizzontale
	t_pt_ins varchar NULL, -- Punto di inserimento del testo associato
	t_ln_anc varchar NULL, -- Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno al fabbricato
	data_gen varchar(10) NULL, -- Data di generazione della mappa
	stato int4 NULL, -- Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione
	data_crea timestamp NULL, -- Data di creazione del record
	CONSTRAINT "fabbricati.geom_pkey" PRIMARY KEY (id_0)
);

-- Column comments

COMMENT ON COLUMN ctmp_a."fabbricati.geom".id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp_a."fabbricati.geom".comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp_a."fabbricati.geom".sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp_a."fabbricati.geom".foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp_a."fabbricati.geom".allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp_a."fabbricati.geom".sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp_a."fabbricati.geom".numero IS 'Codice identificativo della particella contenente il fabbricato';
COMMENT ON COLUMN ctmp_a."fabbricati.geom".t_altezza IS 'Altezza in metri del testo associato';
COMMENT ON COLUMN ctmp_a."fabbricati.geom".t_angolo IS 'Angolo in gradi che il testo associato forma con l''asse orizzontale';
COMMENT ON COLUMN ctmp_a."fabbricati.geom".t_pt_ins IS 'Punto di inserimento del testo associato';
COMMENT ON COLUMN ctmp_a."fabbricati.geom".t_ln_anc IS 'Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno al fabbricato';
COMMENT ON COLUMN ctmp_a."fabbricati.geom".data_gen IS 'Data di generazione della mappa';
COMMENT ON COLUMN ctmp_a."fabbricati.geom".stato IS 'Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione';
COMMENT ON COLUMN ctmp_a."fabbricati.geom".data_crea IS 'Data di creazione del record';