-- ctcn.comuni definition

-- Drop table

-- DROP TABLE ctcn.comuni;

CREATE TABLE ctcn.comuni (
	provincia varchar(2) NOT NULL,
	comune varchar(65) NOT NULL,
	codice varchar(5) NOT NULL,
	CONSTRAINT comuni_pkey PRIMARY KEY (codice)
);