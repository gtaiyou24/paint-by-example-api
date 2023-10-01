from pydantic import BaseModel, Field


class PaintByExampleRequest(BaseModel):
    origin: str = Field(title="オリジナル画像")
    mask: str = Field(title="マスキング画像")
    reference: str = Field(title="参照画像")
