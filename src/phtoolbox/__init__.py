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

from app.deploy import deploy


def init_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'command',
        type=str,
        nargs="1",
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
    return parser.parse_args()


def _main(user_args=None):
    args = init_parser()

    if not args.token:
        args.token = os.environ['SOAR_TOKEN']

    if not args.hostname:
        args.hostname = os.environ['SOAR_HOSTNAME']
    
    return_code = 1
    if args.command == 'deploy':
       return_code = deploy(args)

    sys.exit(return_code)


if __name__ == "__main__":
    _main()
