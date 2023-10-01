import PIL.Image
from injector import inject

from domain.model.generator import ImageGenerationService
from port.adapter.service.generator.adapter import ImageGeneratorAdapter


class ImageGenerationServiceImpl(ImageGenerationService):
    @inject
    def __init__(self, image_generator_adapter: ImageGeneratorAdapter):
        self.__image_generator_adapter = image_generator_adapter

    def paint_by_example(self, origin: PIL.Image.Image, mask: PIL.Image.Image, reference: PIL.Image.Image) -> PIL.Image.Image:
        return self.__image_generator_adapter.paint_by_example(origin, mask, reference)
