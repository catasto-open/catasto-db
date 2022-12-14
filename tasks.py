import os
import time
from invoke import task

# from invoke.exceptions import UnexpectedExit
from pathlib import Path

from app.configs import cnf
from app.geoserver.fixtures import (
    load_workspaces,
    load_data_stores,
    load_layers,
    load_settings,
    refresh_layers
)
from app.tests.app import TestApp


@task(optional=["ci"])
def lint(ctx, ci=False):
    ctx.run("sqlfluff lint ./sql --config ./sql/.sqlfluff")
    flake8_cmd = "flake8 --exclude ./alembic/versions"
    if ci:
        flake8_cmd = f"{flake8_cmd},./.venv/*"
    ctx.run(f"{flake8_cmd}")
    ctx.run("black --check .")


@task
def check_database(ctx):
    ctx.run("alembic current")


@task
def test_catasto_open(ctx):
    ctx.run("python -m unittest -v app/tests/app.py")


@task
def init_database(ctx):
    ctx.run("alembic revision -m 'init catasto-db'")


@task
def migrate_database(ctx):
    ctx.run("alembic upgrade head")


@task
def load_database_fixtures(ctx):
    test_app = TestApp()
    test_app.setUpClass()


@task
def clean_database(ctx):
    test_app = TestApp()
    test_app.clean_database()


@task
def show_database_history(ctx):
    ctx.run("alembic history")


@task(optional=["ci"])
def wait_for_database(ctx, ci=False):
    base_path = Path(__file__).resolve()
    docker_compose_path = base_path.parent / "scripts" / "docker" / "postgis"
    database_env_setup()
    with ctx.cd(os.fspath(docker_compose_path)):
        cmd = "docker compose"
        if ci:
            cmd = f"{cmd} -f docker-compose-ci.yml"
        ready = ctx.run(
            f"{cmd} exec -T db pg_isready -d {cnf.POSTGRES_DB}"  # ,
            # asynchronous=True
        )
        while not ready:
            time.sleep(1)


@task(optional=["start", "stop", "clean", "logs", "isready", "ci"])
def docker_compose_postgis(
    ctx,
    start=False,
    stop=False,
    clean=False,
    logs=False,
    isready=False,
    ci=False,
):
    base_path = Path(__file__).resolve()
    docker_compose_path = base_path.parent / "scripts" / "docker" / "postgis"
    database_env_setup()
    with ctx.cd(os.fspath(docker_compose_path)):
        cmd = "docker compose"
        if ci:
            cmd = "docker compose -f docker-compose-ci.yml"
        if start:
            cmd = f"{cmd} up -d"
        elif stop:
            cmd = f"{cmd} stop"
        elif logs:
            cmd = f"{cmd} logs -f"
        elif clean:
            cmd = f"{cmd} down -v --remove-orphans"
        elif isready:
            cmd = f"{cmd} exec db pg_isready -d {cnf.POSTGRES_DB}"
        else:
            cmd = f"{cmd} ps -a"
        ctx.run(f"{cmd}")


@task(
    optional=[
        "start",
        "setup",
        "loadfixtures",
        "stop",
        "clean",
        "logs",
        "dbclean",
        "refresh"
    ]
)  # noqa
def catasto_open(
    ctx,
    start=False,
    setup=False,
    loadfixtures=False,
    stop=False,
    clean=False,
    logs=False,
    dbclean=False,
    refresh=False
):
    base_path = Path(__file__).resolve()
    docker_compose_path = base_path.parent / "scripts" / "docker"
    database_env_setup()
    geoserver_env_setup()
    if setup:
        migrate_database(ctx)
        geoserver_setup()
        return
    elif loadfixtures:
        load_database_fixtures(ctx)
        return
    elif dbclean:
        clean_database(ctx)
        return
    elif refresh:
        refresh_layers()
    with ctx.cd(os.fspath(docker_compose_path)):
        cmd = "docker compose"
        if start:
            cmd = f"{cmd} up -d"
        elif stop:
            cmd = f"{cmd} stop"
        elif logs:
            cmd = f"{cmd} logs -f"
        elif clean:
            cmd = f"{cmd} down -v --remove-orphans"
        else:
            cmd = f"{cmd} ps -a"
        ctx.run(f"{cmd}")


def geoserver_setup():
    load_workspaces()
    load_data_stores()
    load_layers()
    load_settings()


def database_env_setup():
    os.environ["POSTGIS_VERSION_TAG"] = cnf.APP_CONFIG.POSTGIS_VERSION_TAG
    os.environ["POSTGRES_DB"] = cnf.POSTGRES_DB
    os.environ["POSTGRES_USER"] = cnf.POSTGRES_USER
    os.environ["POSTGRES_PASS"] = cnf.POSTGRES_PASS
    os.environ["POSTGRES_HOST"] = cnf.POSTGRES_HOST
    os.environ["POSTGRES_HOST_PORT"] = str(cnf.POSTGRES_HOST_PORT)
    os.environ["POSTGRES_CONTAINER_PORT"] = str(cnf.POSTGRES_CONTAINER_PORT)


def geoserver_env_setup():
    os.environ["GS_VERSION"] = cnf.APP_CONFIG.GS_VERSION
    os.environ["GEOSERVER_HOST_PORT"] = cnf.GEOSERVER_HOST_PORT
    os.environ["GEOSERVER_CONTAINER_PORT"] = cnf.GEOSERVER_CONTAINER_PORT
    os.environ["GEOSERVER_DATA_DIR"] = cnf.GEOSERVER_DATA_DIR
    os.environ["GEOSERVER_ADMIN_USER"] = cnf.GEOSERVER_ADMIN_USER
    os.environ["GEOSERVER_ADMIN_PASSWORD"] = cnf.GEOSERVER_ADMIN_PASSWORD
    os.environ["GEOWEBCACHE_CACHE_DIR"] = cnf.GEOWEBCACHE_CACHE_DIR
    os.environ["INITIAL_MEMORY"] = cnf.INITIAL_MEMORY
    os.environ["MAXIMUM_MEMORY"] = cnf.MAXIMUM_MEMORY
