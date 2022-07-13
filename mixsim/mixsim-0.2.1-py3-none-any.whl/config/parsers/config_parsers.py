import toml


class TOMLParser:
    @staticmethod
    def parse_string(s):
        try:
            return toml.loads(f'val = {s}')['val']
        except toml.decoder.TomlDecodeError:
            return s

    @staticmethod
    def load_config(stream):
        return toml.load(stream)

    @staticmethod
    def save_config(d, stream=None, **kwargs):
        if stream is None:
            return toml.dumps(d, **kwargs)
        else:
            return toml.dump(d, stream, **kwargs)
