#!/usr/bin/python
""" Entrypoint for running dclone with commands
"""

import src.click.cli as click_cli

if __name__ == '__main':
    click_cli.cli()