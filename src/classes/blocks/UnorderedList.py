from src.classes.Block import Block


class UnorderedList(Block):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.start_delimeter = {"*", "-"}

    @staticmethod
    def is_ulist(block: Block) -> bool:
        split_block_text: list[str] = block.text.split("\n")

        for line in split_block_text:
            if (line[0] == "*" or line[0] == "-") and line[1] == " ":
                continue

            return False

        return True

    @staticmethod
    def build_list_items(block_text: str) -> str:
        s = ""

        split_block_lines = block_text.split("\n")

        for line in split_block_lines:
            split_line = line.split(" ", maxsplit=1)
            if split_line[0] != "*" and split_line[0] != "-":
                continue
            s += split_line[1] + "\n"

        return s
