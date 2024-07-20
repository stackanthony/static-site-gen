from src.classes.Block import Block


class OrderedList(Block):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.start_delimeter = "."

    @staticmethod
    def is_olist(block: Block) -> bool:
        split_block_text: list[str] = block.text.split("\n")
        numbers: list[int] = []

        # check number is valid and add to list
        for line in split_block_text:
            try:
                split_line = line.split(". ")
                number: int = int(split_line[0])
                numbers.append(number)

                if len(split_line) <= 1:
                    return False

            except ValueError:
                return False

        if not OrderedList._is_incremental(numbers):
            return False

        return True

    @staticmethod
    def _is_incremental(numbers: list[int]) -> bool:
        return numbers == list(range(numbers[0], numbers[0] + len(numbers)))
