import mimetypes


class FileInfo:
    @staticmethod
    def get_file_info(file):
        filename = None
        if isinstance(file, tuple):
            if len(file) == 2:
                path, mime = file
            else:
                path, mime, filename = file
        else:
            path = file
            mime = mimetypes.guess_type(file)[0]
        if isinstance(path, bytes):
            content = path
        else:
            content = open(path, "rb")

        return filename, path, mime, content
