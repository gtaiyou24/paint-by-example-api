import abc

from PIL.Image import Image


class ImageStorageService(abc.ABC):
    @abc.abstractmethod
    def upload(self, image: Image) -> str:
        pass
