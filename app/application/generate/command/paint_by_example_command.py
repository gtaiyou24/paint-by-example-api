import base64
import io

import PIL.Image
import requests


class PaintByExampleCommand:
    def __init__(self, origin: str, mask: str, reference: str):
        self.__origin = origin
        self.__mask = mask
        self.__reference = reference

    @property
    def origin(self) -> PIL.Image.Image:
        return self.__image_from(self.__origin)

    @property
    def mask(self) -> PIL.Image.Image:
        return self.__image_from(self.__mask)

    @property
    def reference(self) -> PIL.Image.Image:
        return self.__image_from(self.__reference)

    def __image_from(self, source: str) -> PIL.Image.Image:
        if 'base64,' in source:
            image_data = source.split(',')[1]
            image = io.BytesIO(base64.b64decode(image_data))
        else:
            image = requests.get(source, stream=True).raw
        return PIL.Image.open(image)
