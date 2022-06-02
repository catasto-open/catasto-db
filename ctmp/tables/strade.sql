-- ctmp.strade definition

-- Drop table

-- DROP TABLE ctmp.strade;

CREATE TABLE ctmp.strade (
    id serial4 NOT NULL, -- Identificativo univoco della tabella
    comune varchar(4) NOT NULL, -- Codice catastale del Comune
    sezione varchar(1) NOT NULL, -- Codice sezione censuaria
    foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
    allegato varchar(1) NULL, -- Eventuale codice allegato
    sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
    numero varchar(9) NULL, -- Eventuale codice identificativo della strada presente nelle mappe di tipo FONDIARIO
    t_altezza numeric(12, 2) NULL, -- Altezza in metri del testo associato
    -- Angolo in gradi che il testo associato forma con l'asse orizzontale
    t_angolo numeric(12, 2) NULL,
    t_pt_ins geometry NULL, -- Punto di inserimento del testo associato
    t_ln_anc geometry NULL, -- Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno al contorno
    geom geometry NOT NULL, -- Geometria del contorno della strada
    CONSTRAINT strade_pkey PRIMARY KEY (id)
);
CREATE INDEX strade_i1 ON ctmp.strade USING btree(
    comune, sezione, foglio, allegato, sviluppo, numero
);
CREATE INDEX strade_si1 ON ctmp.strade USING gist(geom);
CREATE INDEX strade_si2 ON ctmp.strade USING gist(t_pt_ins);
CREATE INDEX strade_si3 ON ctmp.strade USING gist(t_ln_anc);
COMMENT ON TABLE ctmp.strade IS 'Contorni delle strade';

-- Column comments

COMMENT ON COLUMN ctmp.strade.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp.strade.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp.strade.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp.strade.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp.strade.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp.strade.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp.strade.numero IS 'Eventuale codice identificativo della strada presente nelle mappe di tipo FONDIARIO';
COMMENT ON COLUMN ctmp.strade.t_altezza IS 'Altezza in metri del testo associato';
COMMENT ON COLUMN ctmp.strade.t_angolo IS 'Angolo in gradi che il testo associato forma con l''asse orizzontale';
COMMENT ON COLUMN ctmp.strade.t_pt_ins IS 'Punto di inserimento del testo associato';
COMMENT ON COLUMN ctmp.strade.t_ln_anc IS 'Eventuale linea di ancoraggio tra il punto di inserimento del testo ed un punto interno al contorno';
COMMENT ON COLUMN ctmp.strade.geom IS 'Geometria del contorno della strada';
