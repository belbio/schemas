# Example naming convention

The test instance names have to conform to the schema name and version in the
schemas directory.  You can add a label indicating a specific type of example
by including it after the first dash in the name.

    nanopub_bel-<LABEL>-0.9.0.yaml

The first dash and label will be removed to determine which schema (including version)
to check it against.

Good example LABELs that should pass validation start with -good...-  Bad example LABELs
start with -bad...-

Example names:

    nanopub_bel-0.9.0.yaml  # no example label

    nanopub_bel-good_citation_db-0.9.0.yaml # label of 'good' test
