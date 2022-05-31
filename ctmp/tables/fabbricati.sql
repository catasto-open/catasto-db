-- ctmp.fabbricati definition

-- Drop table

-- DROP TABLE ctmp.fabbricati;

CREATE TABLE ctmp.fabbricati (
	id serial4 NOT NULL, -- Identificativo univoco della tabella
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
	CONSTRAINT fabbricati_pkey PRIMARY KEY (id)
);
CREATE INDEX fabbricati_i1 ON ctmp.fabbricati USING btree (comune, sezione, foglio, allegato, sviluppo, numero);
CREATE INDEX fabbricati_si1 ON ctmp.fabbricati USING gist (geom);
CREATE INDEX fabbricati_si2 ON ctmp.fabbricati USING gist (t_pt_ins);
CREATE INDEX fabbricati_si3 ON ctmp.fabbricati USING gist (t_ln_anc);
COMMENT ON TABLE ctmp.fabbricati IS 'Fabbricati';

-- Column comments

COMMENT ON COLUMN ctmp.fabbricati.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp.fabbricati.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp.fabbricati.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp.fabbricati.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp.fabbricati.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp.fabbricati.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp.fabbricati.numero IS 'Codice identificativo della particella contenente il fabbricato';
COMMENT ON COLUMN ctmp.fabbricati.t_altezza IS 'Altezza in metri del testo associato';
COMMENT ON COLUMN ctmp.fabbricati.t_angolo IS 'Angolo in gradi che il testo associato forma con l''asse orizzontale';
COMMENT ON COLUMN ctmp.fabbricati.t_pt_ins IS 'Punto di inserimento del testo associato';
COMMENT ON COLUMN ctmp.fabbricati.t_ln_anc IS 'Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno al fabbricato';
COMMENT ON COLUMN ctmp.fabbricati.geom IS 'Geometria del fabbricato';