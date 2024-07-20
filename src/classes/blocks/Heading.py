from src.classes.Block import Block


class Heading(Block):
    def __init__(self, text: str, count: int) -> None:
        super().__init__(text)
        self.start_delimeter = "#"
        self.count = count

    @staticmethod
    def is_heading(block: Block) -> bool:
        hash_count = block.text.split()[0].count("#")
        return hash_count <= 6 and hash_count >= 1 and block.text.count("# ") == 1
