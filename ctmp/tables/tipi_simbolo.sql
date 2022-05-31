-- ctmp.tipo_simbolo definition

-- Drop table

-- DROP TABLE ctmp.tipo_simbolo;

CREATE TABLE ctmp.tipo_simbolo (
	codice int4 NOT NULL, -- Codice del tipo di simobolo
	descrizione varchar(100) NULL, -- Descrizione del tipo di simobolo
	CONSTRAINT tipo_simbolo_pkey PRIMARY KEY (codice)
);
COMMENT ON TABLE ctmp.tipo_simbolo IS 'Descrizioni dei tipi di simobolo';

-- Column comments

COMMENT ON COLUMN ctmp.tipo_simbolo.codice IS 'Codice del tipo di simobolo';
COMMENT ON COLUMN ctmp.tipo_simbolo.descrizione IS 'Descrizione del tipo di simobolo';