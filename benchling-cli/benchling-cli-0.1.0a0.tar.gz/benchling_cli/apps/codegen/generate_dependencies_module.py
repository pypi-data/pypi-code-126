from benchling_api_client.v2.alpha.models.benchling_app_manifest import BenchlingAppManifest
from benchling_sdk.apps.helpers.config_helpers import (
    field_definitions_from_dependency,
    options_from_dependency,
    scalar_type_from_config,
    workflow_task_schema_output_from_dependency,
)
from jinja2 import Environment, PackageLoader

from benchling_cli.apps.codegen.helpers import (
    dependency_to_pascal_case,
    dependency_to_snake_case,
    is_secure_text_dependency,
    reformat_code_str,
)


def generate_dependencies_module(manifest: BenchlingAppManifest) -> str:
    env = Environment(
        loader=PackageLoader("benchling_cli.apps.codegen", "templates"),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("dependencies.py.jinja2")
    rendered_template = template.render(
        manifest=manifest,
        is_secure_text_dependency=is_secure_text_dependency,
        dependency_to_pascal_case=dependency_to_pascal_case,
        dependency_to_snake_case=dependency_to_snake_case,
        field_definitions_from_dependency=field_definitions_from_dependency,
        options_from_dependency=options_from_dependency,
        scalar_type_from_config=scalar_type_from_config,
        workflow_task_schema_output_from_dependency=workflow_task_schema_output_from_dependency,
    )

    return reformat_code_str(rendered_template)
