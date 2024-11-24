from mkdocs.commands.build import build
from mkdocs.config.base import load_config


def test_inexistent_mapping_is_skipped():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        plugins={
            "data": {'mappings': {'data': 'tests/inexistent'}}
        },
    )

    build(mkdocs_config)

    dataPlugin = mkdocs_config["plugins"]["data"]

    assert "data" not in dataPlugin.mappings


def test_folder_mapping():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        plugins={
            "data": {'mappings': {'data': 'tests/data'}}
        },
    )

    build(mkdocs_config)

    dataPlugin = mkdocs_config["plugins"]["data"]
    data = dataPlugin.mappings["data"]

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
