#!/usr/bin/env python
"""
Validate app.tar files before deployment to SOAR.

This module provides functionality to validate the contents of app.tar files,
specifically checking that app.json contains valid data with no empty top-level values.
"""

import json
import sys
import tarfile
from pathlib import Path
from typing import Dict, Any, List


def validate_app_json(app_json_data: Dict[str, Any]) -> List[str]:
    """
    Validate that app.json has no empty top-level values.
    
    Args:
        app_json_data: The parsed JSON data from app.json
        
    Returns:
        List of validation error messages. Empty list means validation passed.
    """
    errors = []
    
    for key, value in app_json_data.items():
        if value is None or value == "" or (isinstance(value, (list, dict)) and len(value) == 0):
            errors.append(f"Top-level key '{key}' has an empty value")
    
    return errors


def extract_and_validate_app_json(tar_path: str) -> int:
    """
    Extract app.json from app.tar and validate its contents.
    
    Args:
        tar_path: Path to the app.tar file
        
    Returns:
        Exit code: 0 for success, 1 for validation failure
    """
    try:
        with tarfile.open(tar_path, 'r') as tar:
            # Look for app.json in the tar file, excluding resource fork files
            app_json_members = [member for member in tar.getmembers() 
                              if member.name.endswith('app.json') and not member.name.startswith('._')]
            
            if not app_json_members:
                print(f"Error: No app.json found in {tar_path}", file=sys.stderr)
                return 1
            
            # Use the first app.json found (there should typically be only one)
            app_json_member = app_json_members[0]
            
            # Extract and parse the JSON
            app_json_file = tar.extractfile(app_json_member)
            if app_json_file is None:
                print(f"Error: Could not extract app.json from {tar_path}", file=sys.stderr)
                return 1
            
            try:
                content = app_json_file.read()
                # Try different encodings
                for encoding in ['utf-8', 'latin-1', 'cp1252']:
                    try:
                        decoded_content = content.decode(encoding)
                        app_json_data = json.loads(decoded_content)
                        break
                    except (UnicodeDecodeError, json.JSONDecodeError):
                        continue
                else:
                    print("Error: Could not decode app.json with any supported encoding", file=sys.stderr)
                    return 1
            except json.JSONDecodeError as e:
                print(f"Error: Invalid JSON in app.json: {e}", file=sys.stderr)
                return 1
            
            # Validate the JSON data
            validation_errors = validate_app_json(app_json_data)
            
            if validation_errors:
                print("Validation failed:", file=sys.stderr)
                for error in validation_errors:
                    print(f"  - {error}", file=sys.stderr)
                return 1
            
            print(f"✓ Validation passed: {tar_path}")
            return 0
            
    except tarfile.TarError as e:
        print(f"Error: Invalid tar file {tar_path}: {e}", file=sys.stderr)
        return 1
    except FileNotFoundError:
        print(f"Error: File not found: {tar_path}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: Unexpected error validating {tar_path}: {e}", file=sys.stderr)
        return 1


def validate(args) -> int:
    """
    CLI entry point for the validate command.
    
    Args:
        args: Parsed command line arguments
        
    Returns:
        Exit code: 0 for success, 1 for validation failure
    """
    return extract_and_validate_app_json(args.file.name)
