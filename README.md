# Schemas

The schemas used by BELBio for important data objects are managed here. The schemas
are in JSONSchema format, but the original and editable versions are stored in YAML
format to allow for additional comments and easier reading of the data objects.

The data object schemas are for:

* nanopubs
* edges
* terminologies
* orthologies
* taxonomy

Tooling is also available including a tool to convert the YAML formats to JSON. 

## Descriptions

Many of the following schemas will support JSONLines (jsonlines.org) format to 
allow streaming of the dataset so one doesn't have to load all of the JSON file
before processing.  One can load each sub-object, e.g. a term at at time in the
terminology schema which for some terminologies with a few million entries can
make an enormous different in memory usage.

### Nanopubs

The nanopub schema is for capturing curated knowledge or assertions as a triple
(subject, relation, object or SRO). The triple (or array of triples) have 
a citation indicating from where the triple was sourced, context such as for
BEL Nanopubs what tissue, disease context, cell line, species, etc the triples
are associated with. Miscellaneous metadata is also captured for the triple.

### Edges 

The objects imported/exported to/from the EdgeStore are in this format defined
by the edge schema.

### Terminologies

Terms for the BEL Namespaces are loaded from datafiles in this format

### Orthologies

Orthology data for BEL is loaded from datafiles in this format

### Taxonomy

Taxonomy data is loaded into BEL from datafiles in this format.