import urllib.request
import urllib.error


class Downloader:
    def __init__(self, connection):
        self.connection = connection

    def download(self, path, filename):
        file_path = self.connection.getmainurl() + path
        try:
            urllib.request.urlretrieve(file_path, filename)
        except urllib.error.HTTPError:
            return False
        return True
