# mkdocs-data-plugin
MkDocs plugin that allows to read data from external markup files.

Currently supported formats:

- JSON
- YAML

## Documentation
This plugin documentation can be found here: https://joapuiib.github.io/mkdocs-data-plugin/

## Installation
This plugin can be installed via pip:

```bash
pip install mkdocs-data-plugin
```

## Configuration
Activate the plugin in your `mkdocs.yml`:

```yaml
plugins:
  - data
```

## Overview
When using this plugin, you can define data in YAML or JSON files
in a separate directory and reference it in your Markdown files.

```txt
root/
├── docs/
│   └── ...
├── data/
│   └── fruits.yml
└── mkdocs.yml
```

```yaml title="fruits.yml"
- Apple
- Banana
- Strawberry
```

Files in this directory can be referenced in your Markdown files using the `data` variable.

```markdown
{% for fruit in data.fruits -%}
- {{ fruit }}
{% endfor %}
```