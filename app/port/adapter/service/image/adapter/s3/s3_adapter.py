import io
import urllib
import uuid

import boto3
from PIL.Image import Image
from slf4py import set_logger

from port.adapter.service.image.adapter import ImageStorageAdapter


@set_logger
class S3Adapter(ImageStorageAdapter):
    def __init__(self, bucket: str, cdn_hostname: str, region: str):
        self.__bucket = bucket
        self.__cdn_hostname = cdn_hostname
        self.__s3_client = boto3.client('s3', region_name=region)

    def upload(self, image: Image) -> str:
        _format = f'{image.format.lower()}'

        memory = io.BytesIO()
        image.save(memory, format=_format)
        memory.seek(0)

        path = f'tmp/mask/{str(uuid.uuid4())}.{_format}'
        self.__s3_client.put_object(
            Bucket=self.__bucket,
            Key=path,
            Body=memory,
            ContentType=f'image/{_format}',
            Tagging=f'lifecycle=6h'
        )

        return urllib.parse.urljoin(self.__cdn_hostname, path)
