from __future__ import annotations

import base64
import io

import PIL.Image
from pydantic import BaseModel, Field


class PaintByExampleJson(BaseModel):
    image: str = Field(title='生成された画像')

    @staticmethod
    def of(image: PIL.Image.Image) -> PaintByExampleJson:
        buffer = io.BytesIO()
        image.save(buffer, image.format.lower())
        binary = f'data:image/{image.format.lower()};base64,{base64.b64encode(buffer.getvalue()).decode("ascii")}'
        return PaintByExampleJson(image=binary)

