from mkdocs.commands.build import build
from mkdocs.config.base import load_config


def test_inexistent_source_is_skipped():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        plugins={
            "data": {'sources': {'data': 'tests/inexistent'}}
        },
    )

    build(mkdocs_config)

    dataPlugin = mkdocs_config["plugins"]["data"]

    assert "data" not in dataPlugin.sources


def test_folder_source():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        plugins={
            "data": {'sources': {'data': 'tests/data'}}
        },
    )

    build(mkdocs_config)

    dataPlugin = mkdocs_config["plugins"]["data"]
    data = dataPlugin.sources["data"]

    assert data == {
            "a": {
                "number": 1,
                "string": "text",
            },
            "dir1": {
                "number": 1,
                "string": "text",
                "b": {
                    "number": 2,
                    "string": "text",
                },
            },
            "dir2": {
                "c": {
                    "number": 3,
                    "string": "text",
                },
            },
    }

def test_folder_source_slash():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        plugins={
            "data": {'sources': {'data': 'tests/data/'}}
        },
    )

    build(mkdocs_config)

    dataPlugin = mkdocs_config["plugins"]["data"]
    data = dataPlugin.sources["data"]

    assert data == {
            "a": {
                "number": 1,
                "string": "text",
            },
            "dir1": {
                "number": 1,
                "string": "text",
                "b": {
                    "number": 2,
                    "string": "text",
                },
            },
            "dir2": {
                "c": {
                    "number": 3,
                    "string": "text",
                },
            },
    }

def test_file_source():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        plugins={
            "data": {'sources': {'fruits': 'tests/docs/fruits.yml'}}
        },
    )

    build(mkdocs_config)

    dataPlugin = mkdocs_config["plugins"]["data"]
    data = dataPlugin.sources["fruits"]
    print(dataPlugin.sources)

    assert data == ['Apple', 'Banana', 'Strawberry']
