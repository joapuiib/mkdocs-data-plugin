import os
import yaml
import json


from mkdocs.config.defaults import MkDocsConfig
from mkdocs.config import base, config_options as c
from mkdocs.plugins import BasePlugin, get_plugin_logger

log = get_plugin_logger(__name__)

class DataPluginConfig(base.Config):
    data_dir = c.Type(str, default='data')


class DataPlugin(BasePlugin[DataPluginConfig]):
    def __init__(self):
        self.data = {}
        self.processors = {
            '.yml': yaml.safe_load,
            '.yaml': yaml.safe_load,
            '.json': json.load
        }


    def set_data(self, keys, value):
        """
        Set a value in the data attribute.
        """
        data = self.data
        for key in keys[:-1]:
            data = data.setdefault(key, {})
        data[keys[-1]] = value


    def on_config(self, config: MkDocsConfig):
        self.load_data(self.config.data_dir)

        macros_plugin = config.plugins.get('macros')
        if macros_plugin:
            macros_plugin.register_variables({'data': self.data})
        else:
            log.warning("The macros plugin is not installed. The `data` variable won't be available in pages.")


    def load_data(self, path: str):
        """
        Iterate over all files in the data directory
        and load them into the data attribute.
        """
        for root, _, files in os.walk(path):

            keys = []
            if root != self.config.data_dir:
                directory = os.path.relpath(root, self.config.data_dir)
                keys = directory.split(os.sep)

            for file in files:
                value = self.load_file(os.path.join(root, file))

                filename, _ = os.path.splitext(file)
                self.set_data(keys + [filename], value)


    def load_file(self, path: str):
        """
        Load a file and return its content.
        """
        _, extension = os.path.splitext(path)
        with open(path, 'r') as file:
            return self.processors[extension](file)



    def on_page_context(self, context, page, config, nav):
        context['data'] = self.data
        return context

