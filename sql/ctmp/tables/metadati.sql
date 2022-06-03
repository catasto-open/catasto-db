INSERT INTO ctmp.fabbricati
(comune, sezione, foglio, allegato, sviluppo, numero, t_altezza, t_angolo, t_pt_ins, t_ln_anc, geom)
VALUES('', '', '', '', '', '', 0, 0, ?, ?, ?);
-- ctmp.metadati definition

-- Drop table

-- DROP TABLE ctmp.metadati;

CREATE TABLE ctmp.metadati (
    id serial4 NOT NULL, -- Identificativo univoco della tabella
    tipo_mappa varchar(100) NOT NULL, -- Tipo di mappa, valori: MAPPA, MAPPA FONDIARIO, QUADRO D'UNIONE
    nome_mappa varchar(11) NOT NULL, -- Nome della mappa, coincide con il nome del file CXF
    scala varchar(12) NOT NULL, -- Fattore di scala della mappa cartacea originaria
    data_gen varchar(10) NOT NULL, -- Data di generazione del file SUP
    n_fabbric varchar(10) NULL, -- Numero totale di fabbricati
    n_partic varchar(10) NULL, -- Numero totale di particelle
    n_strade varchar(10) NULL, -- Numero totale di strade
    n_acque varchar(10) NULL, -- Numero totale di acque
    n_svil_all varchar(10) NULL, -- Numero totale di buchi relativi a sviluppi e allegati
    fabbric varchar(10) NULL, -- Area totale di tutti i fabbricati
    partic varchar(10) NULL, -- Area totale di tutte le particelle
    strade varchar(10) NULL, -- Area totale di tutte le strade
    acque varchar(10) NULL, -- Area totale di tutte le acque
    svil_all varchar(10) NULL, -- Area totale di tutti i buchi relativi a sviluppi e allegati
    totale varchar(10) NULL, -- Area somma delle aree di particelle, strade, acque, sviluppi e allegati
    confine varchar(10) NULL, -- Area totale del confine della mappa
    sbilancio varchar(10) NULL, -- Differenza tra totale e il confine
    data_elab timestamp NOT NULL, -- Data di eleborazione della mappa
    CONSTRAINT metadati_pkey PRIMARY KEY (id)
);
CREATE INDEX metadati_i1 ON ctmp.metadati USING btree(nome_mappa, data_elab);
COMMENT ON TABLE ctmp.metadati IS 'Dati riferiti alle importazioni dai file CXF e dai file SUP';

-- Column comments

COMMENT ON COLUMN ctmp.metadati.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp.metadati.tipo_mappa IS 'Tipo di mappa, valori: MAPPA, MAPPA FONDIARIO, QUADRO D''UNIONE';
COMMENT ON COLUMN ctmp.metadati.nome_mappa IS 'Nome della mappa, coincide con il nome del file CXF';
COMMENT ON COLUMN ctmp.metadati.scala IS 'Fattore di scala della mappa cartacea originaria';
COMMENT ON COLUMN ctmp.metadati.data_gen IS 'Data di generazione del file SUP';
COMMENT ON COLUMN ctmp.metadati.n_fabbric IS 'Numero totale di fabbricati';
COMMENT ON COLUMN ctmp.metadati.n_partic IS 'Numero totale di particelle';
COMMENT ON COLUMN ctmp.metadati.n_strade IS 'Numero totale di strade';
COMMENT ON COLUMN ctmp.metadati.n_acque IS 'Numero totale di acque';
COMMENT ON COLUMN ctmp.metadati.n_svil_all IS 'Numero totale di buchi relativi a sviluppi e allegati';
COMMENT ON COLUMN ctmp.metadati.fabbric IS 'Area totale di tutti i fabbricati';
COMMENT ON COLUMN ctmp.metadati.partic IS 'Area totale di tutte le particelle';
COMMENT ON COLUMN ctmp.metadati.strade IS 'Area totale di tutte le strade';
COMMENT ON COLUMN ctmp.metadati.acque IS 'Area totale di tutte le acque';
COMMENT ON COLUMN ctmp.metadati.svil_all IS 'Area totale di tutti i buchi relativi a sviluppi e allegati';
COMMENT ON COLUMN ctmp.metadati.totale IS 'Area somma delle aree di particelle, strade, acque, sviluppi e allegati';
COMMENT ON COLUMN ctmp.metadati.confine IS 'Area totale del confine della mappa';
COMMENT ON COLUMN ctmp.metadati.sbilancio IS 'Differenza tra totale e il confine';
COMMENT ON COLUMN ctmp.metadati.data_elab IS 'Data di eleborazione della mappa';
