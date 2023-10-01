import base64
import io
import os
import zipfile

import PIL.Image
import boto3
import botocore
from sagemaker import Predictor, Session
from sagemaker.deserializers import StreamDeserializer
from sagemaker.serializers import JSONSerializer

from port.adapter.service.generator.adapter import ImageGeneratorAdapter


class SageMakerAdapter(ImageGeneratorAdapter):
    def __init__(self, endpoint_name: str):
        session = Session(boto_session=boto3.Session(profile_name=os.getenv("AWS_PROFILE"), region_name='ap-northeast-1'))
        self.__predictor = Predictor(
            endpoint_name=endpoint_name,
            sagemaker_session=session,
            serializer=JSONSerializer(),
            deserializer=StreamDeserializer(),
        )

    def paint_by_example(self, origin: PIL.Image.Image, mask: PIL.Image.Image, reference: PIL.Image.Image) -> PIL.Image.Image:
        response = self.__predictor.predict({
            "origin": self.__to_base64_from(origin),
            "mask": self.__to_base64_from(mask),
            "reference": self.__to_base64_from(reference)
        })
        streaming_body: botocore.response.StreamingBody = response[0]

        zf = zipfile.ZipFile(io.BytesIO(streaming_body.read()), "r")
        for i, fileinfo in enumerate(zf.infolist()):
            return PIL.Image.open(zf.open(fileinfo.filename))

    def __to_base64_from(self, image: PIL.Image.Image) -> str:
        buffered = io.BytesIO()
        image.save(buffered, format=f"{image.format.lower()}")
        img_base64 = base64.b64encode(buffered.getvalue()).decode("ascii")
        return f"data:image/{image.format.lower()};base64,{img_base64}"
