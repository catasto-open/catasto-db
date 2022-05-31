-- ctcn.cucodcat definition

-- Drop table

-- DROP TABLE ctcn.cucodcat;

CREATE TABLE ctcn.cucodcat (
	categoria varchar(3) NOT NULL,
	descrizion varchar(200) NOT NULL,
	CONSTRAINT cucodcat_pkey PRIMARY KEY (categoria)
);