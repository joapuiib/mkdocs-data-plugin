from mkdocs.config.base import load_config

from mkdocs_data_plugin.plugin import DataPlugin


def test_config_default_values():
    plugin = DataPlugin()
    plugin.load_config({})
    assert plugin.config.data_dir == 'data'


def test_config_data_dir():
    plugin = DataPlugin()
    plugin.load_config({'data_dir': 'other_data'})
    assert plugin.config.data_dir == 'other_data'
