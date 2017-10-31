#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:  program.py <customer>

"""

import sys
from jsonschema import Draft4Validator
import yaml
import glob

# if len(sys.argv) > 1:
#     fn = sys.argv[1]
# else:
#     print('No filename to check')
#     quit()

schemas = glob.glob('../schemas/*.yaml')


def test_check_schemas():
    """Check that schemas are valid"""

    for fn in schemas:
        with open(fn, 'r') as f:
            schema = yaml.load(f)
        try:
            result = Draft4Validator.check_schema(schema)
            assert result is None
            print('Valid schema: ', fn)
        except Exception as e:
            print('Problem with schema: ', fn)
            print(e)
            assert False


def main():
    check_schemas()


if __name__ == '__main__':
    main()

