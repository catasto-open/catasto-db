-- ctmp.testi definition

-- Drop table

-- DROP TABLE ctmp.testi;

CREATE TABLE ctmp.testi (
	id serial4 NOT NULL, -- Identificativo univoco della tabella
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
	CONSTRAINT testi_pkey PRIMARY KEY (id)
);
CREATE INDEX testi_i1 ON ctmp.testi USING btree (comune, sezione, foglio, allegato, sviluppo);
CREATE INDEX testi_si1 ON ctmp.testi USING gist (geom);
COMMENT ON TABLE ctmp.testi IS 'Testi';

-- Column comments

COMMENT ON COLUMN ctmp.testi.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp.testi.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp.testi.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp.testi.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp.testi.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp.testi.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp.testi.testo IS 'Testo';
COMMENT ON COLUMN ctmp.testi.altezza IS 'Altezza in metri del testo';
COMMENT ON COLUMN ctmp.testi.angolo IS 'Angolo in gradi che il testo forma con l''asse orizzontale';
COMMENT ON COLUMN ctmp.testi.esterno IS 'Indica se l''elemento si trova all''esterno del confine della mappa';
COMMENT ON COLUMN ctmp.testi.geom IS 'Punto di inserimento del testo';