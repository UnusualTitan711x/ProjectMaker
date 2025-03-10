import click
import subprocess

from .commands import create_godot, create_unity, create_web

@click.group()
def cli():
    """ProjectMaker CLI Tool"""
    pass

cli.add_command(create_web)
cli.add_command(create_godot)
cli.add_command(create_unity)

if __name__ == "__main__":
    cli()