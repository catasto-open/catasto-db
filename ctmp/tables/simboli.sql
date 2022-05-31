-- ctmp.simboli definition

-- Drop table

-- DROP TABLE ctmp.simboli;

CREATE TABLE ctmp.simboli (
	id serial4 NOT NULL, -- Identificativo univoco della tabella
	comune varchar(4) NOT NULL, -- Codice catastale del Comune
	sezione varchar(1) NOT NULL, -- Codice sezione censuaria
	foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
	allegato varchar(1) NULL, -- Eventuale codice allegato
	sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
	codice int4 NOT NULL, -- Codice del tipo di simbolo
	angolo numeric(12, 2) NULL, -- Angolo in gradi che il simbolo forma con l'asse orizzontale
	esterno int4 NOT NULL, -- Indica se l'elemento si trova all'esterno del confine della mappa
	geom geometry NOT NULL, -- Punto di inserimento del simbolo
	CONSTRAINT simboli_pkey PRIMARY KEY (id)
);
CREATE INDEX simboli_i1 ON ctmp.simboli USING btree (comune, sezione, foglio, allegato, sviluppo);
CREATE INDEX simboli_si1 ON ctmp.simboli USING gist (geom);
COMMENT ON TABLE ctmp.simboli IS 'Simboli';

-- Column comments

COMMENT ON COLUMN ctmp.simboli.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp.simboli.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp.simboli.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp.simboli.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp.simboli.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp.simboli.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp.simboli.codice IS 'Codice del tipo di simbolo';
COMMENT ON COLUMN ctmp.simboli.angolo IS 'Angolo in gradi che il simbolo forma con l''asse orizzontale';
COMMENT ON COLUMN ctmp.simboli.esterno IS 'Indica se l''elemento si trova all''esterno del confine della mappa';
COMMENT ON COLUMN ctmp.simboli.geom IS 'Punto di inserimento del simbolo';