# Catasto-db/Geoserver for development

## How to use

### Configuring the development environment
Run the following command:

```shell
 ENV_STATE=dev
```

### Start PostGIS/Geoserver

Run the following command:

```shell
poetry run inv catasto-open --start
```

### Check PostGIS/Geoserver containers

Run the following command:

```shell
poetry run inv catasto-open
```

### Stop PostGIS/Geoserver

Run the following command:

```shell
poetry run inv catasto-open --stop
```

### Check the PostGIS/Geoserver logs

Run the following command:

```shell
poetry run inv catasto-open --logs
```

### Configure the database and geoserver

Run the following command:

```shell
poetry run inv catasto-open --setup
```

### Load Catasto Open data

Run the following command:

```shell
poetry run inv catasto-open --loadfixtures
```

### Reset Catasto Open data

Run the following command:

```shell
poetry run inv catasto-open --clean
```
