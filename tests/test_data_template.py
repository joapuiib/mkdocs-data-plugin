import re

from mkdocs.commands.build import build
from mkdocs.config.base import load_config


def test_dir_source_in_markdown_file():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        plugins={
            "macros": {},
            "data": {'sources': {'data': 'tests/data'}},
        },
    )

    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]

    with open(site_dir+'/test_dir_source/index.html') as f:
        data_loaded = re.findall(r"<code>([^<]*)", f.read())
        print(data_loaded)
        assert(data_loaded == [
            "{'a1': 1, 'a2': 'text'}", # data/a.yml
            "1", # data/a.yml -> a1
            "text", # data/a.yml -> a2
            "2", # data/dir1/b.yml -> b1
            "text", # data/dir1/b.yml -> b2
            "3", # data/dir2/c.yml -> c1
            "text", # data/dir2/c.yml -> c2
        ])

def test_file_source_in_markdown_file():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        plugins={
            "macros": {},
            "data": {'sources': {'fruits': 'tests/docs/fruits.yml'}},
        },
    )

    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]

    with open(site_dir+'/test_file_source/index.html') as f:
        data_loaded = re.findall(r"<code>([^<]*)", f.read())
        print(data_loaded)
        assert(data_loaded == [
            "Apple",
            "Banana",
            "Strawberry",
        ])

