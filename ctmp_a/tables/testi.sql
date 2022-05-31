-- ctmp_a.testi definition

-- Drop table

-- DROP TABLE ctmp_a.testi;

CREATE TABLE ctmp_a.testi (
	id int4 NOT NULL, -- Identificativo univoco della tabella
	comune varchar(4) NOT NULL, -- Codice catastale del Comune
	sezione varchar(1) NOT NULL, -- Codice sezione censuaria
	foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
	allegato varchar(1) NULL, -- Eventuale codice allegato
	sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
	testo varchar(80) NULL, -- Testo
	altezza numeric(12, 2) NULL, -- Altezza in metri del testo
	angolo numeric(12, 2) NULL, -- Angolo in gradi che il testo forma con l'asse orizzontale
	esterno int4 NOT NULL, -- Indica se l'elemento si trova all'esterno del confine della mappa
	geom geometry NOT NULL, -- Punto di inserimento del testo
	data_gen varchar(10) NOT NULL, -- Data di generazione della mappa
	stato int4 NOT NULL, -- Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione
	data_crea timestamp NOT NULL, -- Data di creazione del record
	CONSTRAINT testi_pkey PRIMARY KEY (id, stato)
);
CREATE INDEX testi_i1 ON ctmp_a.testi USING btree (comune, sezione, foglio, allegato, sviluppo);
CREATE INDEX testi_si1 ON ctmp_a.testi USING gist (geom);
COMMENT ON TABLE ctmp_a.testi IS 'Testi';

-- Column comments

COMMENT ON COLUMN ctmp_a.testi.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp_a.testi.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp_a.testi.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp_a.testi.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp_a.testi.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp_a.testi.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp_a.testi.testo IS 'Testo';
COMMENT ON COLUMN ctmp_a.testi.altezza IS 'Altezza in metri del testo';
COMMENT ON COLUMN ctmp_a.testi.angolo IS 'Angolo in gradi che il testo forma con l''asse orizzontale';
COMMENT ON COLUMN ctmp_a.testi.esterno IS 'Indica se l''elemento si trova all''esterno del confine della mappa';
COMMENT ON COLUMN ctmp_a.testi.geom IS 'Punto di inserimento del testo';
COMMENT ON COLUMN ctmp_a.testi.data_gen IS 'Data di generazione della mappa';
COMMENT ON COLUMN ctmp_a.testi.stato IS 'Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione';
COMMENT ON COLUMN ctmp_a.testi.data_crea IS 'Data di creazione del record';