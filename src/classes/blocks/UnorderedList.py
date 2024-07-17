from src.classes.Block import Block


class UnorderedList(Block):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.start_delimeter = {"*", "-"}
