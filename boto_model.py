import os
import logging
import boto3
from botocore.exceptions import ClientError

# TODO: cleanup for DO conversion


def upload_file(file_name, bucket, object_name=None, ExtraArgs={'ACL': 'public-read'}):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    boto_session = boto3.session.Session()
    boto_client = boto_session.client('s3',
                                      region_name='sfo2',
                                      endpoint_url=os.environ['BASE_URL'],
                                      aws_access_key_id=os.environ['DO_ACCESS_KEY_ID'],
                                      aws_secret_access_key=os.environ['DO_SECRET_ACCESS_KEY'])

    try:
        boto_client.upload_fileobj(
            file_name,
            os.environ['BUCKET'],
            object_name,
            ExtraArgs={
                "ContentType": "image/png"
            })
        boto_client.put_object_acl(
            ACL='public-read', Bucket=os.environ['BUCKET'], Key=object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
