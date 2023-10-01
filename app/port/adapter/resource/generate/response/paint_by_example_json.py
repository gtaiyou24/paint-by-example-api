from __future__ import annotations

from pydantic import BaseModel, Field


class PaintByExampleJson(BaseModel):
    image_url: str = Field(title='生成された画像のURL')

    @staticmethod
    def of(image_url: str) -> PaintByExampleJson:
        return PaintByExampleJson(image_url=image_url)
