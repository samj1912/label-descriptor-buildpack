import libcnb
import toml

def detector(context: libcnb.DetectContext) -> libcnb.DetectResult:
    project_descriptor = context.application_dir / "project.toml"
    result = libcnb.DetectResult()
    if project_descriptor.exists():
        project_content = toml.load(project_descriptor)
        try:
            project_content["io"]["buildpacks"]["labels"]
        except (KeyError, TypeError) as e:
            pass
        else:
            result.passed = True
    return result


def builder(context: libcnb.BuildContext) -> libcnb.BuildResult:
    print("Running Label Descriptor Buildpack")
    project_descriptor = context.application_dir / "project.toml"
    result = libcnb.BuildResult()
    labels = toml.load(project_descriptor)["io"]["buildpacks"]["labels"]
    print(f"Detected {len(labels)} labels")
    result_labels = result.launch_metadata.labels
    for label in labels:
        result_labels.append(libcnb.Label.parse_obj(label))
        print(f"Added label: {result_labels[-1]}")
    return result


if __name__ == "__main__":
    libcnb.run(detector=detector, builder=builder)
