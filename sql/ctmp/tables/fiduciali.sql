-- ctmp.fiduciali definition

-- Drop table

-- DROP TABLE ctmp.fiduciali;

CREATE TABLE ctmp.fiduciali (
    id serial4 NOT NULL, -- Identificativo univoco della tabella
    comune varchar(4) NOT NULL, -- Codice catastale del Comune
    sezione varchar(1) NOT NULL, -- Codice sezione censuaria
    foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
    allegato varchar(1) NULL, -- Eventuale codice allegato
    sviluppo varchar(1) NULL, -- Eventuale codice sviluppo
    prog int4 NOT NULL, -- Numero identificativo del fiduciale
    codice int4 NOT NULL, -- Codice del tipo di fiduciale
    -- Indica se l'elemento si trova all'esterno del confine della mappa
    esterno int4 NOT NULL,
    -- Punto di inserimento del numero identificativo associato al fiduciale
    t_pt_ins geometry NULL,
    geom geometry NOT NULL, -- Punto di inserimento del fiduciale
    CONSTRAINT fiduciali_pkey PRIMARY KEY (id)
);
CREATE INDEX fiduciali_i1 ON ctmp.fiduciali USING btree(
    comune, sezione, foglio, allegato, sviluppo
);
CREATE INDEX fiduciali_si1 ON ctmp.fiduciali USING gist(geom);
CREATE INDEX fiduciali_si2 ON ctmp.fiduciali USING gist(t_pt_ins);
COMMENT ON TABLE ctmp.fiduciali IS 'Punti fiduciali';

-- Column comments

COMMENT ON COLUMN ctmp.fiduciali.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp.fiduciali.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp.fiduciali.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp.fiduciali.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp.fiduciali.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp.fiduciali.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp.fiduciali.prog IS 'Numero identificativo del fiduciale';
COMMENT ON COLUMN ctmp.fiduciali.codice IS 'Codice del tipo di fiduciale';
COMMENT ON COLUMN ctmp.fiduciali.esterno IS 'Indica se l''elemento si trova all''esterno del confine della mappa';
COMMENT ON COLUMN ctmp.fiduciali.t_pt_ins IS 'Punto di inserimento del numero identificativo associato al fiduciale';
COMMENT ON COLUMN ctmp.fiduciali.geom IS 'Punto di inserimento del fiduciale';
