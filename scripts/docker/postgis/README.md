# Catasto-db database for development

## How to use

### Start PostGIS

Run the following command:

```shell
poetry run inv docker-compose-postgis --start
```

### Check PostGIS container

Run the following command:

```shell
poetry run inv docker-compose-postgis
```

### Stop PostGIS

Run the following command:

```shell
poetry run inv docker-compose-postgis --stop
```

### Check the PostGIS log

Run the following command:

```shell
poetry run inv docker-compose-postgis --logs
```

### Check PostGIS database availability

Run the following command:

```shell
poetry run inv docker-compose-postgis --isready
```

### Reset PostGIS data

Run the following command:

```shell
poetry run inv docker-compose-postgis --logs
```
