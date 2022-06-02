-- ctcn.cuptaspe definition

-- Drop table

-- DROP TABLE ctcn.cuptaspe;

CREATE TABLE ctcn.cuptaspe (
    partita varchar(1) NOT NULL,
    descrizion varchar(100) NOT NULL,
    CONSTRAINT cuptaspe_pkey PRIMARY KEY (partita)
);
