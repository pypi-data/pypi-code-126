import os


class PathUtil:
    @staticmethod
    def make_folder(path: str, folder_name: str) -> None:
        """
        创建文件夹
        :param path: 路径
        :param folder_name: 文件夹名称
        :return:
        """
        if not os.path.isdir(path + '/' + folder_name):
            os.mkdir(path + '/' + folder_name)


if __name__ == '__main__':
    make_folder('E:', 'test_folder')
