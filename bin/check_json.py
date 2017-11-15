#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:  check_json.py schema jsonfile

"""

import click
import jsonschema
import re
import gzip
import json
import yaml
from typing import Tuple, List, Mapping, Any


def validate_to_schema(data, schema: Mapping[str, Any]) -> Tuple[bool, List[Tuple[str, str]]]:
    """Validate datafile against jsonschema

    Args:
        data: datafile to validate
        schema (Mapping[str, Any]): schema

    Returns:
        Tuple[bool, List[str]]:
            bool: Is valid?  Yes = True, No = False
            List[Tuple[str, str]]: Validation issues, empty if valid, tuple is ('Error|Warning', msg)
                e.g. [('ERROR', "'subject' is a required property")]
    """

    v = jsonschema.Draft4Validator(schema)
    messages = []
    errors = sorted(v.iter_errors(data), key=lambda e: e.path)
    for error in errors:
        for suberror in sorted(error.context, key=lambda e: e.schema_path):
            print(list(suberror.schema_path), suberror.message, '\n\n', sep=", ")
            messages.append(('ERROR', suberror.message))

    is_valid = True
    if errors:
        is_valid = False

    return (is_valid, messages)


@click.command()
@click.argument('schemafn')
@click.argument('fn')
def check_file(schemafn: str, fn: str) -> List[str]:
    """Check that file conforms to JSON schema

    Args:
        schemafn (str): schema filename (either yaml or json)
        fn (str): filename to test (json, yaml - possibly gzipped)

    Returns:
        List[str]: error messages
    """

    if re.search('gz$', fn):
        if 'yaml' in fn:
            with gzip.open(fn, 'r') as f:
                data = yaml.load(f)
        elif 'json' in fn:
            with gzip.open(fn, 'r') as f:
                data = json.load(f)
        else:
            print('Do not know how to load file: ', fn)
    else:
        if 'yaml' in fn:
            with open(fn, 'r') as f:
                data = yaml.load(f)
        elif 'json' in fn:
            with open(fn, 'r') as f:
                data = json.load(f)
        else:
            print('Do not know how to load file: ', fn)

    if 'yaml' in schemafn:
        with open(schemafn, 'r') as f:
            schema = yaml.load(f)
    elif 'json' in schemafn:
        with open(schemafn, 'r') as f:
            schema = json.load(f)
    else:
        print('Do not know how to load schema: ', schemafn)

    (is_valid, messages) = validate_to_schema(data, schema)

    if is_valid:
        print('File is valid according to JSON Schema')

    else:
        print(messages)


def main():
    check_file()


if __name__ == '__main__':
    main()

