from mkdocs.config.base import load_config

from mkdocs_data_plugin.plugin import DataPlugin


def test_config_default_values():
    plugin = DataPlugin()
    plugin.load_config({})
    assert plugin.config.sources == {'data': 'data'}


def test_config_sources():
    plugin = DataPlugin()
    plugin.load_config({'sources': {'data': 'other_data'}})
    assert plugin.config.sources == {'data': 'other_data'}
