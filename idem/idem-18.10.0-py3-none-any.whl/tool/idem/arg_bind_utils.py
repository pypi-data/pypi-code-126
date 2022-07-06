from typing import Any
from typing import Dict
from typing import List


def parse_dict_and_list(
    hub,
    data: Dict or List,
    key: Any,
    default: Any = None,
):
    """
    Traverse a dict or list using a colon-delimited (or otherwise delimited,
    using the 'delimiter' param) target string. The target 'foo:bar:0' will
    return data['foo']['bar'][0] if this value exists, and will otherwise
    return the dict in the default argument.
    List resolution - The target 'foo:bar:[0]' or 'foo:bar[0]' will return data['foo']['bar'][0] if data
    like {'foo':{'bar':['baz']}}
    Dict resolution - The target 'foo:bar:0' will return data['foo']['bar'][0] if data like
    {'foo':{'bar':{'0':'baz'}}}
    """
    ptr = data
    for each in key:
        key_to_parse, index_digits = hub.idem.rules.arg_resolver.parse_index(each)
        if isinstance(ptr, list):
            if key_to_parse:
                raise ValueError(
                    f"Index provided was {key_to_parse}. List index should be an integer"
                )

            if index_digits:
                try:
                    for index in index_digits:
                        ptr = ptr[index]
                except IndexError:
                    raise IndexError(f"Index {index} not found in the list {ptr}")
        else:
            try:
                if key_to_parse:
                    ptr = ptr[key_to_parse]

                if index_digits and isinstance(ptr, dict):
                    raise ValueError(
                        f"Index {index_digits} access not supported in dict"
                    )
                if index_digits:
                    try:
                        for index in index_digits:
                            ptr = ptr[index]
                    except IndexError:
                        raise IndexError(f"Index {index} not found in the list {ptr}")

            except KeyError:
                raise KeyError(
                    f"Key {key_to_parse} not present in the dictionary {ptr}"
                )
            except TypeError:
                return default
    return ptr


async def find_arg_reference_data(hub, arg_bind_expr: str):
    """
    Resolve ${cloud:state:attribute_path} expressions to a value used in jinja using the hub's RUNNING dictionary
    """

    state_data = None

    run_name = hub.idem.RUN_NAME

    arg_bind_arr = arg_bind_expr.split(":")

    if len(arg_bind_arr) < 2:
        hub.log.debug(
            f" arg-bind expression `{arg_bind_expr}` doesn't comply with standards. Expected format is "
            f"$'{'resource_state:resource_name:attribute-path'}'  "
        )
        return state_data, False

    state_id = arg_bind_arr[1]

    attribute_path = None

    if len(arg_bind_arr) > 2:

        """
        From the arg-bind template - ${cloud:state:[0]:attribute:[1]} , get the attribute path [0]:attribute:[1]
        which will be used to resolve the correct value from the new_state.
        """
        attribute_path = arg_bind_arr[2:]

    run_data = hub.idem.RUNS.get(run_name, None)
    low_data = None
    if run_data:
        low_data = run_data.get("low", None)

    tag = None
    if low_data:
        for low in low_data:
            if "__id__" in low and low["__id__"] == state_id:
                ctx = low.get("ctx", None)
                if ctx:
                    tag = ctx.get("tag", None)
                break

    arg_bind_template = "${" + arg_bind_expr[0] + "}"

    if not tag:
        hub.log.debug(
            f"Could not parse `{arg_bind_expr}` in jinja. The data for arg_binding reference `{arg_bind_template}` "
            f"could not be found on the hub. "
        )
        return state_data, False

    if run_data:
        executed_states = run_data.get("running", None)
        if executed_states is not None and tag in executed_states:
            state_data = executed_states.get(tag).get("new_state", None)
            if state_data and attribute_path:
                state_data = hub.tool.idem.arg_bind_utils.parse_dict_and_list(
                    state_data, attribute_path
                )

    return state_data, True
