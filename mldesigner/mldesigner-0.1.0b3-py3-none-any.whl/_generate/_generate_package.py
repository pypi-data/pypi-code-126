# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from typing import Union

from mldesigner._logger_factory import _LoggerFactory

generate_pkg_logger = _LoggerFactory.get_logger("generate_package")


def generate_package(
    *,
    assets: Union[list, dict, str],
    package_name: str = None,
    force_regenerate: bool = False,
    **kwargs,
) -> None:
    """For a set of assets, generate a python module which contains component consumption functions and import it
    for use.

    Supported asset types:
       - components: component consumption functions


    :param assets: List[assets_identifier], dict[module_relative_path, List[assets_identifier]] or str

        * None: we will generate a module with ml_client.from_config() if assets not specified, not supported for now.

        * list example: specify as assets pattern list and we will generate modules

            .. code-block:: python

                # workspace assets, module name will be workspace name
                assets = ["azureml://subscriptions/{subscription_id}/resourcegroups/{resource_group}/
                          workspaces/{workspace_name}"]

                # registry assets, module name will be registry name
                assets = ["azureml://registries/HuggingFace"]

                # local assets, module name will be "components"
                assets = ["components/**/component_spec.yaml"]

        * dict example: component module name relative path as key and List[assets_identifier] as value

            .. code-block:: python

                # module name with an assets identifier
                assets = {"path/to/component/module": "azureml://subscriptions/{subscription_id}/"
                                         "resourcegroups/{resource_group}/workspaces/{workspace_name}"}
                # module name with a list of assets identifier
                assets = {"path/to/component/module": ["azureml://subscriptions/{subscription_id}/"
                                          "resourcegroups/{resource_group}/workspaces/{workspace_name}",
                                          "components/**/component_spec.yaml"]}

        * str example: assets.yaml, config file which contains the asset dict

        .. remarks::

            module_relative_path: relative path of generate component module
                * When package name not provided, component module name relative path will relative to current folder
                * When package name is provided, component module name relative path will relative to generated package folder
            components: single or list of glob string which specify a set of components. Example values:
                * assets from workspace
                    1. all assets
                        ``azureml://subscriptions/{subscription_id}/resource_group/{resource_group}/
                        workspaces/{workspace_name}``
                    2. components with name filter
                        ``azureml://subscriptions/{subscription_id}/resource_group/{resource_group}
                        /workspaces/{workspace_name}/components/microsoft_samples_*``
                * components from local yaml
                    ``components/**/component_spec.yaml``
                * components from registries
                    For registry concept, please see: `https://aka.ms/azuremlsharing`.
                    azureml://registries/HuggingFace  # All assets in registry HuggingFace.
                    azureml://registries/HuggingFace/components/Microsoft*

    :type assets: typing.Union[list, dict, str]
    :param package_name: name of the generated python package. Example: cool-component-package
        * If specified: we generate the module file to specified package.
            * If the cool-component-package folder does not exists, we will create a new skeleton package under
            ./cool-component-package and print info in command line and ask user to do:
            ``pip install -e ./cool-component-package``
            Then next user can do: 'from cool.component.package import component_func'
            * If the folder exists, we will try to update component folders inside .
        * If not specified, we generate the module directory under current directory.
    :type package_name: str
    :param force_regenerate: whether to force regenerate the python module file.
        * If True, will always regenerate component folder.
        * If False, will reuse previous generated file. If the existing file not valid, raise import error.
    :type force_regenerate: bool
    :param kwargs: A dictionary of additional configuration parameters.
    :type kwargs: dict
    """
    # import locally so generate package interface don't depend on azure-ai-ml
    from mldesigner._generate._generate_package_impl import _generate_package

    return _generate_package(assets=assets, package_name=package_name, force_regenerate=force_regenerate, **kwargs)
