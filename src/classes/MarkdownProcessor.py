from src.classes.Block import Block
from src.classes.HTMLNode import HTMLNode
from src.classes.TextNode import TextNode
from src.classes.blocks.BlockFactory import BlockFactory
from src.classes.blocks.Code import Code
from src.classes.blocks.Heading import Heading
from src.classes.blocks.OrderedList import OrderedList


class MarkdownProcessor:
    def __init__(self, markdown: str):
        self.markdown = markdown

    def markdown_to_html_node(self):
        blocks: list[Block] = BlockFactory.create_blocks(self.markdown)
        root_node: HTMLNode = HTMLNode("div")

        for block in blocks:
            if isinstance(block, Heading):
                new_node = HTMLNode(f"h{block.count}", children=[
                    TextNode(block.text, "text").text_node_to_html_node()
                ])
                root_node.children.append(new_node)
            elif isinstance(block, Code):
                new_node = HTMLNode("pre", children=[
                    TextNode(block.text, "code").text_node_to_html_node()
                ])
                root_node.children.append(new_node)
            # elif isinstance(block, OrderedList):


        return root_node
