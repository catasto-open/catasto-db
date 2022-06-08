import os
from invoke import task
from pathlib import Path


@task
def lint(ctx):
    ctx.run("sqlfluff lint ./sql --config ./sql/.sqlfluff")
    ctx.run("flake8")
    ctx.run("black --check .")


@task
def check_database(ctx):
    ctx.run("alembic current")


@task
def init_database(ctx):
    ctx.run("alembic revision -m 'init catasto-db'")


@task
def migrate_database(ctx):
    ctx.run("alembic upgrade head")


@task
def show_database_history(ctx):
    ctx.run("alembic history")


@task(optional=['start', 'stop', 'clean', 'logs'])
def docker_compose_postgis(
    ctx, 
    start=False,
    stop=False,
    clean=False,
    logs=False
):
    base_path = Path(__file__).resolve()
    docker_compose_path = base_path.parent / "scripts" / "docker" / "postgis"
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
