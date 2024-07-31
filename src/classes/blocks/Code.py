from src.classes.Block import Block


class Code(Block):
    def __init__(self, text: str) -> None:
        super().__init__(text)

    @staticmethod
    def is_code(block: Block) -> bool:
        split_block_text: list[str] = block.text.split('```')

        return split_block_text[0] == '' and split_block_text[-1] == ''

    def build(self) -> Block:
        split_block_text: list[str] = self.text.split('```')

        if len(split_block_text) < 2:
            raise ValueError

        return Code(split_block_text[1])
