-- ctmp.fogli definition

-- Drop table

-- DROP TABLE ctmp.fogli;

CREATE TABLE ctmp.fogli (
	id serial4 NOT NULL, -- Identificativo univoco della tabella
	comune varchar(4) NOT NULL, -- Codice catastale del Comune
	sezione varchar(1) NOT NULL, -- Codice sezione censuaria
	foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
	allegato varchar(1) NULL, -- Eventuale codice allegato
	sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
	t_altezza numeric(12, 2) NULL, -- Altezza in metri del testo associato
	t_angolo numeric(12, 2) NULL, -- Angolo in gradi che il testo associato forma con l'asse orizzontale
	t_pt_ins geometry NULL, -- Punto di inserimento del testo associato
	t_ln_anc geometry NULL, -- Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno al foglio
	geom geometry NOT NULL, -- Geometria del foglio
	CONSTRAINT fogli_pkey PRIMARY KEY (id)
);
CREATE INDEX fogli_i1 ON ctmp.fogli USING btree (comune, sezione, foglio, allegato, sviluppo);
CREATE INDEX fogli_idx_comune01 ON ctmp.fogli USING btree (comune);
CREATE INDEX fogli_si1 ON ctmp.fogli USING gist (geom);
CREATE INDEX fogli_si2 ON ctmp.fogli USING gist (t_pt_ins);
CREATE INDEX fogli_si3 ON ctmp.fogli USING gist (t_ln_anc);
COMMENT ON TABLE ctmp.fogli IS 'Fogli';

-- Column comments

COMMENT ON COLUMN ctmp.fogli.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp.fogli.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp.fogli.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp.fogli.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp.fogli.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp.fogli.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp.fogli.t_altezza IS 'Altezza in metri del testo associato';
COMMENT ON COLUMN ctmp.fogli.t_angolo IS 'Angolo in gradi che il testo associato forma con l''asse orizzontale';
COMMENT ON COLUMN ctmp.fogli.t_pt_ins IS 'Punto di inserimento del testo associato';
COMMENT ON COLUMN ctmp.fogli.t_ln_anc IS 'Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno al foglio';
COMMENT ON COLUMN ctmp.fogli.geom IS 'Geometria del foglio';