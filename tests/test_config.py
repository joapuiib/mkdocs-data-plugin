from mkdocs.config.base import load_config

from mkdocs_data_plugin.plugin import DataPlugin


def test_config_default_values():
    plugin = DataPlugin()
    plugin.load_config({})
    assert plugin.config.mappings == {'data': 'data'}


def test_config_mappings():
    plugin = DataPlugin()
    plugin.load_config({'mappings': {'data': 'other_data'}})
    assert plugin.config.mappings == {'data': 'other_data'}
