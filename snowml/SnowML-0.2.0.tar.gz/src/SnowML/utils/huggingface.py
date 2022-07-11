from .aws import upload_file_to_s3
import os


def save_and_upload_pretrained(objs, bucket, key, local_dir='/tmp/'):
  """
      Save a list of objects from local directory to remote s3 bucket.

      Args:
        objs(list): A list of huggingface objects to save.
        bucket(str): S3 bucket to uploadf files to.
        key(str): the remote directory to save the files to.
        local_dir(str): the local directory to save the files to before they're being uploaded. Defaults to '/tmp/'.
  """ 
  # create local path, if doesnt exist
  if not os.path.exists(local_dir):
    os.makedirs(local_dir)
  
  # save each object files into local dir
  for obj in objs:
    obj.save_pretrained(local_dir)
  
  # upload files from local dir to remote
  for f in os.listdir(local_dir):
    full_file_path = os.path.join(local_dir, f)
    upload_file_to_s3(bucket, key, full_file_path)