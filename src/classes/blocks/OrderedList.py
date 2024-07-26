from typing import Optional
from src.classes.Block import Block


class OrderedList(Block):
    def __init__(self, text: str, items: Optional[list[str]] = None) -> None:
        super().__init__(text)
        self.items = items if items else []

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

    @staticmethod
    def build_list_items(block_text: str) -> list[str]:
        items: list[str] = []

        split_block_lines: list[str] = block_text.split("\n")

        for line in split_block_lines:
            split_line: list[str] = line.split(". ", maxsplit=1)

            if len(split_line) < 2:
                raise ValueError

            items.append(split_line[1])
            
        return items
        
    def build(self) -> Block:
        ordered_list_items: list[str] = OrderedList.build_list_items(self.text)

        return OrderedList(self.text, ordered_list_items)
