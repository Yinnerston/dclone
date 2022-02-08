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
    print("Click Group Init")

## TODO: ADD ARGS AND OPTIONS

@cli.command(help='Run a process in a container')
@click.option('--image-name', '-i', help='Image name', default='ubuntu')
@click.option('--image-dir', help='Images directory',
              default='/images')
@click.option('--container-dir', help='Containers directory',
              default='/containers')
@click.argument('Command', required=True, nargs=-1)
def run(image_name, image_dir, container_dir, command):
    return RunCommand(image_name, image_dir, container_dir, command)

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