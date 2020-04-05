from core.management import cli
from core import settings
import click

@cli.command()
@click.option('-a', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=5000)
@click.option('-d', '--debug', default=False)
def run(port, host, debug):
    import uvicorn
    settings.DEBUG = debug
    uvicorn.run('app:app', host=host, port=port, reload=debug)


@cli.command()
def upgrade():
    from alembic.config import Config
    from alembic import command
    alembic_cfg = Config(f"{settings.BASE_DIR}/alembic.ini")
    command.upgrade(alembic_cfg, "head")


if __name__ == '__main__':
    cli()
