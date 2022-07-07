import csv


class WorkCSV:
    """класс для работы с CSV файлами"""
    def __init__(self, path_file: str, file_name: str):
        self.path_file = path_file
        self.file_name = file_name
        self.full_path = path_file + file_name

    def read_csv(self, delimiter: bool = True, delimiter_symbol: str = "|") -> list:
        """читаем csv файл, отдаем инфо инфо в виде list"""
        if delimiter:
            with open(self.full_path) as f:
                reader = csv.reader(f, delimiter=delimiter_symbol, quotechar="}")
                list_info_csv = list(reader)

            return list_info_csv
        else:
            list_info_csv = []
            with open(self.full_path) as f:
                reader = csv.reader(f)
                for row in reader:
                    list_info_csv.append(row)
            return list_info_csv

    def write_csv(self, data: list):
        """создаем новый csv файл, прнимает путь, название файла и  data(инфо, которую записываем в файл)"""

        with open(self.full_path, 'w') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)

    def selective_reading_csv(self, fragment: str = None) -> list:
        """Записываем в data(в результат выполнения функции, только те строки,
        в которым присутствует fragment)"""
        my_data = []
        with open(self.full_path) as csvfile:
            spam_reader = csv.reader(csvfile)

            for row in spam_reader:
                if fragment in (', '.join(row)):
                    my_data.append((', '.join(row)).split('|'))
        return my_data
