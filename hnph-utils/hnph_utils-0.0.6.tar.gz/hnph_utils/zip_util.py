import zipfile


def gen_zip_file(zip_file_name: str, folder_name: str, user_list: list):
    """
    生成 ZIP 文件
    """
    zip_file = zipfile.ZipFile(zip_file_name, mode='w')

    for user in user_list:
        for image in user['image_list']:
            zip_file.write(
                image['file_path'],
                folder_name + '/' + user['user_name'] + '/' + image['file_name'] + image['file_path'][image['file_path'].rindex('.'):]
            )

    zip_file.close()
