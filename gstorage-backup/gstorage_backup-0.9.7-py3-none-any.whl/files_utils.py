import zipfile
import os
import logging
from datetime import timezone
from google.cloud import storage
from datetime import datetime
from dotenv import load_dotenv
from slugify import slugify

load_dotenv()

BUCKET_NAME = os.getenv("BUCKET_NAME")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

def _compact_and_upload(file_or_folder_path, bucket_name, remote_path=None):
    if not GOOGLE_APPLICATION_CREDENTIALS:
        return "Set GOOGLE_APPLICATION_CREDENTIALS in env system to point to JSON file GCP"
    compact_file(file_or_folder_path)
    logging.info("Enviando arquivo pra cloud >>>>")
    """Uploads a file to the bucket."""
    storage_client = storage.Client.from_service_account_json(
        GOOGLE_APPLICATION_CREDENTIALS
    )
    bucket = storage_client.get_bucket(bucket_name)
    timestamp = slugify(str(datetime.now(timezone.utc)))
    source_file_name = f"{file_or_folder_path}.zip"
    destination_blob_name = source_file_name.split("/")[-1]
    destination_blob_name = f"{destination_blob_name[:-4]}.{timestamp}.zip"
    if remote_path:
        remote_path = f"{remote_path}/" if remote_path[-1] == "/" else remote_path
        destination_blob_name = f"{remote_path}/{destination_blob_name}"
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    os.remove(source_file_name)
    return f"UPLOAD file in path {destination_blob_name}"


def compact_file(zfilename):
    logging.info("Compactando arquivo >><<")
    zout = zipfile.ZipFile(f"{zfilename}.zip", "w", zipfile.ZIP_DEFLATED)
    zout.write(zfilename)
    zout.close()




# def uncompact_file(zfilename):
#     logging.info("Desompactando arquivo <<>>")
#     with zipfile.ZipFile(zfilename, "r") as zzz:
#         zzz.extractall()
#     logging.info("Excluindo arquivo compactado")
#     os.remove(zfilename)


# def download_file(bucket_name, source_blob_name, destination_file_name):
#     logging.info("Baixando arquivo da cloud <<<<")
#     """Downloads a blob from the bucket."""
#     storage_client = storage.Client.from_service_account_json("chave-storage-gcp.json")
#     bucket = storage_client.get_bucket(bucket_name)
#     blob = bucket.blob(source_blob_name)
#     if "/" in destination_file_name:
#         dir1 = destination_file_name.split("/")[0]
#         dir2 = os.path.join(dir1, destination_file_name.split("/")[1])
#         if not os.path.exists(dir1):
#             os.mkdir(dir1)
#         if not os.path.exists(dir2):
#             os.mkdir(dir2)
#     blob.download_to_filename(destination_file_name)
#     uncompact_file(destination_file_name)
