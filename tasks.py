from invoke import task


@task
def lint(ctx):
    ctx.run("sqlfluff lint . --dialect postgres")
    ctx.run("flake8")
    ctx.run("black --check .")
