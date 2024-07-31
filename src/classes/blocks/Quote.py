from src.classes.Block import Block


class Quote(Block):
    def __init__(self, text: str) -> None:
        super().__init__(text)

    @staticmethod
    def is_quote(block: Block) -> bool:
        split_quote_text: list[str] = block.text.split('\n')

        for quote in split_quote_text:
            if quote[0] != '>':
                return False

        return True

    @staticmethod
    def parse_quote_items(block_text: str) -> str:
        s = ''

        split_block_lines = block_text.split('\n')

        for line in split_block_lines:
            split_line = line.split(' ', maxsplit=1)
            if split_line[0] != '>':
                continue
            s += split_line[1] + '\n'

        return s[:-1]

    def build(self) -> Block:
        quote_items_str = Quote.parse_quote_items(self.text)

        return Quote(quote_items_str)
