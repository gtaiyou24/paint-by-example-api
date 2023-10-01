from di import DIContainer
from fastapi import APIRouter

from application.image import ImageApplicationService
from port.adapter.resource.image.request import UploadMaskImageRequest
from port.adapter.resource.image.response import UploadMaskImageJson

router = APIRouter(
    prefix="/images",
    tags=["画像アップロード"]
)


@router.post("/mask", name="マスキング画像のアップロード", response_model=UploadMaskImageJson)
def upload_mask(request: UploadMaskImageRequest) -> UploadMaskImageJson:
    application_service = DIContainer.instance().resolve(ImageApplicationService)
    image_url = application_service.upload_mask(request.image_binary())
    return UploadMaskImageJson.of(image_url)
