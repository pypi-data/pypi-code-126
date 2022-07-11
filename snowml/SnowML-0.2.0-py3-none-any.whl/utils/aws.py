from fileinput import filename
import boto3, re, os

def s3_uri_to_parts(s3_uri) -> tuple:
  """
  Convert a s3 uri to a bucket, key and filename.

    Args:
        s3_uri (str): the s3 uri to convert.

    Returns:
        tuple: (bucket, key, filename)
  """
  bucket, key, filename = re.match(r"s3:\/{2}([\w-]+)\/(.*)\/(.*)", s3_uri).groups()
  return bucket, key, filename

def download_from_s3(uri=None, bucket=None, key=None, save_path='/tmp/', overwrite=False) -> str:
  """
  Download a file from s3 to local directory.

    Args:
        uri (str): the full s3 uri of the file to download. (Default: None)
        bucket (str): the s3 bucket of the file to download. Must be provided with key. (Default: None)
        key (str): the s3 key of the file to download. Must be provided with bucket. (Default: None)
        save_path (str): an existing local direcotry to save the file to. (Default: '/tmp/')
        overwrite (bool): whether to overwrite the file if it already exists. (Default: False)

    Returns:
        str: path to the locally saved file.
  """

  if uri is None and (bucket is None and key is None) or uri is not None and (bucket is not None or key is not None):
    raise ValueError("Must provide either a uri or bucket and key.")
  elif uri is None:
    uri = r's3://' + bucket + '/' + key

  bucket, key, filename = s3_uri_to_parts(uri)
  local_file_path = os.path.join(save_path, filename)

  if not os.path.exists(local_file_path) or overwrite:
    s3 = boto3.resource('s3')
    s3.meta.client.download_file(bucket, f"{key}/{filename}", local_file_path)

  return local_file_path
  
def upload_file_to_s3(bucket, key, local_file_path) -> str:
  """
  Upload a file to s3 bucket at a given key.

  Args:
      bucket (str): the bucket to upload the file to. 
      key (str): the spesific key to save the file in. 
      local_file_path (str): the local file path to upload.

  Returns:
      str: _description_
  """
  s3 = boto3.resource('s3')
  s3.meta.client.upload_file(full_file_path, bucket, local_file_path)