class Block:
    def __init__(self, text: str) -> None:
        self.text = text

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, Block):
            return NotImplemented
        return self.text == other.text

    @staticmethod
    def markdown_to_blocks(markdown: str) -> list['Block']:
        blocks: list['Block'] = []
        split_text: list[str] = markdown.split("\n\n")

        for text in split_text:
            if text == "":
                continue
            blocks.append(Block(text.strip()))

        return blocks
