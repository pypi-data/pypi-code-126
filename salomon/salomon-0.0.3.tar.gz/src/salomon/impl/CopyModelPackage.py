import boto3, os, time, tempfile, logging
import docker
from .s3_helper import parse_s3_url


def copy_model_package(
        source_arn: str, dst_group_name: str, dst_s3_path: str, dst_ecr: str,
        src_session: boto3.session.Session = boto3.session.Session(),
        dst_session: boto3.session.Session = boto3.session.Session(),
        docker_client: docker.client.DockerClient = docker.client.from_env()
):
    """
    Makes a copy of SageMaker Model Package.

    1. Reads source_arn SageMaker Model Package
    2. Replaces paths for data files with `dst_s3_path`
    3. Replaces docker image URIs with `dst_ecr`
    4. Makes a copy of data files to `dst_s3_path`
    5. Pulls docker images and then pushes to `dst_ecr`
    6. Creates new SageMaker Model Package in current AWS account.

    :param source_arn: source model package ARN.
    :param dst_group_name: target model package group name.
    :param dst_s3_path: target S3 path, where model files will be copied to.
    :param dst_ecr: target ECR, where images will be copied to.
    :param src_session: boto3.session.Session, used only in source AWS account.
    :param dst_session: boto3.session.Session, used only in destination AWS account.
    :param docker_client: docker.client.DockerClient
    :return: ARN of created model
    """
    logger = logging.getLogger(__name__)
    src_sm = src_session.client('sagemaker')
    dst_sm = dst_session.client('sagemaker')
    src_model_package = src_sm.describe_model_package(ModelPackageName=source_arn)

    dst_model_package, files_to_copy, docker_images_to_copy = rebuild_model_package(
        src_model_package, dst_group_name, dst_s3_path, dst_ecr
    )

    logger.debug(dst_model_package)
    logger.debug(files_to_copy)
    logger.debug(docker_images_to_copy)

    copy_files(files_to_copy, src_session, dst_session)
    copy_docker_images(docker_images_to_copy, docker_client)

    response = dst_sm.create_model_package(**dst_model_package)
    print("Model copy completed.")
    logger.debug(response)
    return response.get("ModelPackageArn")


def rebuild_model_package(src_model_package: dict, dst_group_name: str, dst_s3_path: str, dst_ecr: str):
    dont_copy_keys = [
        'ModelPackageName', 'ModelPackageGroupName',
        'ModelPackageVersion', 'ModelPackageArn', 'CreationTime', 'ModelPackageStatus', 'ModelPackageStatusDetails',
        'CreatedBy', 'LastModifiedTime', 'LastModifiedBy', 'ApprovalDescription', 'ResponseMetadata']

    dst_model_package = {}
    for k, v in src_model_package.items():
        if k not in dont_copy_keys:
            dst_model_package[k] = v

    # dst_model_package['ModelPackageName'] = dst_name      # gives error: botocore.exceptions.ClientError: An error occurred (ValidationException) when calling the CreateModelPackage operation: 1 validation errors detected:Environment variable map cannot be specified when using non-versioned ModelPackages
    dst_model_package['ModelPackageGroupName'] = dst_group_name

    files_to_copy = []
    docker_images_to_copy = []
    for container in dst_model_package.get("InferenceSpecification").get("Containers"):
        # copy docker image
        p: tuple = prepare_docker_urls(container.get("Image"), dst_ecr)
        docker_images_to_copy.append(p)
        container["Image"] = p[1]

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
    src_repository, src_tag = src_uri.split(":")
    if "/" in src_repository:
        src_image = src_repository.split("/")[1]
    else:
        src_image = src_repository

    dst_tag = f"{src_image}-{src_tag}"

    return src_uri, f"{dst_ecr}:{dst_tag}"


def copy_files(
        files_to_copy: list,
        src_session: boto3.session.Session,
        dst_session: boto3.session.Session
    ):
    logger = logging.getLogger(__name__)
    with tempfile.TemporaryDirectory() as temp_dir:
        src_s3 = src_session.client('s3')
        dst_s3 = dst_session.client('s3')
        for src, dst in files_to_copy:
            src_tuple = parse_s3_url(src)
            dst_tuple = parse_s3_url(dst)
            filename = os.path.basename(src)
            temp_file = os.path.join(temp_dir, filename)

            logger.debug(f"Downloading {src} to temp file {temp_file}")
            src_s3.download_file(src_tuple[0], src_tuple[1], temp_file)

            logger.debug(f"Uploading {dst}")
            dst_s3.upload_file(temp_file, dst_tuple[0], dst_tuple[1])

            logger.debug(f"Deleting {temp_file}")
            os.remove(temp_file)


def copy_docker_images(images_to_copy: list, docker_client: docker.client.DockerClient):
    logger = logging.getLogger(__name__)
    for src, dst in images_to_copy:
        src_repository, src_tag = src.split(":")
        dst_repository, dst_tag = dst.split(":")

        logger.debug(f"Pulling image {src_repository}:{src_tag}")
        image = docker_client.images.pull(repository=src_repository, tag=src_tag)

        logger.debug(f"Tagging image {src_repository}:{src_tag} with {dst_repository}:{dst_tag}")
        image.tag(repository=dst_repository, tag=dst_tag)

        logger.debug(f"Pushing image {dst_repository}:{dst_tag}")

        prev_ts = time.time() - 10
        for line in docker_client.api.push(repository=dst_repository, tag=dst_tag, stream=True, decode=True):
            ts = time.time()
            if ts - prev_ts > 10:
                prev_ts = ts
                logger.debug(line)


def list_docker_images_in_model_package(model_package_arn: str, session: boto3.session.Session = boto3.session.Session()):
    sm = session.client('sagemaker')
    src_model_package = sm.describe_model_package(ModelPackageName=model_package_arn)

    return [container.get("Image") for container in src_model_package.get("InferenceSpecification").get("Containers")]

