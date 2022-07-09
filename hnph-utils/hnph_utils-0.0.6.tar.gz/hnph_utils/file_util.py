import os


class FileUtil:
    @staticmethod
    def load_all_pdf_file_cascade(path: str) -> list:
        """
        从路径下加载所有 PDF 文件（含子目录）
        :param path: 路径
        :return:
        """
        file_list = []
        for file_name in os.listdir(path):
            real_path = path + '/' + file_name
            if os.path.isfile(real_path):
                if not file_name.startswith('~'):
                    if file_name.upper().endswith('.PDF'):
                        file_list.append({
                            'file_name': file_name,
                            'file_path': real_path
                        })
            else:
                for pdf_file in FileUtil.load_all_pdf_file_cascade(real_path):
                    file_list.append(pdf_file)
        return file_list

    @staticmethod
    def load_all_excel_file_cascade(path: str) -> list:
        """
        加载目录下所有 Excel 文件（含目录及子目录下 xls 及 xlsx 文件）
        :param path: 路径
        :return:
        """
        file_list = []
        for file_name in os.listdir(path):
            real_path = path + '/' + file_name
            if os.path.isfile(real_path):
                if not file_name.startswith('~'):
                    if file_name.upper().endswith('.XLS') or file_name.upper().endswith('.XLSX'):
                        file_list.append({
                            'file_name': file_name,
                            'file_path': real_path
                        })
            else:
                for excel_file in FileUtil.load_all_excel_file_cascade(real_path):
                    file_list.append(excel_file)
        return file_list

    @staticmethod
    def load_all_csv_file(path: str) -> list:
        """
        加载目录下素有csv文件
        :param path:
        :return:
        """
        file_list = []
        for file_name in os.listdir(path):
            real_path = path + '/' + file_name
            if os.path.isfile(real_path):
                if not file_name.startswith('~'):
                    if file_name.upper().endswith('.CSV'):
                        file_list.append({
                            'file_name': file_name,
                            'file_path': real_path
                        })
        return file_list

    @staticmethod
    def file_rename(file_path: str, file_old_name: str, file_new_name: str) -> None:
        """
        文件重命名
        :param file_path: 文件路径
        :param file_old_name: 旧文件名
        :param file_new_name: 新文件名
        :return:
        """
        old_file = file_path + '/' + file_old_name
        new_file = file_path + '/' + file_new_name
        os.rename(old_file, new_file)
