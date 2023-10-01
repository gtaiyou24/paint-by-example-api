import uuid

from PIL.Image import Image
from slf4py import set_logger

from port.adapter.service.image.adapter import ImageStorageAdapter


@set_logger
class ImageStorageAdapterStub(ImageStorageAdapter):
    def upload(self, image: Image) -> str:
        return f'https://localhost:8000/images/{uuid.uuid4()}.{image.format.lower()}'
