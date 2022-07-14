import typing as t

import mantik.unicore._config._base as _base


def get_required_config_value(
    name: str, value_type: t.Type, config: t.Dict
) -> t.Any:
    """Get a required config value.

    Parameters
    ----------
    name : str
        Name of the config value.
    value_type : type
        Python type that the value is expected to have.
        Value will be cast to that type.
    config : t.Dict
        The config to read from.

    Raises
    ------
    ValueError
        If the config value is not present in the config.

    Returns
    -------
    Any
        The value from the config cast as `value_type`.

    """
    if name not in config:
        raise ValueError(f"Backend config is missing entry for key '{name}'")
    return _get_config_value(name=name, value_type=value_type, config=config)


def get_optional_config_value(
    name: str, value_type: t.Type, config: t.Dict
) -> t.Any:
    """Get an optional config value.

    Parameters
    ----------
    name : str
        Name of the config value.
    value_type : type
        Python type that the value is expected to have.
        Value will be cast to that type.
    config : t.Dict
        The config to read from.

    Returns
    -------
    Any or None
        The value from the config cast as `value_type`, `None` if not present.

    """
    if name not in config:
        return None
    return _get_config_value(name=name, value_type=value_type, config=config)


def _get_config_value(name: str, value_type: t.Type, config: t.Dict) -> t.Any:
    value = config[name]
    return _cast_type(name=name, value=value, value_type=value_type)


def _cast_type(name: str, value: str, value_type: t.Type) -> t.Any:
    try:
        return value_type(value)
    except ValueError:
        raise ValueError(
            f"Backend config value for '{name}' has to be of type {value_type}"
        )


def create_dict_with_not_none_values(**kwargs) -> t.Dict:
    """Create a dict which only contains value that are not `None`."""
    return {
        key: _convert_value(value)
        for key, value in kwargs.items()
        if value is not None
    }


def _convert_value(value: t.Union[t.Any, _base.ConfigObject]) -> t.Any:
    if isinstance(value, _base.ConfigObject):
        return value.to_dict()
    elif isinstance(value, bool):
        return str(value).lower()
    return value
