import json
import os

import yaml
from mkdocs.config import base
from mkdocs.config import config_options as c
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin, get_plugin_logger

log = get_plugin_logger(__name__)


class DataPluginConfig(base.Config):
    mappings = c.Type(dict, default={'data': 'data'})


class DataPlugin(BasePlugin[DataPluginConfig]):
    def __init__(self):
        self.mappings = {}
        self.processors = {'.yml': yaml.safe_load, '.yaml': yaml.safe_load, '.json': json.load}

    def load_mappings(self):
        """
        Load all mappings from the config file and load the data from the files.
        """
        for mapping, path in self.config['mappings'].items():
            if not os.path.exists(path):
                log.warning(f"Mapping path '{path}' not found. Skipping.")
            elif os.path.isdir(path):
                self.load_folder(mapping, path)
            else:
                value = self.load_file(path)
                self.update_data(mapping, [], value)

    def update_data(self, mapping: str, keys: list, value: any):
        """
        Update the mappings data with the given value.
        """
        if len(keys) == 0:
            self.mappings[mapping] = value
        else:
            data = self.mappings.setdefault(mapping, {})
            for key in keys[:-1]:
                data = data.setdefault(key, {})
            data[keys[-1]] = value

    def load_folder(self, mapping: str, path: str):
        """
        Iterate over all files in the data directory
        and load them into the data attribute.
        """
        for root, _, files in os.walk(path):

            keys = []
            if root != path:
                directory = os.path.relpath(root, path)
                keys = directory.split(os.sep)

            for file in files:
                value = self.load_file(os.path.join(root, file))

                filename, _ = os.path.splitext(file)
                self.update_data(mapping, keys + [filename], value)

    def load_file(self, path: str):
        """
        Loads a file and processes it with the appropriate processor.
        """
        _, extension = os.path.splitext(path)
        with open(path, 'r') as file:
            return self.processors[extension](file)

    def on_config(self, config: MkDocsConfig):
        self.load_mappings()

        macros_plugin = config.plugins.get('macros')
        if macros_plugin:
            for mapping, data in self.mappings.items():
                macros_plugin.register_variables({mapping: data})
        else:
            log.warning(
                "The macros plugin is not installed. The `data` variable won't be available in pages."
            )

    def on_page_context(self, context, page, config, nav):
        for mapping, data in self.mappings.items():
            context[mapping] = data
        return context
