CREATE INDEX ctfisica_i3 ON ctcn.ctfisica USING btree (((((cognome)::text || ' '::text) || (nome)::text)) varchar_pattern_ops);
