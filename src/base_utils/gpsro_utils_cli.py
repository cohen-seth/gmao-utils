
import logging
import os
import sys

import click

import gpsro_utils #obs_inv_utils
import config_handlers
from base_utils import sinv

@click.group()
def cli():
    """Cli for gpsro_utils."""

@cli.command()
#@click.option('-c', '--config-yaml', 'config_yaml', required=True, type=str)
@click.option('-f', '--bufr-file', 'bufr', required=True, type=str)
def sinv(bufr):
    return sinv_base(bufr)

