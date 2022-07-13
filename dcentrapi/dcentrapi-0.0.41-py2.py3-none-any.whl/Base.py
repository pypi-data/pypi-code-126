class Base:

    def __init__(self, stage, key):
        self.key = key
        self.headers = {'X-API-KEY': self.key}
        self.__version__ = '0.0.41'

        if stage == 'develop':
            self.url = "https://7nbvdnqrsc.execute-api.us-east-1.amazonaws.com/develop/"
        if stage == 'staging':
            self.url = "https://staging-api.dcentralab.com/"
