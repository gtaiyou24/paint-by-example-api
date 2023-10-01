import abc


class ImageGenerationService(abc.ABC):
    def generate(self) -> str:
        pass
