-- ctmp.message_log definition

-- Drop table

-- DROP TABLE ctmp.message_log;

CREATE TABLE ctmp.message_log (
	id serial4 NOT NULL, -- identificativo univoco del messaggio
	log_time timestamp NULL DEFAULT now(), -- data e ora del messaggio
	message text NULL, -- messaggio
	CONSTRAINT message_log_pkey PRIMARY KEY (id)
);
CREATE INDEX message_log_idx1 ON ctmp.message_log USING btree (log_time);
CREATE INDEX message_log_idx2 ON ctmp.message_log USING btree (message);
COMMENT ON TABLE ctmp.message_log IS 'messaggi ed errori di tutte le procedure';

-- Column comments

COMMENT ON COLUMN ctmp.message_log.id IS 'identificativo univoco del messaggio';
COMMENT ON COLUMN ctmp.message_log.log_time IS 'data e ora del messaggio';
COMMENT ON COLUMN ctmp.message_log.message IS 'messaggio';