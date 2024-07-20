from src.classes.Block import Block
from src.classes.blocks.Code import Code
from src.classes.blocks.Heading import Heading
from src.classes.blocks.OrderedList import OrderedList
from src.classes.blocks.Quote import Quote
from src.classes.blocks.UnorderedList import UnorderedList

class BlockFactory:
    
    @staticmethod
    def create_blocks(markdown: str) -> list[Block]:
        blocks: list[Block] = Block.markdown_to_blocks(markdown)
        processed_blocks: list[Block] = []

        for block in blocks:
            if Heading.is_heading(block):
                processed_blocks.append(Heading(block.text))
            elif Code.is_code(block):
                processed_blocks.append(Code(block.text))
            elif Quote.is_quote(block):
                processed_blocks.append(Quote(block.text))
            elif UnorderedList.is_ulist(block):
                processed_blocks.append(UnorderedList(block.text))
            elif OrderedList.is_olist(block):
                processed_blocks.append(OrderedList(block.text))
            else:
                processed_blocks.append(block)


        return processed_blocks
