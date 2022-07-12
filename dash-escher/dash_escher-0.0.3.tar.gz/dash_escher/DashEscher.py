# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashEscher(Component):
    """A DashEscher component.
DashEscher visualizes a metabolic network using Escher Builder.
It takes two properties, `mapData` and `modelData`, and
displays the network.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- height (string; optional):
    Height of the canvas.

- mapData (list; required):
    The metabolic network map.

- modelData (dict; optional):
    The metabolic network model.

- options (dict; optional):
    Rendering options. Full list of options at
    https://escher.readthedocs.io/en/latest/javascript_api.html.

- width (string; optional):
    Width of the canvas."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_escher'
    _type = 'DashEscher'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, mapData=Component.REQUIRED, modelData=Component.UNDEFINED, options=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'height', 'mapData', 'modelData', 'options', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'height', 'mapData', 'modelData', 'options', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['mapData']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashEscher, self).__init__(**args)
