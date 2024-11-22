# Configuration

This plugin provides the following configuration options.

## Data Directory
The `data_dir` option specifies the directory where data files are stored. By default, this is set to `data`.

```yaml
plugins:
  - data:
      data_dir: data
```

!!! tip
    It is recommended to configure the `watch` option in the `mkdocs.yml` file
    to automatically reload the site when data files are modified.

    ```yaml
    watch:
      - data
    ```
