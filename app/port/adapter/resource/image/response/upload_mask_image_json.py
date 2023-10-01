from __future__ import annotations

from pydantic import Field, BaseModel


class UploadMaskImageJson(BaseModel):
    image_url: str = Field(title='アップロードされた画像のURL')

    @staticmethod
    def of(image_url: str) -> UploadMaskImageJson:
        return UploadMaskImageJson(image_url=image_url)
