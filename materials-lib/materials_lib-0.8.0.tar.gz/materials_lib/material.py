import toml
from pathlib import Path

class Material:
    def __init__(self, name: str, material_spec: str = None, unit_registry = None):
        if unit_registry is None:
            self._with_units = False
        else:
            self._with_units = True
            self._ureg = unit_registry

        if material_spec is None:   # Define default argument
            self._spec = "standard"
        else:
            self._spec = material_spec

        self._all_properties = toml.load(f"{Path(__file__).parent.resolve()}/data/{name.lower()}.toml")
        self._properties = self._all_properties[self._spec]

    def E(self, unit = None):
        unitless_value = self._properties['e']
        if not self._with_units:
            return self._properties['e']
        else:
            value = unitless_value * self._ureg.Pa
            if unit is None:
                return value
            else:
                return value.to(unit)

    def poisson(self):
        return self._properties['poisson']

    def density(self, unit = None):
        unitless_value = self._properties['density']
        if not self._with_units:
            return unitless_value
        else:
            value = unitless_value  * (self._ureg.kg/self._ureg.m**3)
            if unit is None:
                return value
            else:
                return value.to(unit)

    def G(self):
        return self.E()/(2.0*(1+self.poisson()))

    def G_rotation(self):
        return self.E()/(1+self.poisson())
