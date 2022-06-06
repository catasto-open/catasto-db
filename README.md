# Catasto-db

## development

### How to use PostGIS

There is a docker-compose script in the following directory `scripts/docker/postgis` that make the development easier.
There is a `README.md` file in the same directory which explains the commands to run from the root of the repository. Please be careful about the requirement to have **docker-compose** installed.

### Check the database config_ini_section

Run the following command:

```shell
poetry run inv check-database
```

If the database is ready and the connection is established then you will receive the following output:

```shell
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
```

### Initialize the database

```shell
poetry run inv init-database
```
