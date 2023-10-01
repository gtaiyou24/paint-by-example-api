import base64
import io

import PIL.Image
import requests
from pydantic import BaseModel, Field


class UploadMaskImageRequest(BaseModel):
    mask_image: str = Field(title='マスキング画像')

    def image_binary(self) -> PIL.Image.Image:
        if 'base64,' in self.mask_image:
            image_data = self.mask_image.split(',')[1]
            image = io.BytesIO(base64.b64decode(image_data))
        else:
            image = requests.get(self.mask_image, stream=True).raw
        return PIL.Image.open(image)
