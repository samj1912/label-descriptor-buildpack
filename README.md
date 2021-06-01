# Proc Descriptor Buildpack

![Version](https://img.shields.io/badge/dynamic/json?url=https://cnb-registry-api.herokuapp.com/api/v1/buildpacks/sam/label-descriptor&label=Version&query=$.latest.version)

This is a [Cloud Native Buildpack](https://buildpacks.io) that configures image labels using a [project descriptor](https://github.com/buildpacks/spec/blob/main/extensions/project-descriptor.md#project-descriptor) file - `project.toml`

## Usage

The buildpack automatically generates labels on the output image when you run a build:

```bash
pack build --buildpack sam/label-descriptor myapp
```

You can customize the generated labels by creating a `project.toml` file in your application, and a table like:

```toml
[[io.buildpacks.labels]]
key = "<label-name>"
value = "<label-value>"

```

The keys in the `io.buildpacks.labels` table map directly to [the keys described here.](https://github.com/buildpacks/spec/blob/main/buildpack.md#launchtoml-toml)

## Example

For example create a `project.toml` file with the following content - 

```
[[io.buildpacks.labels]]
key = "label-name"
value = "hello world"


[[io.buildpacks.labels]]
key = "another-label-name"
value = "hello universe"
```

Then run - 

```bash
pack build --buildpack sam/label-descriptor myapp
docker inspect myapp --format '{{ index .Config.Labels "label-name" }}'
```

