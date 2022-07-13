class Base:

    def __init__(self, stage, key):
        self.key = key
        self.headers = {'X-API-KEY': self.key}
        self.__version__ = '0.0.40'

        if stage == 'develop':
            self.url = "https://d-d3crzxure7.execute-api.us-east-1.amazonaws.com/"
        if stage == 'staging':
            self.url = "https://staging-api.dcentralab.com/"
