import argparse

from mvatv.core.controller import executor
from mvatv.core.commands import commands

def main():
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers(dest='command')

    for command in commands:
        temp_sub_parser = sub_parser.add_subparsers(command['action'], help=command.get('help', ''))
        for arg in command.get('arguments', []):
            temp_sub_parser.add_argument(arg['dest'], **arg['kwargs'])

    action = parser.parse_args()
    executor(action)