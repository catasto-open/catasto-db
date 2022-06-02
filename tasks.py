from invoke import task


@task
def lint(ctx):
    ctx.run("sqlfluff lint ./sql --config ./sql/.sqlfluff")
    ctx.run("flake8")
    ctx.run("black --check .")
