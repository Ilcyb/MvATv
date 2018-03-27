import argparse

from mvatv.core.controller import executor
from mvatv.core.commands import commands
from mvatv.core.mvatv import MVATV
from mvatv.plugin.data_sources import ZIMUZU

def main():
    load_plugins()

    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers(dest='command')

    for command in commands:
        temp_sub_parser = sub_parser.add_parser(command['action'], help=command.get('help', ''))
        for arg in command.get('arguments', []):
            temp_sub_parser.add_argument(arg['dest'], **arg['kwargs'])

    action = parser.parse_args()
    executor(action)

def load_plugins():
    MVATV.plugging(ZIMUZU())