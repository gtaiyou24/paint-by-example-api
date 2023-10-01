import abc

import PIL.Image


class ImageGeneratorAdapter(abc.ABC):
    @abc.abstractmethod
    def paint_by_example(self, origin: PIL.Image.Image, mask: PIL.Image.Image, reference: PIL.Image.Image) -> PIL.Image.Image:
        pass
