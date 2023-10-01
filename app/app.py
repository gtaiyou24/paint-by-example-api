import os
from contextlib import asynccontextmanager

from di import DIContainer, DI
from fastapi import FastAPI

from domain.model.generator import ImageGenerationService
from domain.model.image import ImageStorageService
from port.adapter.resource.generate import generate_resource
from port.adapter.resource.health import health_resource
from port.adapter.resource.image import image_resource
from port.adapter.service.generator import ImageGenerationServiceImpl
from port.adapter.service.generator.adapter import ImageGeneratorAdapter
from port.adapter.service.generator.adapter.sagemaker import SageMakerAdapter
from port.adapter.service.image import ImageStorageServiceImpl
from port.adapter.service.image.adapter import ImageStorageAdapter
from port.adapter.service.image.adapter.s3 import S3Adapter
from port.adapter.standalone.adapterstub import ImageStorageAdapterStub


@asynccontextmanager
async def lifespan(app: FastAPI):
    di_list = (
        DI.of(ImageGenerationService, {}, ImageGenerationServiceImpl),
        DI.of(ImageGeneratorAdapter, {}, SageMakerAdapter(os.getenv('AWS_SAGEMAKER_ENDPOINT', 'image-generator'))),
        DI.of(ImageStorageService, {}, ImageStorageServiceImpl),
        DI.of(ImageStorageAdapter,
              {'Stub': ImageStorageAdapterStub},
              S3Adapter(os.getenv('AWS_S3_BUCKET'), os.getenv('AWS_CLOUDFRONT_HOSTNAME'), os.getenv('AWS_REGION'))),
    )
    for di in di_list:
        DIContainer.instance().register(di)
    yield
    app.clip = None


app = FastAPI(title='Paint By Example API', openapi_prefix=os.getenv('OPENAPI_PREFIX'), lifespan=lifespan)

app.include_router(generate_resource.router)
app.include_router(health_resource.router)
app.include_router(image_resource.router)
