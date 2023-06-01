#!/usr/bin/python
"""
description:
Helps deploy Splunk SOAR apps

example:
phantom deploy --file app.tar
phantom deploy --file app.tar --token TOKEN --hostname example.com
"""

import argparse
import os
import sys

from .deploy import deploy


def init_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prog="phantom"
    )
    parser.add_argument(
        'command',
        type=str,
        nargs=1,
        help='Command to execute')
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="Tar file to deploy",
        required=True)
    parser.add_argument(
        "-t",
        "--token",
        type=str,
        help="Phantom api auth token",
        required=False)
    parser.add_argument(
        "-H",
        "--hostname",
        type=str,
        help="Phantom hostname",
        required=False)
    return parser


def _main(user_args=None):

    if not user_args.token:
        user_args.token = os.environ['SOAR_TOKEN']

    if not user_args.hostname:
        user_args.hostname = os.environ['SOAR_HOSTNAME']

    return_code = 1
    if user_args.command == 'deploy':
        return_code = deploy(user_args)

    sys.exit(return_code)


def main():
    args = init_parser().parse_args()
    _main(user_args=args)
