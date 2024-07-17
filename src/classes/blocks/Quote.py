from src.classes.Block import Block


class Quote(Block):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.start_delimeter = ">"

    @staticmethod
    def is_quote(block: Block) -> bool:
        split_quote_text: list[str] = block.text.split("\n")

        for quote in split_quote_text:
            if quote[0] != ">":
                return False
        
        return True
