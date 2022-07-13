from functools import singledispatch

import jinja2
from jinja2.exceptions import TemplateSyntaxError
from jinja2.ext import Extension
from jinja2.nodes import Assign, Call, ContextReference, Getattr, Keyword, Name

from ..errors import BotError, YamlSnippet, YamlSymbols


class VariablesExtension(Extension):

    tags = {"slot", "user"}

    def parse(self, parser):
        var = parser.stream.current.value
        lineno = next(parser.stream).lineno

        name = parser.stream.expect("name").value
        parser.stream.expect("assign")
        value = parser.parse_expression()

        # transform our custom statements into dict updates
        # {% user name = 'Bob' %}
        #   -> {% set _ = user.update({'name': 'Bob'}) %}
        # {% slot guests = entities.number %}
        #   -> {% set _ = slots.update({'guests': entities.number}) %}
        if var == "slot":
            var = "slots"
        method = Getattr(Name(var, "load"), "update", ContextReference())
        call = Call(method, [], [Keyword(name, value)], None, None)
        dummy = Name("_", "store")
        return Assign(dummy, call).set_lineno(lineno)


# nosec note: autoescape is not actual when rendering yaml
jinja_env = jinja2.Environment(extensions=[VariablesExtension], autoescape=False)  # nosec B701


JINJA_ERRORS = (
    TypeError,
    ValueError,
    LookupError,
    ArithmeticError,
    AttributeError,
    jinja2.TemplateError,
)


def Expression(source):
    try:
        expr = jinja_env.compile_expression(source)
    except TemplateSyntaxError as exc:
        _bot_error(exc.message, source, exc.lineno)

    def evaluate(context, **params):
        params = _build_params(context, params)
        try:
            return expr(**params)
        except JINJA_ERRORS as exc:
            # jinja always treats expressions as on line
            _bot_error(str(exc), source, line=1)

    return evaluate


@singledispatch
def Scenario(raw):
    raise TypeError(f"Unexpected argument type {type(raw)}")


@Scenario.register(dict)
def Template(template):
    if template["syntax"] == "raw":
        load = template["schema"].load
    elif template["syntax"] == "yaml":
        load = template["schema"].loads
    else:
        raise ValueError(f"Unknown content syntax {template['syntax']}")

    try:
        tpl = jinja_env.from_string(template["content"])
    except TemplateSyntaxError as exc:
        _bot_error(exc.message, template, exc.lineno)

    def template_(context, **params):
        params = _build_params(context, params)
        try:
            document = tpl.render(**params)
        except TemplateSyntaxError as exc:
            _bot_error(exc.message, template, exc.lineno)
        except JINJA_ERRORS as exc:
            _bot_error(str(exc), template, _extract_lineno(exc))

        if isinstance(document, str) and document.strip():
            try:
                return load(document)
            except BotError as exc:
                # wrap original error to include template snippet
                _bot_error(str(exc), template, line=1)
            finally:
                # cleanup globally stored data to avoid memory leaks
                YamlSymbols.cleanup(document)
        else:
            return []

    return template_


@Scenario.register(list)
def Commands(cmd_list):
    def commands(context, **params):
        return cmd_list

    return commands


def _build_params(context, params):
    result = vars(context)
    if params is not None:
        result.update(params)
    return result


def _bot_error(exc, source, line):
    raise BotError(exc, YamlSnippet.format(source, line=line))


def _extract_lineno(exc):
    """
    Extract line where template error is occured
    assuming that traceback was rewritten by jinja
    @see jinja2.debug.rewrite_traceback_stack
    """
    tb = exc.__traceback__
    lineno = None
    while tb:
        if tb.tb_frame.f_code.co_filename == "<template>":
            lineno = tb.tb_lineno
        tb = tb.tb_next
    return lineno
