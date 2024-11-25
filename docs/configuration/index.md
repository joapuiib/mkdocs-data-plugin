# Configuration

This plugin provides the following configuration options.

## Data Sources
The `sources` option is a dictionary that defines the data sources to be used.
Each key-value pair represents a source name and its corresponding directory path.

A source can reference directories or files.
If a directory is specified, all files in the directory and its subdirectories will be loaded.

By default, a single data source named `data` is defined with the directory path `data`.

```yaml
plugins:
  - sources:
      data: data # default
      foo: docs/foo.yml
```

!!! tip
    It is recommended to configure the `watch` option in the `mkdocs.yml` file
    to automatically reload the site when files in the data sources outside
    the `docs` directory are modified.

    ```yaml
    watch:
      - data
    ```
