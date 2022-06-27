-- ctcn.message_log definition

-- Drop table

-- DROP TABLE ctcn.message_log;

CREATE TABLE ctcn.message_log (
    id serial4 NOT NULL, -- identificativo univoco del messaggio
    log_time timestamp NULL DEFAULT now(), -- data e ora del messaggio
    message text NULL, -- messaggio
    CONSTRAINT message_log_pkey PRIMARY KEY (id)
);
CREATE INDEX message_log_idx1 ON ctcn.message_log USING btree(log_time);
CREATE INDEX message_log_idx2 ON ctcn.message_log USING btree(message);
COMMENT ON TABLE ctcn.message_log IS 'messaggi e errori di tutte le procedure';

-- Column comments

COMMENT ON COLUMN ctcn.message_log.id IS 'identificativo univoco del messaggio';
COMMENT ON COLUMN ctcn.message_log.log_time IS 'data e ora del messaggio';
COMMENT ON COLUMN ctcn.message_log.message IS 'messaggio';
