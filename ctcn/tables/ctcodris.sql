-- ctcn.ctcodris definition

-- Drop table

-- DROP TABLE ctcn.ctcodris;

CREATE TABLE ctcn.ctcodris (
	codice varchar(1) NOT NULL,
	descrizion varchar(50) NOT NULL,
	CONSTRAINT ctcodris_pkey PRIMARY KEY (codice)
);