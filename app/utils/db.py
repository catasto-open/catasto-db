import sqlalchemy as db
from sqlalchemy import inspect


class DataAccessLayer:
    connection = None
    engine = None
    conn_string = None
    metadata = db.MetaData()
    inspector = None

    def db_init(self, conn_string):
        self.engine = db.create_engine(conn_string or self.conn_string)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData(bind=self.connection)
        self.inspector = inspect(self.engine)

    def get_table(self, table_name, schema):
        return db.Table(
            table_name,
            self.metadata,
            autoload=True,
            autoload_with=self.engine,
            schema=schema,
        )

    def get_schema_names(self):
        return self.inspector.get_schema_names()

    def get_table_names(self, schema):
        return self.inspector.get_table_names(schema)


dal = DataAccessLayer()
