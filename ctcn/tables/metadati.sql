-- ctcn.metadati definition

-- Drop table

-- DROP TABLE ctcn.metadati;

CREATE TABLE ctcn.metadati (
    estrazione varchar(20) NULL, -- Nome del file della fornitura
    comune varchar(4) NULL, -- Comune richiesto
    sezione varchar(4) NULL, -- Sezione del comune richiesto
    data_rich varchar(10) NULL, -- Data della richista
    data_elab varchar(10) NULL, -- Data di elaborazione della fornitura
    tipo_estr varchar(100) NULL, -- Tipologia di estrazione della richiesta
    -- Data di riferimento per la selezione (solo per attualita)
    data_selez varchar(10) NULL,
    date_reg varchar(50) NULL, -- Data iniziale e finale intervallo (solo se aggiornamenti per data di registrazione)
    numero_rec varchar(20) NULL -- Numero di record estratti
);
CREATE INDEX metadati_idx1 ON ctcn.metadati USING btree(comune, sezione);
COMMENT ON TABLE ctcn.metadati IS 'Dati riferiti alle importazioni eseguite';

-- Column comments

COMMENT ON COLUMN ctcn.metadati.estrazione IS 'Nome del file della fornitura';
COMMENT ON COLUMN ctcn.metadati.comune IS 'Comune richiesto';
COMMENT ON COLUMN ctcn.metadati.sezione IS 'Sezione del comune richiesto';
COMMENT ON COLUMN ctcn.metadati.data_rich IS 'Data della richista';
COMMENT ON COLUMN ctcn.metadati.data_elab IS 'Data di elaborazione della fornitura';
COMMENT ON COLUMN ctcn.metadati.tipo_estr IS 'Tipologia di estrazione della richiesta';
COMMENT ON COLUMN ctcn.metadati.data_selez IS 'Data di riferimento per la selezione (solo per attualita)';
COMMENT ON COLUMN ctcn.metadati.date_reg IS 'Data iniziale e finale intervallo (solo se aggiornamenti per data di registrazione)';
COMMENT ON COLUMN ctcn.metadati.numero_rec IS 'Numero di record estratti';
