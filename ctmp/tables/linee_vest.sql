-- ctmp.linee_vest definition

-- Drop table

-- DROP TABLE ctmp.linee_vest;

CREATE TABLE ctmp.linee_vest (
	id serial4 NOT NULL, -- Identificativo univoco della tabella
	comune varchar(4) NOT NULL, -- Codice catastale del Comune
	sezione varchar(1) NOT NULL, -- Codice sezione censuaria
	foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
	allegato varchar(1) NULL, -- Eventuale codice allegato
	sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
	codice int4 NOT NULL, -- Codice del tipo di tratto
	esterno int4 NOT NULL, -- Indica se l'elemento si trova all'esterno del confine della mappa
	geom geometry NOT NULL, -- Geometria della linea
	CONSTRAINT linee_vest_pkey PRIMARY KEY (id)
);
CREATE INDEX linee_vest_i1 ON ctmp.linee_vest USING btree (comune, sezione, foglio, allegato, sviluppo);
CREATE INDEX linee_vest_si1 ON ctmp.linee_vest USING gist (geom);
COMMENT ON TABLE ctmp.linee_vest IS 'Linee di vestizione';

-- Column comments

COMMENT ON COLUMN ctmp.linee_vest.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp.linee_vest.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp.linee_vest.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp.linee_vest.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp.linee_vest.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp.linee_vest.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp.linee_vest.codice IS 'Codice del tipo di tratto';
COMMENT ON COLUMN ctmp.linee_vest.esterno IS 'Indica se l''elemento si trova all''esterno del confine della mappa';
COMMENT ON COLUMN ctmp.linee_vest.geom IS 'Geometria della linea';