---
title: Home
---
# MkDocs Data Plugin

__MkDocs Data Plugin__ is a plugin for [MkDocs](https://www.mkdocs.org/) that allows
reading data from markup files and use it in your Markdown pages.

## Overview
When using this plugin, you can define data in YAML or JSON files
in a separate directory and reference them in your Markdown pages.

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
{% raw %}
{% for fruit in data.fruits -%}
- {{ fruit }}
{% endfor %}
{% endraw %}
```
/// html | div.result
{% for fruit in data.fruits -%}
- {{ fruit }}
{% endfor %}
///

## Supported Formats
The plugin supports the following file formats:

- JSON: `.json`
- YAML: `.yml`, `.yaml`
