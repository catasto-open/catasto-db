-- ctcn.cutipnot definition

-- Drop table

-- DROP TABLE ctcn.cutipnot;

CREATE TABLE ctcn.cutipnot (
	tipo_nota varchar(1) NOT NULL,
	descrizion varchar(35) NOT NULL,
	CONSTRAINT cutipnot_pkey PRIMARY KEY (tipo_nota)
);