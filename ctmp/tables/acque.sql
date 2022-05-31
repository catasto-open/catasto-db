-- ctmp.acque definition

-- Drop table

-- DROP TABLE ctmp.acque;

CREATE TABLE ctmp.acque (
	id serial4 NOT NULL, -- Identificativo univoco della tabella
	comune varchar(4) NOT NULL, -- Codice catastale del Comune
	sezione varchar(1) NOT NULL, -- Codice sezione censuaria
	foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
	allegato varchar(1) NULL, -- Eventuale codice allegato
	sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
	numero varchar(9) NULL, -- Eventuale codice identificativo dell'acqua presente nelle mappe di tipo FONDIARIO
	t_altezza numeric(12, 2) NULL, -- Altezza in metri del testo associato
	t_angolo numeric(12, 2) NULL, -- Angolo in gradi che il testo associato forma con l'asse orizzontale
	t_pt_ins geometry NULL, -- Punto di inserimento del testo associato
	t_ln_anc geometry NULL, -- Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno al contorno
	geom geometry NOT NULL, -- Geometria del contorno dell'acqua
	CONSTRAINT acque_pkey PRIMARY KEY (id)
);
CREATE INDEX acque_i1 ON ctmp.acque USING btree (comune, sezione, foglio, allegato, sviluppo, numero);
CREATE INDEX acque_si1 ON ctmp.acque USING gist (geom);
CREATE INDEX acque_si2 ON ctmp.acque USING gist (t_pt_ins);
CREATE INDEX acque_si3 ON ctmp.acque USING gist (t_ln_anc);
COMMENT ON TABLE ctmp.acque IS 'Contorni delle acque';

-- Column comments

COMMENT ON COLUMN ctmp.acque.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp.acque.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp.acque.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp.acque.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp.acque.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp.acque.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp.acque.numero IS 'Eventuale codice identificativo dell''acqua presente nelle mappe di tipo FONDIARIO';
COMMENT ON COLUMN ctmp.acque.t_altezza IS 'Altezza in metri del testo associato';
COMMENT ON COLUMN ctmp.acque.t_angolo IS 'Angolo in gradi che il testo associato forma con l''asse orizzontale';
COMMENT ON COLUMN ctmp.acque.t_pt_ins IS 'Punto di inserimento del testo associato';
COMMENT ON COLUMN ctmp.acque.t_ln_anc IS 'Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno al contorno';
COMMENT ON COLUMN ctmp.acque.geom IS 'Geometria del contorno dell''acqua';