import os
import sys
from six.moves.urllib.request import urlretrieve
import tarfile

last_percent_reported = None

def download_progress_hook(count, blockSize, totalSize):
    """A hook to report the progress of a download. This is mostly intended for users with
    slow internet connections. Reports every 1% change in download progress.
    """
    global last_percent_reported
    percent = int(count * blockSize * 100 / totalSize)

    try:
        if (last_percent_reported != percent):
            if percent % 5 == 0:
                sys.stdout.write("%s%%" % percent)
                sys.stdout.flush()
            else:
                sys.stdout.write(".")
                sys.stdout.flush()

            last_percent_reported = percent
    except:
        last_percent_reported = percent


def download_svhn(save_path, dataset_name='train', force=False) -> str:
    """download SVHN dataset from the website

    Args:
        save_path (str): dataset save location *without ending slash   Ex: relative path : '../../data' or complete path 'C:/usr/local/project/data'
        dataset_name (str, optional): dataset type from 'train', 'test and 'extra'. Defaults to 'train'.
        force (bool, optional): Force download even the file already in the save_path. Defaults to False.

    Returns:
        str: downloaded file path Ex : '../data/train.tar.gz'
    """
    root_url = 'http://ufldl.stanford.edu/housenumbers/'
    file_name = f'{save_path}/{dataset_name}.tar.gz'
    folder_path = f'{save_path}/{dataset_name}'

    if force or (not os.path.exists(file_name)) or (os.path.isdir(folder_path)):
        print('Attempting to download:', file_name)
        filename, _ = urlretrieve(
            f'{root_url}{dataset_name}.tar.gz', file_name, reporthook=download_progress_hook)
        print('\nDownload Complete!')
    else:
        filename = file_name
        if os.path.exists(file_name):
            print(f' File name : {file_name} already exists in the system')
        elif os.path.exists(folder_path):
            print(f'Folder name : {folder_path} already exists in the systems')
    return filename


def extract_svhn(root_dir, folder_name, zip_dir, force=False) -> str:
    """Extract downloaded .tar file

    Args:
        filename (str): file path for .tar.gz file, basically the output from 'download_svhn()' function
        save_path (str, optional): folder directory for extraction location. Defaults to '' -> mean extract to folder that .tar file saved. custom path could or could not end with '/'
        force (bool, optional): extract and create a folder even there is folder with same name. Defaults to False.

    Returns:
        str: extracted folder directory
    """
    dest_dir = os.path.join(root_dir, folder_name)
    # if save_path == '':
    #     root = os.path.splitext(os.path.splitext(filename)[0])[0]  # remove .tar.gz
    # else:
    #     root = save_path
    if os.path.isdir(dest_dir) and not force:
        # You may override by setting force=True.
        print('%s already present - Skipping extraction of %s.' %
              (dest_dir, zip_dir))
    else:
        print('Extracting data for %s. This may take a while. Please wait.' % dest_dir)
        tar = tarfile.open(zip_dir)
        tar.extractall(dest_dir)
        tar.close()
    return dest_dir


def delete_zip(filename):
    """delete .tar.gz file after extracted"""
    assert os.path.exists(filename), f"{filename} does not exists"
    os.remove(filename)


def download(dataset_type='train', save_path='', extract=True, force=False, del_zip=False) -> str:
    """download svhn dataset and save [optional : extract, delete .tar file]

    Args:
        dataset_type (str, optional): dataset type from 'train', 'test and 'extra'. Defaults to 'train'.
        save_path (str, optional): dataset save location *without ending slash   Ex: relative path : '../../data' or complete path 'C:/usr/local/project/data'. Defaults to ''.
        extract (bool, optional): whether or not the downloaded .tar file extracts. Defaults to True.
        force (bool, optional): download and save even the dataset already in the given directory. Defaults to False.
        del_zip (bool, optional): whether or not delete the .tar file after extraction. Defaults to False.

    Returns:
        str: .tar file path if only downloaded, else the extraction had happened extraced folder directory
    """
    filename = download_svhn(save_path, dataset_type, force)
    # print('Filename : ', filename)
    
    if extract:
        save_folder = extract_svhn(save_path, dataset_type, filename, force)
        if del_zip:
            delete_zip(filename)
        filename = save_folder
        return filename
    else:
        return save_path
        
    
