from PIL.Image import Image
from injector import singleton, inject

from domain.model.image import ImageStorageService


@singleton
class ImageApplicationService:
    @inject
    def __init__(self, image_storage_service: ImageStorageService):
        self.__image_storage_service = image_storage_service

    def upload_mask(self, mask_image: Image) -> str:
        return self.__image_storage_service.upload(mask_image)
