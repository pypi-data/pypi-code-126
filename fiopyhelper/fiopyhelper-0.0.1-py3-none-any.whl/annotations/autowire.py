import inspect
import functools
import fiopy

__all__ = ["autowire"]


def autowire(*, argmap={}):
    def wrapper(func):
        @functools.wraps(func)
        def wrapped(self, **kwargs):
            signature = inspect.signature(func)
            kwargs["user"] = kwargs.get("user") or fiopy.Fio.default_user()
            for name, value in signature.parameters.items():
                if not kwargs.get(name) and name != "self" and name != "user":
                    wired_value = None
                    if "." in argmap.get(name, name):
                        for name_part in argmap.get(name, name).split("."):
                            wired_value = getattr(
                                wired_value or self,
                                argmap.get(name_part, name_part),
                                None,
                            )
                    else:
                        wired_value = getattr(self, argmap.get(name, name), None)
                    kwargs[name] = wired_value or value.default

            return func(self, **kwargs)

        return wrapped

    return wrapper
