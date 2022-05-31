-- ctcn.cuutilit definition

-- Drop table

-- DROP TABLE ctcn.cuutilit;

CREATE TABLE ctcn.cuutilit (
	codice varchar(4) NOT NULL,
	sezione varchar(1) NOT NULL,
	immobile int8 NOT NULL,
	tipo_imm varchar(1) NOT NULL,
	progressiv int4 NOT NULL,
	sez_urbana varchar(3) NULL,
	foglio varchar(4) NULL,
	numero varchar(5) NULL,
	denominato int4 NULL,
	subalterno varchar(4) NULL
);
CREATE INDEX cuutilit_idx1 ON ctcn.cuutilit USING btree (codice, sezione, immobile, tipo_imm, progressiv);