-- ctcn.ctptaspe definition

-- Drop table

-- DROP TABLE ctcn.ctptaspe;

CREATE TABLE ctcn.ctptaspe (
    partita varchar(1) NOT NULL,
    descrizion varchar(100) NOT NULL,
    CONSTRAINT ctptaspe_pkey PRIMARY KEY (partita)
);
