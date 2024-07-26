from typing import Optional
from src.classes.Block import Block


class Heading(Block):
    def __init__(self, text: str, count: Optional[int] = 0) -> None:
        super().__init__(text)
        self.count = count

    @staticmethod
    def is_heading(block: Block) -> bool:
        hash_count = block.text.split()[0].count("#")
        return hash_count <= 6 and hash_count >= 1 and block.text.count("# ") == 1

    def build(self) -> Block:
        split_block_text: list[str] = self.text.split(" ", maxsplit=1)

        if len(split_block_text) < 2:
            raise ValueError

        text = split_block_text[1]
        count = len(split_block_text[0])

        return Heading(text, count)
