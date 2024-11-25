# mkdocs-data-plugin
__MkDocs Data Plugin__ is a plugin for [MkDocs](https://www.mkdocs.org/) that allows
reading data from markup files and use it in your Markdown pages.

Currently supported formats:

- JSON: `.json`
- YAML: `.yml`, `.yaml`

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
  - macros
  - data
```

## Overview
When using this plugin, you can define data in YAML or JSON files
in a separate directory and reference them in your Markdown files.

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
