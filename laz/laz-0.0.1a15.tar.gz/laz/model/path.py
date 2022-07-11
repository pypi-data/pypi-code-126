class Path:
    sep = '/'

    def __init__(self, value: str, default_target: str = 'default'):
        self.value = value
        self.default_target = default_target

    def __repr__(self):
        return self.value

    @property
    def base(self) -> str:
        return self.sep.join(self.value.split(self.sep)[:-1])

    @property
    def target(self) -> str:
        return self.value.split(self.sep)[-1] or self.default_target

    @property
    def base_pattern(self) -> str:
        if self.base == '':
            return '**'
        else:
            return f'**/{self.base}/**'
