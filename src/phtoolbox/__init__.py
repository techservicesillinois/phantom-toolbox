#!/usr/bin/python
"""
example:
phantom deploy app.tar
phantom deploy --token TOKEN --hostname example.com app.tar
phantom deps -i src/app.json -o dist/app.json wheels
"""

import argparse
import json
import os
import sys

from .deploy import deploy
from .deps import deps


def directory(path):
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"{path}: not a valid directory.")
    return path


def json_file(path):
    if path == "-":
        return json.load(sys.stdin)
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"{path}: not a valid file.")
    try:
        with open(path, 'r') as f:
            r = json.load(f)
    except Exception as e:
        raise argparse.ArgumentTypeError(f"{path}: not a valid JSON file: {e}")
    return r


def init_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prog="phantom"
    )
    subparsers = parser.add_subparsers(
    )

    deploy = subparsers.add_parser(
        'deploy',
        help="Deploy Splunk SOAR apps",
    )
    deploy.set_defaults(func=_deploy)
    deploy.add_argument(
        "file",
        metavar="FILE",
        type=argparse.FileType('rb'),
        help="Tar file to deploy")
    deploy.add_argument(
        "-t",
        "--token",
        type=str,
        help="Phantom api auth token",
        required=False)
    deploy.add_argument(
        "-H",
        "--hostname",
        type=str,
        help="Phantom hostname",
        required=False)
    dependencies = subparsers.add_parser(
        'dependencies',
        aliases=['deps'],
        help="Add wheel dependencies to SOAR metadata file",
    )
    dependencies.set_defaults(func=deps)
    dependencies.add_argument(
        "dir",
        metavar="DIR",
        type=str,
        nargs=1,
        help="A directory containing only wheels",
    )
    dependencies.add_argument(
        "-C",
        "--change-directory",
        metavar="DIR",
        nargs='?',
        type=directory,
        help=(
            "Change to this directory before running. "
            "Wheel paths will be relative to this directory."
        ),
    )
    dependencies.add_argument(
        "-i",
        "--input-file",
        nargs='?',
        type=json_file,
        default="-",
        help="Input SOAR app metadata file",
    )
    dependencies.add_argument(
        "-o",
        "--output-file",
        nargs='?',
        type=argparse.FileType('w'),
        help="Output SOAR app metadata file",
    )
    return parser


def _deploy(args):
    if not args.token:
        args.token = os.environ['SOAR_TOKEN']

    if not args.hostname:
        args.hostname = os.environ['SOAR_HOSTNAME']

    return deploy(args)


def _main(parser, args):
    if hasattr(args, 'func'):
        return args.func(args)
    else:
        parser.print_help(sys.stderr)
        return 1


def main():
    parser = init_parser()
    args = parser.parse_args()
    sys.exit(_main(parser, args))
