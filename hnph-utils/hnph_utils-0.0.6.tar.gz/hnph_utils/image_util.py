import os
from PIL import Image


class ImageUtil:
    @staticmethod
    def get_image_direction(path: str) -> str:
        """
        获取图片方向
        :param path: 图片路径
        :return: H 横向长方形、V 纵向长方形、S 正方形
        """
        im = Image.open(path)
        if im.size[0] > im.size[1]:
            return 'H'
        elif im.size[0] < im.size[1]:
            return 'V'
        else:
            return 'S'

    @staticmethod
    def load_all_image_files_cascade(path: str) -> list:
        """
        加载文件夹下面所有图片文件（支持 BMP、JPG、PNG、TIF 四种格式图片文件）（包含下级子目录）
        :param path: 文件路径
        :return:
        """
        image_file_list = []
        for file_name in os.listdir(path):
            real_path = path + '/' + file_name
            if os.path.isfile(real_path):
                if not file_name.startswith('~'):
                    if file_name.upper().endswith('.BMP') \
                            or file_name.upper().endswith('.JPG') \
                            or file_name.upper().endswith('.PNG') \
                            or file_name.upper().endswith('.TIF'):
                        image_file_list.append({
                            'file_name': file_name,
                            'file_path': real_path
                        })
            else:
                for pdf_file in ImageUtil.load_all_image_files_cascade(real_path):
                    image_file_list.append(pdf_file)
        return image_file_list

    @staticmethod
    def load_all_image_files(path: str) -> list:
        """
        加载文件夹下面所有图片文件（支持 BMP、JPG、PNG、TIF 四种格式图片文件）
        :param path: 文件路径
        :return:
        """
        image_file_list = []
        for file_name in os.listdir(path):
            real_path = path + '/' + file_name
            if os.path.isfile(real_path):
                if not file_name.startswith('~'):
                    if file_name.upper().endswith('.BMP') \
                            or file_name.upper().endswith('.JPG') \
                            or file_name.upper().endswith('.PNG') \
                            or file_name.upper().endswith('.TIF'):
                        image_file_list.append({
                            'file_name': file_name,
                            'file_path': real_path
                        })
        return image_file_list
