import PIL.Image
from injector import singleton, inject

from application.generate.command import PaintByExampleCommand
from domain.model.generator import ImageGenerationService


@singleton
class GenerateImageApplicationService:
    @inject
    def __init__(self, image_generation_service: ImageGenerationService):
        self.__image_generation_service = image_generation_service

    def paint_by_example(self, command: PaintByExampleCommand) -> PIL.Image.Image:
        return self.__image_generation_service.paint_by_example(command.origin, command.mask, command.reference)
