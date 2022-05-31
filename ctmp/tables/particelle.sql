-- ctmp.particelle definition

-- Drop table

-- DROP TABLE ctmp.particelle;

CREATE TABLE ctmp.particelle (
	id serial4 NOT NULL, -- Identificativo univoco della tabella
	comune varchar(4) NOT NULL, -- Codice catastale del Comune
	sezione varchar(1) NOT NULL, -- Codice sezione censuaria
	foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
	allegato varchar(1) NULL, -- Eventuale codice allegato
	sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
	numero varchar(9) NULL, -- Codice identificativo della particella
	t_altezza numeric(12, 2) NULL, -- Altezza in metri del testo associato
	t_angolo numeric(12, 2) NULL, -- Angolo in gradi che il testo associato forma con l'asse orizzontale
	t_pt_ins geometry NULL, -- Punto di inserimento del testo associato
	t_ln_anc geometry NULL, -- Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno alla particella
	geom geometry NOT NULL, -- Geometria della particella
	CONSTRAINT particelle_pkey PRIMARY KEY (id)
);
CREATE INDEX particelle_i1 ON ctmp.particelle USING btree (comune, sezione, foglio, allegato, sviluppo, numero);
CREATE INDEX particelle_si1 ON ctmp.particelle USING gist (geom);
CREATE INDEX particelle_si2 ON ctmp.particelle USING gist (t_pt_ins);
CREATE INDEX particelle_si3 ON ctmp.particelle USING gist (t_ln_anc);
COMMENT ON TABLE ctmp.particelle IS 'Particelle';

-- Column comments

COMMENT ON COLUMN ctmp.particelle.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp.particelle.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp.particelle.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp.particelle.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp.particelle.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp.particelle.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp.particelle.numero IS 'Codice identificativo della particella';
COMMENT ON COLUMN ctmp.particelle.t_altezza IS 'Altezza in metri del testo associato';
COMMENT ON COLUMN ctmp.particelle.t_angolo IS 'Angolo in gradi che il testo associato forma con l''asse orizzontale';
COMMENT ON COLUMN ctmp.particelle.t_pt_ins IS 'Punto di inserimento del testo associato';
COMMENT ON COLUMN ctmp.particelle.t_ln_anc IS 'Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno alla particella';
COMMENT ON COLUMN ctmp.particelle.geom IS 'Geometria della particella';