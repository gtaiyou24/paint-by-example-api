from di import DIContainer
from fastapi import APIRouter

from application.generate import GenerateImageApplicationService
from application.generate.command import PaintByExampleCommand
from port.adapter.resource.generate.request import PaintByExampleRequest
from port.adapter.resource.generate.response import PaintByExampleJson

router = APIRouter(
    prefix="/generate",
    tags=["画像生成"]
)


@router.post("/paint-by-example", name="Paint By Example", response_model=PaintByExampleJson)
def generate(request: PaintByExampleRequest) -> PaintByExampleJson:
    application_service = DIContainer.instance().resolve(GenerateImageApplicationService)

    command = PaintByExampleCommand(origin=request.origin, mask=request.mask, reference=request.reference)
    image = application_service.paint_by_example(command)

    return PaintByExampleJson.of(image)
