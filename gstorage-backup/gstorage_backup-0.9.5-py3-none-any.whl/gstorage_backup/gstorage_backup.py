from fire import Fire
from files_utils import _compact_and_upload

def upload(file_or_folder_path, bucket_name, remote_path=None):
    """Upload a file or folder for file_or_folder_path in bucket_name """
    return _compact_and_upload(file_or_folder_path, bucket_name, remote_path)

def main():
    Fire()

if __name__ == '__main__':
    Fire()