# Installation
This plugin can be installed via `pip`:

```bash
pip install mkdocs-data-plugin
```

## Configuration
To use the plugin, add the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - macros
  - data
```

## Requirements
Aside from Python and MkDocs, the plugin has the following dependencies:

- [`mkdocs-macros-plugin`][macros-plugin]: Needed to provide the `data` variable in pages.

    [macros-plugin]: https://mkdocs-macros-plugin.readthedocs.io/en/latest/
