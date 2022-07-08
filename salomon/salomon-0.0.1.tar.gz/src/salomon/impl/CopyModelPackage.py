import boto3, os, time
from pprint import pprint
import docker
from .s3_helper import parse_s3_url


def copy_model_package(source_arn: str, dst_account_id: str, dst_name: str, dst_group_name: str, dst_s3_path: str, dst_ecr: str):
    """
    Makes a copy of SageMaker Model Package.

    1. Reads source_arn SageMaker Model Package
    2. Replaces paths for data files with `dst_s3_path`
    3. Replaces docker image URIs with `dst_ecr`
    4. Makes a copy of data files to `dst_s3_path`
    5. Pulls docker images and then pushes to `dst_ecr`
    6. Creates new SageMaker Model Package in current AWS account.

    :param source_arn:
    :param dst_account_id:
    :param dst_name:
    :param dst_group_name:
    :param dst_s3_path:
    :param dst_ecr:
    :return:
    """
    sm = boto3.client('sagemaker')
    src_model_package = sm.describe_model_package(ModelPackageName=source_arn)

    dst_model_package, files_to_copy, docker_images_to_copy = rebuild_model_package(src_model_package, dst_account_id, dst_name, dst_group_name, dst_s3_path, dst_ecr)
    pprint(dst_model_package)
    pprint(files_to_copy)
    pprint(docker_images_to_copy)

    copy_files(files_to_copy)
    copy_docker_images(docker_images_to_copy)

    response = sm.create_model_package(**dst_model_package)
    pprint(response)

    pass


def rebuild_model_package(src_model_package: dict, dst_account_id: str, dst_name: str, dst_group_name: str, dst_s3_path: str, dst_ecr: str):
    dont_copy_keys = [
        'ModelPackageName', 'ModelPackageGroupName',
        'ModelPackageVersion', 'ModelPackageArn', 'CreationTime', 'ModelPackageStatus', 'ModelPackageStatusDetails',
        'CreatedBy', 'LastModifiedTime', 'LastModifiedBy', 'ApprovalDescription', 'ResponseMetadata']

    dst_model_package = {}
    for k, v in src_model_package.items():
        if k not in dont_copy_keys:
            dst_model_package[k] = v

    # dst_model_package['Tags'] = []
    # dst_model_package['ModelPackageName'] = dst_name
    dst_model_package['ModelPackageGroupName'] = dst_group_name

    files_to_copy = []
    docker_images_to_copy = []
    for container in dst_model_package.get("InferenceSpecification").get("Containers"):
        # copy docker image
        p: tuple = prepare_docker_urls(container.get("Image"), dst_ecr)
        docker_images_to_copy.append(p)

        del container["ImageDigest"]

        # copy files
        p: tuple = prepare_file_paths(container.get("ModelDataUrl"), dst_s3_path)
        container["ModelDataUrl"] = p[1]
        files_to_copy.append(p)

        if type(container.get("Environment")) is dict:
            for var_name, var_value in container["Environment"].items():
                if var_value.startswith("s3://"):
                    p: tuple = prepare_file_paths(var_value, dst_s3_path)
                    container["Environment"][var_name] = p[1]
                    files_to_copy.append(p)
    return dst_model_package, files_to_copy, docker_images_to_copy


def prepare_file_paths(src: str, dst_s3_path: str):
    filename = os.path.basename(src)
    dst = join_uri(dst_s3_path, filename)
    return src, dst


def join_uri(path: str, filename: str) -> str:
    if path.endswith("/") or path == "":
        return f"{path}{filename}"
    else:
        return f"{path}/{filename}"


def prepare_docker_urls(src_uri: str, dst_ecr: str):
    # 492215442770.dkr.ecr.eu-central-1.amazonaws.com/sagemaker-scikit-learn:0.23-1-cpu-py3

    src_repository, src_tag = src_uri.split(":")
    if "/" in src_repository:
        src_image = src_repository.split("/")[1]
    else:
        src_image = src_repository

    dst_tag = f"{src_image}-{src_tag}"

    return src_uri, f"{dst_ecr}:{dst_tag}"


def copy_files(files_to_copy: list):
    s3 = boto3.resource('s3')
    for src, dst in files_to_copy:
        src_tuple = parse_s3_url(src)
        dst_tuple = parse_s3_url(dst)
        copy_source = {
            'Bucket': src_tuple[0],
            'Key': src_tuple[1]
        }
        print(f"Copying from {src} to {dst}")
        s3.meta.client.copy(copy_source, dst_tuple[0], dst_tuple[1])


def copy_docker_images(images_to_copy: list):
    docker_client = docker.from_env()
    for src, dst in images_to_copy:
        src_repository, src_tag = src.split(":")
        dst_repository, dst_tag = dst.split(":")

        print(f"Pulling image {src_repository}:{src_tag}")
        image = docker_client.images.pull(repository=src_repository, tag=src_tag)

        print(f"Tagging image {src_repository}:{src_tag} with {dst_repository}:{dst_tag}")
        image.tag(repository=dst_repository, tag=dst_tag)

        print(f"Pushing image {dst_repository}:{dst_tag}")

        prev_ts = time.time() - 10
        for line in docker_client.api.push(repository=dst_repository, tag=dst_tag, stream=True, decode=True):
            ts = time.time()
            if ts - prev_ts > 10:
                prev_ts = ts
                print(line)


def list_docker_images_in_model_package(source_arn: str):
    sm = boto3.client('sagemaker')
    src_model_package = sm.describe_model_package(ModelPackageName=source_arn)

    return [container.get("Image") for container in src_model_package.get("InferenceSpecification").get("Containers")]

