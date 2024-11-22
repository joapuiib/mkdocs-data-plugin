import re

from mkdocs.commands.build import build
from mkdocs.config.base import load_config


def test_loads_files():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        plugins={
            "macros": {},
            "data": {'data_dir': 'tests/data'},
        },
    )

    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]

    with open(site_dir+'/test_data_template/index.html') as f:
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

