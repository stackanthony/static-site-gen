from src.classes.Block import Block


class OrderedList(Block):
    def __init__(self, text: str, order: str) -> None:
        super().__init__(text)
        self.order = order
        self.start_delimeter = "."
