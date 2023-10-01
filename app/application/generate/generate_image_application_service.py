from injector import singleton

from application.generate.command import PaintByExampleCommand


@singleton
class GenerateImageApplicationService:
    def paint_by_example(self, command: PaintByExampleCommand) -> str:
        pass
