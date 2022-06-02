-- ctmp.tipo_trasformazioni definition

-- Drop table

-- DROP TABLE ctmp.tipo_trasformazioni;

CREATE TABLE ctmp.tipo_trasformazioni (
    codice varchar(20) NOT NULL, -- Codice del tipo di trasformazione
    -- Descrizione del tipo di trasformazione
    descrizione varchar(1000) NOT NULL,
    CONSTRAINT tipo_trasformazioni_pkey PRIMARY KEY (codice)
);
COMMENT ON TABLE ctmp.tipo_trasformazioni IS 'Tipologie di trasformazioni geometriche';

-- Column comments

COMMENT ON COLUMN ctmp.tipo_trasformazioni.codice IS 'Codice del tipo di trasformazione';
COMMENT ON COLUMN ctmp.tipo_trasformazioni.descrizione IS 'Descrizione del tipo di trasformazione';
