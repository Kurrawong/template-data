# Data repo structure

- background/ - for background ontologies
- data/
    - folder per id
        - resources/ folder for resources (for catalogs)
            - folder per resource id
                - `<resource_id>.ttl`
                - scores/ folder for scores per resource (for catalogs)
                    - `<resource_id>-<score_name>.ttl` per score type
        - scripts/ folder for etl
            - `<id>-etl.py` for the top-level etl script to be run
        - source/ folder for raw source data
        - `<id>-metadata.ttl` for dataset to be used in ETL
        - `<id>.nq` for generated N-quads file from ETL
        - `<id>.ttl` for non-datasets
- draft-data/ folder for unpublished/unfinished data not to be uploaded
- scripts/ - for scripts
    - `validate.py` for running validation
    - `upload.py` for uploading data
    - `etl.sh` for ETL generation
- system/ - for profiles, validators, etc.
    - profiles/ folder for profiles - to be used for upload
    - validator/ folder for validators


```
<project_root>/
├── .github/
│   └── workflows/
│       ├── upload.yaml
│       └── validate.yaml
├── background/
│   └── <ontology_id>.ttl
├── data/
│   └── <id>/
│       ├── resources/ # for catalogs
│       │   └── <resource_id>/
│       │       ├── <resource_id>.ttl
│       │       └── scores/ # for catalogs
│       │           └── <resource_id>-<score_name>.ttl # e.g. care, fair, idg
│       ├── scripts/
│       │   └── <id>-etl.py
│       ├── source/
│       ├── <id>-metadata.ttl # for dataset etl
│       ├── <id>.nq # gitignored, for dataset etl
│       └── <id>.ttl # for non-datasets
├── draft-data/
│   └── <draft_id>/
├── scripts/
│   ├── upload.py
│   ├── utils.py
│   └── validate.py
├── system/
│   ├── profiles/
│   └── validators/
├── .gitignore
├── LICENSE
├── README.md
├── poetry.lock
└── pyproject.toml
```
