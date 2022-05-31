-- ctmp.punti_controllo definition

-- Drop table

-- DROP TABLE ctmp.punti_controllo;

CREATE TABLE ctmp.punti_controllo (
	comune varchar(4) NOT NULL, -- Codice catastale del Comune
	sezione varchar(1) NOT NULL, -- Codice sezione censuaria
	foglio varchar(4) NOT NULL, -- Codice identificativo del foglio
	numero varchar(9) NULL, -- Codice identificativo della particella
	n_gruppo int4 NOT NULL, -- Numero ordinale del gruppo di punti
	n_punto int4 NOT NULL, -- Numero ordinale del punto di controllo
	pt_orig geometry NOT NULL, -- Geometria del punto di origine
	pt_dest geometry NOT NULL, -- Geometria del punto di destinazione
	CONSTRAINT punti_controllo_pkey PRIMARY KEY (comune, sezione, foglio, n_gruppo, n_punto)
);
CREATE INDEX punti_controllo_si1 ON ctmp.punti_controllo USING gist (pt_orig);
CREATE INDEX punti_controllo_si2 ON ctmp.punti_controllo USING gist (pt_dest);
COMMENT ON TABLE ctmp.punti_controllo IS 'Punti di controllo per la trasformazione geometrica delle mappe';

-- Column comments

COMMENT ON COLUMN ctmp.punti_controllo.comune IS 'Codice catastale del Comune';
COMMENT ON COLUMN ctmp.punti_controllo.sezione IS 'Codice sezione censuaria';
COMMENT ON COLUMN ctmp.punti_controllo.foglio IS 'Codice identificativo del foglio';
COMMENT ON COLUMN ctmp.punti_controllo.numero IS 'Codice identificativo della particella';
COMMENT ON COLUMN ctmp.punti_controllo.n_gruppo IS 'Numero ordinale del gruppo di punti';
COMMENT ON COLUMN ctmp.punti_controllo.n_punto IS 'Numero ordinale del punto di controllo';
COMMENT ON COLUMN ctmp.punti_controllo.pt_orig IS 'Geometria del punto di origine';
COMMENT ON COLUMN ctmp.punti_controllo.pt_dest IS 'Geometria del punto di destinazione';