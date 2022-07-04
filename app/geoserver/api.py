import json

import requests
from requests.auth import HTTPBasicAuth
import logging
from app.configs import cnf

logging.basicConfig(level=logging.INFO)


def create_workspace(workspace):
    response = requests.post(
        f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
        f"/geoserver/rest/workspaces/",
        auth=HTTPBasicAuth(username="admin", password="geoserver"),
        json=workspace,
    )
    logging.info(
        f"Loading Geoserver {cnf.CATASTO_OPEN_GS_WORKSPACE} workspace..."
    )
    logging.info(f"{response.text}: status code {response.status_code}")


def create_datastore(datastore):
    try:
        response = requests.post(
            f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/rest/workspaces/"
            f"CatastoOpenDev/datastores/",
            auth=HTTPBasicAuth(username="admin", password="geoserver"),
            json=datastore,
        )
        logging.info(
            f"Loading Geoserver {cnf.CATASTO_OPEN_GS_DATASTORE} datastore..."
        )
        logging.info(f"{response.text}: status code {response.status_code}")
    except Exception as e:
        logging.error(e)


def create_layer(layer):
    try:
        response = requests.post(
            f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/rest"
            f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
            f"/datastores/{cnf.CATASTO_OPEN_GS_DATASTORE}"
            f"/featuretypes",
            auth=HTTPBasicAuth(username="admin", password="geoserver"),
            json=layer,
        )
        logging.info(f"Loading {layer['featureType']['name']} layer...")
        logging.info(
            f"{response.text}: " f"status code {response.status_code}"
        )
    except Exception as e:
        logging.error(e)


def get_settings():
    response = requests.get(
        f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
        f"/geoserver/rest/settings/",
        auth=HTTPBasicAuth(username="admin", password="geoserver"),
    )
    settings = json.loads(response.text)
    return settings


def update_settings(settings):
    try:
        response = requests.put(
            f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/rest/settings/",
            auth=HTTPBasicAuth(username="admin", password="geoserver"),
            json=settings,
        )
        logging.info("Updating Geoserver settings...")
        logging.info(
            f"{response.text}: " f"status code {response.status_code}"
        )
    except Exception as e:
        logging.error(e)
