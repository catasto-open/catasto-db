"""added ctis schema

Revision ID: 0457a2bbc011
Revises: f7c7baa76adf
Create Date: 2022-12-05 16:45:30.668608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0457a2bbc011'
down_revision = 'f7c7baa76adf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("create schema ctis")
    op.execute("""CREATE TABLE ctis.import_job_log (
        id bigserial NOT NULL,
        job_type varchar(256) NOT NULL,
        running bool NOT NULL DEFAULT true,
        status bool NOT NULL DEFAULT false,
        error text NULL,
        start_date timestamptz NULL DEFAULT now(),
        end_date timestamptz NULL,
        created_date timestamptz NULL DEFAULT now(),
        modified_date timestamptz NULL DEFAULT now(),
        CONSTRAINT import_job_log_pkey PRIMARY KEY (id)
    )""")
    op.execute("""CREATE INDEX import_job_log_status_idx ON ctis.import_job_log USING btree (status)""")
    op.execute("""CREATE TABLE ctis.import_log (
        id bigserial NOT NULL,
        file_source_path text NULL,
        file_store_active bool NOT NULL DEFAULT false,
        file_store_path text NULL,
        file_sha256_checksum varchar(64) NULL,
        file_name varchar(256) NULL,
        file_date varchar(11) NULL,
        tematismo varchar(256) NULL,
        iscrizione varchar(256) NULL,
        status bool NOT NULL DEFAULT false,
        db_import_status bool NOT NULL DEFAULT false,
        file_store_status bool NOT NULL DEFAULT false,
        error text NULL,
        import_job_log_id bigserial NOT NULL,
        created_date timestamptz NULL DEFAULT now(),
        modified_date timestamptz NULL DEFAULT now(),
        CONSTRAINT import_log_file_sha256_checksum_key UNIQUE (file_sha256_checksum),
        CONSTRAINT import_log_file_source_path_key UNIQUE (file_source_path),
        CONSTRAINT import_log_pkey PRIMARY KEY (id)
        )""")
    op.execute("""CREATE INDEX import_log_file_date_idx ON ctis.import_log USING btree (file_date);""")
    op.execute("""CREATE INDEX import_log_file_metadata_idx ON ctis.import_log USING btree (tematismo, iscrizione, file_name, file_date);""")
    op.execute("""CREATE INDEX import_log_import_job_log_id_idx ON ctis.import_log USING btree (import_job_log_id)""")
    op.execute("""CREATE INDEX import_log_status_idx ON ctis.import_log USING btree (status)""")
    op.execute("""CREATE INDEX import_log_tem_status_idx ON ctis.import_log USING btree (tematismo, status)""")
    op.execute("""CREATE TABLE ctis.error_insert_fab (
	    id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	    "data" text NULL,
	    CONSTRAINT error_insert_fab_pkey PRIMARY KEY (id))""")

def downgrade() -> None:
    op.execute("drop schema ctis")
    op.drop_table("import_job_log", schema="ctis")
    op.drop_index(
        "import_job_log_status_idx",
        table_name="import_job_log",
        schema="ctis",
        postgresql_using="gist",
    )
    op.drop_table("import_log", schema="ctis")
    op.drop_index(
        "import_log_file_date_idx",
        table_name="import_job",
        schema="ctis",
        postgresql_using="gist",
    )
    op.drop_index(
        "import_log_file_metadata_idx",
        table_name="import_job",
        schema="ctis",
        postgresql_using="gist",
    )
    op.drop_index(
        "import_log_import_job_log_id_idx",
        table_name="import_job",
        schema="ctis",
        postgresql_using="gist",
    )
    op.drop_index(
        "import_log_status_idx",
        table_name="import_job",
        schema="ctis",
        postgresql_using="gist",
    )
    op.drop_index(
        "import_log_tem_status_idx",
        table_name="import_job",
        schema="ctis",
        postgresql_using="gist",
    )
    op.drop_table("error_insert_fab", schema="ctis")




