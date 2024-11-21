from mkdocs.commands.build import build
from mkdocs.config.base import load_config


def test_empty_data_is_empty_dict():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        plugins={
            "data": {'data_dir': 'tests/inexistent'}
        },
    )

    build(mkdocs_config)

    dataPlugin = mkdocs_config["plugins"]["data"]
    data = dataPlugin.data

    assert data == {}


def test_loads_files():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        plugins={
            "data": {'data_dir': 'tests/data'}
        },
    )

    build(mkdocs_config)

    dataPlugin = mkdocs_config["plugins"]["data"]
    data = dataPlugin.data

    assert data == {
            "a": {
                "a1": 1,
                "a2": "text",
            },
            "dir1": {
                "b": {
                    "b1": 2,
                    "b2": "text",
                },
            },
            "dir2": {
                "c": {
                    "c1": 3,
                    "c2": "text",
                },
            },
    }
