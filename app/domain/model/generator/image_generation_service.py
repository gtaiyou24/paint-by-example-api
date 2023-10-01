import abc

import PIL.Image


class ImageGenerationService(abc.ABC):
    def paint_by_example(self, origin: PIL.Image.Image, mask: PIL.Image.Image, reference: PIL.Image.Image) -> PIL.Image.Image:
        pass
