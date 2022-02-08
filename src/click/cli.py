""" Click cli interface calling Command objects

Returns:
    [type]: [description]
"""

import click
from ..commands.run import RunCommand
from ..commands.build import BuildCommand
from ..commands.image import ImageCommand
from ..commands.start import StartCommand
from ..commands.stop import StopCommand


@click.group()
def cli():
    """Click group
    """
    pass

## TODO: ADD ARGS AND OPTIONS

@cli.command()
def run():
    return RunCommand()

@cli.command()
def build():
    return BuildCommand()

@cli.command()
def image():
    return ImageCommand()

@cli.command()
def start():
    return StartCommand()

@cli.command()
def stop():
    return StopCommand()