# Example naming convention

The Example names have to conform to the schema name and version in the
schemas directory.  You can add a label indicating a specific type of example
by including it after the first dash in the name.

    nanopub_bel-<LABEL>-0.9.0.yaml

The first dash and label will be removed to determine which schema (including version)
to check it against.

Example names:

    nanopub_bel-0.9.0.yaml  # no example label

    nanopub_bel-test-0.9.0.yaml # label of 'test'
