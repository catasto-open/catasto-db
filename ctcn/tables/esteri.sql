-- ctcn.esteri definition

-- Drop table

-- DROP TABLE ctcn.esteri;

CREATE TABLE ctcn.esteri (
	codice varchar(4) NOT NULL,
	sigla varchar(4) NULL,
	denominaz varchar(65) NOT NULL,
	CONSTRAINT esteri_pkey PRIMARY KEY (codice)
);