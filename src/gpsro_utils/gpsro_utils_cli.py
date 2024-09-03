
import logging
import os
import sys

import click

import gpsro_utils #obs_inv_utils
import config_handlers

@click.group()
def cli():
    """Cli for gpsro_utils."""

@cli.command()
#@click.option('-c', '--config-yaml', 'config_yaml', required=True, type=str)
@click.option('-f', '--bufr-file', required=True, type=str)
def get_obs_inventory(config_yaml):
    return get_obs_inventory_base(config_yaml)

