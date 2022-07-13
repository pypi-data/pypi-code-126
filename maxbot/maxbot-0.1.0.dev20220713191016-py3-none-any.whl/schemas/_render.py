import re

import yaml

from ..errors import BotError, YamlSnippet, YamlSymbols


class Yaml:
    def __init__(self):
        self.Loader = LoaderFactory.new_loader()
        self.Loader.register_debug_watcher()

    def loads(self, data):
        return self.Loader.load(data)


class YamlConfig:
    def loads(self, data, variables=None):
        Loader = LoaderFactory.new_loader()
        Loader.register_scenario_syntax()
        Loader.register_variable_substitution(variables)
        Loader.register_debug_watcher()
        return Loader.load(data)


class LoaderFactory(yaml.SafeLoader):
    @classmethod
    def new_loader(cls):
        return type("ConcreteLoader", (cls,), {})

    @classmethod
    def load(cls, data):
        try:
            # nosec note: actualy we derive a safe loader
            return yaml.load(data, Loader=cls)  # nosec B506
        except yaml.MarkedYAMLError as exc:
            raise YamlParsingError(exc)

    @classmethod
    def register_scenario_syntax(cls):
        def jinja_syntax(syntax):
            def constructor(loader, node):
                rv = {"content": loader.construct_scalar(node), "syntax": syntax}
                YamlSymbols.add(rv, node)
                return rv

            if syntax == "raw":
                # raw syntax is default
                cls.add_constructor("!jinja", constructor)
            cls.add_constructor(f"!jinja/{syntax}", constructor)

        jinja_syntax("raw")
        jinja_syntax("yaml")

    @classmethod
    def register_variable_substitution(cls, variables):
        variables = variables or {}
        VARIABLE = re.compile(r".*?\$\{([^}{:]+)(:([^}]+))?\}.*?")

        def substitute_variables(loader, node):
            string = loader.construct_scalar(node)
            for name, with_colon, default in VARIABLE.findall(string):
                if with_colon:
                    value = variables.get(name, default)
                else:
                    value = variables[name]
                string = string.replace(f"${{{name}{with_colon}}}", value, 1)
            return string

        cls.add_constructor("!ENV", substitute_variables)

    @classmethod
    def register_debug_watcher(cls):
        def watch_mapping(loader, node):
            rv = loader.construct_mapping(node)
            YamlSymbols.add(rv, node)
            return rv

        def watch_sequence(loader, node):
            rv = loader.construct_sequence(node)
            YamlSymbols.add(rv, node)
            return rv

        def watch_string(loader, node):
            rv = loader.construct_scalar(node)
            YamlSymbols.add(rv, node)
            return rv

        cls.add_constructor("tag:yaml.org,2002:map", watch_mapping)
        cls.add_constructor("tag:yaml.org,2002:seq", watch_sequence)
        cls.add_constructor("tag:yaml.org,2002:str", watch_string)


class YamlParsingError(BotError):
    def __init__(self, exc):
        lines = []
        if exc.context:
            lines.append(exc.context)
        if exc.context_mark:
            lines.append(YamlSnippet(exc.context_mark).at_mark())
        if exc.problem:
            lines.append(exc.problem)
        if exc.problem_mark:
            lines.append(YamlSnippet(exc.problem_mark).at_mark())
        if exc.note:
            lines.append(exc.note)
        super().__init__("\n".join(lines))
