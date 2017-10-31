#!/usr/bin/env bash

# Check if in top-level directory for schemas

if [ !  -e "schemas/nanopub_bel-0.9.0.yaml" ]; then
    echo "Not in schemas repo top-level directory - this command has"
    echo "  to be run in schemas top-level directory"
    exit
fi

cd schemas
mkdir -p json
for f in *.yaml
do
    newfn=${f/yaml/json}
    yaml2json $f "./json/${newfn}"
    echo "Creating ${newfn}"
done
