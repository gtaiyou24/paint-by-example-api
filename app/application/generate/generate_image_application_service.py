from injector import singleton

from application.generate.command import PaintByExampleCommand


@singleton
class GenerateImageApplicationService:
    def paint_by_example(self, command: PaintByExampleCommand) -> str:
        return 'https://fujifilm-x.com/wp-content/uploads/2021/01/gfx100s_sample_04_thum-1.jpg'
