import click

from .commands import create_godot, create_unity, create_web, create_nodejs

@click.group()
def cli():
    """ProjectMaker: CLI Tool for creating project templates"""
    pass

cli.add_command(create_web)
cli.add_command(create_godot)
cli.add_command(create_unity)
cli.add_command(create_nodejs)

if __name__ == "__main__":
    cli()