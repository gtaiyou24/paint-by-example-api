from PIL.Image import Image
from injector import inject

from domain.model.image import ImageStorageService
from port.adapter.service.image.adapter import ImageStorageAdapter


class ImageStorageServiceImpl(ImageStorageService):
    @inject
    def __init__(self, image_storage_adapter: ImageStorageAdapter):
        self.__image_storage_adapter = image_storage_adapter

    def upload(self, image: Image) -> str:
        return self.__image_storage_adapter.upload(image)
