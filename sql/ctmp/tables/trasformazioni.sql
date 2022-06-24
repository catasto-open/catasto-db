-- ctmp.trasformazioni definition

-- Drop table

-- DROP TABLE ctmp.trasformazioni;

CREATE TABLE ctmp.trasformazioni ( -- noqa: PRS
    comune varchar(4) NOT NULL, -- Codice catastale del Comune
    sezione varchar(1) NOT NULL, -- Codice sezione censuaria
    foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
    allegato varchar(1) NOT NULL, -- Eventuale codice allegato
    sviluppo varchar(1) NOT NULL, -- Eventuale codice sviluppo
    n_trasf int4 NOT NULL, -- Numero ordinale della trasformazione
    tipo_trasf varchar(20) NOT NULL, -- Codice del tipo di trasformazione
    punti_contr _float8 NOT NULL, -- Punti di controllo usati per creare la matrice di trasformazione
    matrice_trasf _float8 NOT NULL, -- Matrice di trasformazione
    CONSTRAINT trasformazioni_pkey PRIMARY KEY (comune, sezione, foglio, allegato, sviluppo, n_trasf)
);
COMMENT ON TABLE ctmp.trasformazioni IS 'Trasformazioni eseguite sui fogli';

-- Column comments

COMMENT ON COLUMN ctmp.trasformazioni.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp.trasformazioni.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp.trasformazioni.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp.trasformazioni.allegato IS 'Eventuale codice allegato';
COMMENT ON COLUMN ctmp.trasformazioni.sviluppo IS 'Eventuale codice sviluppo';
COMMENT ON COLUMN ctmp.trasformazioni.n_trasf IS 'Numero ordinale della trasformazione';
COMMENT ON COLUMN ctmp.trasformazioni.tipo_trasf IS 'Codice del tipo di trasformazione';
COMMENT ON COLUMN ctmp.trasformazioni.punti_contr IS 'Punti di controllo usati per creare la matrice di trasformazione';
COMMENT ON COLUMN ctmp.trasformazioni.matrice_trasf IS 'Matrice di trasformazione';
