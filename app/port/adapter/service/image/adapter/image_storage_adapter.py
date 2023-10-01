import abc

from PIL.Image import Image


class ImageStorageAdapter(abc.ABC):
    @abc.abstractmethod
    def upload(self, image: Image) -> str:
        pass
