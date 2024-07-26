from src.classes.Block import Block


class Paragraph(Block):
    def __init__(self, text: str) -> None:
        super().__init__(text)
