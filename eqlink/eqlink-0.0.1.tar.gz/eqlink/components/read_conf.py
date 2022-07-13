import yaml


class ReadConf:
    def __init__(self, path):
        self.conf_path = path
        self.configuration = {}

    def __read__(self, item):
        if bool(self.configuration) is False:
            try:
                f = open(self.conf_path, 'r', encoding='utf-8')
                cont = f.read()
                self.configuration = yaml.load(cont, Loader=yaml.FullLoader)
            except Exception as e:
                print(e)
                return ''
        items = item.split('.')
        res = self.configuration
        for i in items:
            res = res[i]
        return res
