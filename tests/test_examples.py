#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:  program.py <customer>

"""

import jsonschema
from jsonschema import validate
from jsonschema.exceptions import ValidationError

import pytest
import yaml
import glob
import re
import os

# get the current path name
cur_path = os.path.dirname(os.path.realpath(__file__))
home_path = cur_path.replace('/tests', '')


def test_examples():
    """Check that schemas are valid"""

    examples = glob.glob(f'{home_path}/examples/*.yaml')

    for fn in examples:
        print('Example fn: ', fn)
        basename = os.path.basename(fn)

        with open(fn, 'r') as f:
            example = yaml.load(f)

        schema_basename = re.sub('\-.*?\-', '-', basename)
        schema_fn = f'{home_path}/schemas/{schema_basename}'

        with open(schema_fn, 'r') as f:
            schema = yaml.load(f)

        v = jsonschema.Draft4Validator(schema)
        errors = sorted(v.iter_errors(example), key=lambda e: e.path)
        for error in errors:
            for suberror in sorted(error.context, key=lambda e: e.schema_path):
                print(list(suberror.schema_path), suberror.message, sep=", ")

        if errors:
            assert False

        # except Exception as e:
        #     print('Problem with example: ', fn)
        #     print(e)


def test_instances():

    test_instances = glob.glob(f'{home_path}/tests/test_instances/*.yaml')

    for fn in test_instances:

        basename = os.path.basename(fn)
        print('Fn', fn)

        with open(fn, 'r') as f:
            test_instance = yaml.load(f)

        schema_basename = re.sub('\-.*?\-', '-', basename)
        schema_fn = f'{home_path}/schemas/{schema_basename}'

        with open(schema_fn, 'r') as f:
            schema = yaml.load(f)

        good_flag = False  # whether test instance should succeed or fail
        if re.search('-good.*?-', fn):
            good_flag = True

        if good_flag:
            v = jsonschema.Draft4Validator(schema)
            errors = sorted(v.iter_errors(test_instance), key=lambda e: e.path)

            for error in errors:
                for suberror in sorted(error.context, key=lambda e: e.schema_path):
                    print(list(suberror.schema_path), suberror.message, sep=", ")

            if errors:
                assert False

            # try:
            #     validate(test_instance, schema)
            # except Exception as e:
            #     assert False
            #     print('Problem with test instance: ', fn, ' against schema: ', schema_fn)
            #     print(e)

        else:
            with pytest.raises(ValidationError, message='Expecting JSONschema validation error') as e:
                validate(test_instance, schema)
                print(e.value)


def main():

    test_examples()
    quit()


    import json
    import pprint

    with open('../examples/nanopub_bel-example-0.9.0.yaml', 'r') as f:
        example = yaml.load(f)

    # with open('../schemas/test.json', 'r') as f:
    #     schema = json.load(f)

    with open('../schemas/test2.yaml', 'r') as f:
        schema = yaml.load(f)

    v = jsonschema.Draft4Validator(schema)
    errors = sorted(v.iter_errors(example), key=lambda e: e.path)
    for error in errors:
        for suberror in sorted(error.context, key=lambda e: e.schema_path):
            print(list(suberror.schema_path), suberror.message, sep=", ")

    # validate(example, schema)


if __name__ == '__main__':
    main()

