-- ctmp_a.metadati definition

-- Drop table

-- DROP TABLE ctmp_a.metadati;

CREATE TABLE ctmp_a.metadati (
    id int4 NOT NULL, -- Identificativo univoco della tabella
    -- Tipo di mappa, valori: MAPPA, MAPPA FONDIARIO, QUADRO D'UNIONE
    tipo_mappa varchar(100) NOT NULL,
    -- Nome della mappa, coincide con il nome del file CXF
    nome_mappa varchar(11) NOT NULL,
    -- Fattore di scala della mappa cartacea originaria
    scala varchar(12) NOT NULL,
    data_gen varchar(10) NOT NULL, -- Data di generazione del file SUP
    n_fabbric varchar(10) NULL, -- Numero totale di fabbricati
    n_partic varchar(10) NULL, -- Numero totale di particelle
    n_strade varchar(10) NULL, -- Numero totale di strade
    n_acque varchar(10) NULL, -- Numero totale di acque
    -- Numero totale di buchi relativi a sviluppi e allegati
    n_svil_all varchar(10) NULL,
    fabbric varchar(10) NULL, -- Area totale di tutti i fabbricati
    partic varchar(10) NULL, -- Area totale di tutte le particelle
    strade varchar(10) NULL, -- Area totale di tutte le strade
    acque varchar(10) NULL, -- Area totale di tutte le acque
    -- Area totale di tutti i buchi relativi a sviluppi e allegati
    svil_all varchar(10) NULL,
    -- Area somma delle aree di particelle, strade, acque, sviluppi e allegati
    totale varchar(10) NULL,
    confine varchar(10) NULL, -- Area totale del confine della mappa
    sbilancio varchar(10) NULL, -- Differenza tra totale e il confine
    data_elab timestamp NOT NULL, -- Data di eleborazione della mappa
    stato int4 NOT NULL, -- Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione
    data_crea timestamp NOT NULL, -- Data di creazione del record
    CONSTRAINT metadati_pkey PRIMARY KEY (id, stato)
);
CREATE INDEX metadati_i1 ON ctmp_a.metadati USING btree(nome_mappa, data_elab);
COMMENT ON TABLE ctmp_a.metadati IS 'Dati riferiti alle importazioni dai file CXF e dai file SUP';

-- Column comments

COMMENT ON COLUMN ctmp_a.metadati.id IS 'Identificativo univoco della tabella';
COMMENT ON COLUMN ctmp_a.metadati.tipo_mappa IS 'Tipo di mappa, valori: MAPPA, MAPPA FONDIARIO, QUADRO D''UNIONE';
COMMENT ON COLUMN ctmp_a.metadati.nome_mappa IS 'Nome della mappa, coincide con il nome del file CXF';
COMMENT ON COLUMN ctmp_a.metadati.scala IS 'Fattore di scala della mappa cartacea originaria';
COMMENT ON COLUMN ctmp_a.metadati.data_gen IS 'Data di generazione del file SUP';
COMMENT ON COLUMN ctmp_a.metadati.n_fabbric IS 'Numero totale di fabbricati';
COMMENT ON COLUMN ctmp_a.metadati.n_partic IS 'Numero totale di particelle';
COMMENT ON COLUMN ctmp_a.metadati.n_strade IS 'Numero totale di strade';
COMMENT ON COLUMN ctmp_a.metadati.n_acque IS 'Numero totale di acque';
COMMENT ON COLUMN ctmp_a.metadati.n_svil_all IS 'Numero totale di buchi relativi a sviluppi e allegati';
COMMENT ON COLUMN ctmp_a.metadati.fabbric IS 'Area totale di tutti i fabbricati';
COMMENT ON COLUMN ctmp_a.metadati.partic IS 'Area totale di tutte le particelle';
COMMENT ON COLUMN ctmp_a.metadati.strade IS 'Area totale di tutte le strade';
COMMENT ON COLUMN ctmp_a.metadati.acque IS 'Area totale di tutte le acque';
COMMENT ON COLUMN ctmp_a.metadati.svil_all IS 'Area totale di tutti i buchi relativi a sviluppi e allegati';
COMMENT ON COLUMN ctmp_a.metadati.totale IS 'Area somma delle aree di particelle, strade, acque, sviluppi e allegati';
COMMENT ON COLUMN ctmp_a.metadati.confine IS 'Area totale del confine della mappa';
COMMENT ON COLUMN ctmp_a.metadati.sbilancio IS 'Differenza tra totale e il confine';
COMMENT ON COLUMN ctmp_a.metadati.data_elab IS 'Data di eleborazione della mappa';
COMMENT ON COLUMN ctmp_a.metadati.stato IS 'Stato del record, valori: 1, 2; 1 per record modificato in seguito ad una trasformazione, 2 per record cancellato in seguito ad una nuova importazione';
COMMENT ON COLUMN ctmp_a.metadati.data_crea IS 'Data di creazione del record';
