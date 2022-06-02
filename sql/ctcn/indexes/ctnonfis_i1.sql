CREATE INDEX ctnonfis_i1 ON ctcn.ctnonfis USING btree(
    denominaz varchar_pattern_ops
);
