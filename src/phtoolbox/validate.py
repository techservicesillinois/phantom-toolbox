"""
Validate app.tar files before deployment to SOAR.

This module provides functionality to validate the contents of
app.tar files, specifically checking that app.json contains valid
data with no empty top-level values.
"""

import json
import sys
import tarfile

from os.path import basename
from typing import Any, Dict, List


def validate_app_json(app_json: Dict[str, Any]) -> List[str]:
    """
    Validate that app.json has no empty top-level values.

    Args:
        app_json_data: The parsed JSON data from app.json

    Returns:
        List of validation error messages. Empty list means validation passed.
    """
    errors = []

    for key, value in app_json.items():
        if value is None or value == "" or \
           (isinstance(value, (list, dict)) and len(value) == 0):
            errors.append(f"Top-level key '{key}' has an empty value")

    return errors


def untar_app_json(tar_path: str) -> Dict[str, Any]:
    """
    Extract app.json from tar_path.

    Args:
        tar_path: A path to a tar file containing an app.json file.

    Returns:
        A dictionary containing the JSON contents of app.json.
    """
    try:
        # Look for app.json in the tar file
        with tarfile.open(tar_path, 'r') as tar:
            app_json_members = [member for member in tar.getmembers()
                                if basename(member.name) == 'app.json']

            if not app_json_members:
                raise Exception("Error: No app.json found in {tar_path}")
            if len(app_json_members) > 1:
                raise Exception(
                    f"Error: Multiple app.json files found in {tar_path}"
                )

            app_json_file = tar.extractfile(app_json_members[0])
            if app_json_file is None:
                raise Exception(
                    f"Error: Could not extract app.json from {tar_path}"
                )
            return json.loads(app_json_file.read().decode('utf-8'))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise Exception(f"Error: Invalid JSON in app.json: {e}")
    except tarfile.TarError as e:
        raise Exception(f"Error: Invalid tar file {tar_path}: {e}")
    except FileNotFoundError:
        raise Exception(f"Error: File not found: {tar_path}")
    except Exception as e:
        raise Exception(
            f"Error: Unexpected error validating {tar_path}: {e}"
        )


def validate(args) -> int:
    """
    CLI entry point for the validate command.

    Args:
        args: Parsed command line arguments

    Returns:
        Exit code: 0 for success, 1 for validation failure
    """
    try:
        app_json = untar_app_json(args.file.name)
    except Exception as e:
        print(e, file=sys.stderr)
        return 1

    # Validate the JSON data
    validation_errors = validate_app_json(app_json)

    if validation_errors:
        print("Validation failed:", file=sys.stderr)
        for error in validation_errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(f"✓ Validation passed: {args.file.name}")
    return 0
