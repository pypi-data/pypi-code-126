import inspect
from typing import Any, Awaitable, Callable, Coroutine, Dict, List, TypeVar, Union

T = TypeVar("T")


async def async_invoke(
    func: Callable[[Any], Union[T, Coroutine[Any, Any, T]]], *args, **kwargs
) -> Awaitable[T]:
    sig = inspect.signature(func)
    call_args: List[Any] = []
    call_kwargs: Dict[str, Any] = {}
    args_index = 0
    for param_name, param_info in sig.parameters.items():
        if param_name in kwargs:
            call_kwargs[param_name] = kwargs[param_name]
        elif param_info.kind in {
            inspect.Parameter.POSITIONAL_OR_KEYWORD,
            inspect.Parameter.POSITIONAL_ONLY,
        }:
            if args_index < len(args):
                call_args.append(args[args_index])
                args_index += 1
        elif param_info.kind is inspect.Parameter.VAR_KEYWORD:
            call_kwargs[param_name] = kwargs
        elif param_info.kind is inspect.Parameter.VAR_POSITIONAL:
            call_args.extend(args[args_index:])
            args_index = len(args)

    if inspect.iscoroutinefunction(func):
        r = await func(*call_args, **call_kwargs)
    else:
        r = func(*call_args, **call_kwargs)
    return r


async def await_if_needed(val: Union[T, Awaitable[T]]) -> T:
    if inspect.isawaitable(val):
        return await val
    else:
        return val
