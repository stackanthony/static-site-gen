from src.classes.Block import Block
from src.classes.HTMLNode import HTMLNode
from src.classes.LeafNode import LeafNode
from src.classes.ParentNode import ParentNode
from src.classes.TextNode import TextNode
from src.classes.blocks.BlockFactory import BlockFactory
from src.classes.blocks.Code import Code
from src.classes.blocks.Heading import Heading
from src.classes.blocks.OrderedList import OrderedList
from src.classes.blocks.UnorderedList import UnorderedList
from src.classes.blocks.Quote import Quote


class MarkdownProcessor:
    def __init__(self, markdown: str):
        self.markdown = markdown

    def markdown_to_html_node(self) -> HTMLNode:
        blocks: list[Block] = BlockFactory.create_blocks(self.markdown)
        root_node: ParentNode = ParentNode("div")

        for block in blocks:
            new_node: ParentNode | None = None
            if isinstance(block, Heading):
                new_node = ParentNode(f"h{block.count}", children=[
                    TextNode(block.text, "text").text_node_to_html_node()
                ])
                root_node.children.append(new_node)
            elif isinstance(block, Code):
                new_node = ParentNode("pre", children=[
                    TextNode(block.text, "code").text_node_to_html_node()
                ])
                root_node.children.append(new_node)
            elif isinstance(block, Quote):
                new_node = ParentNode("blockquote", children=[
                    TextNode(block.text, "text").text_node_to_html_node()
                ])
                root_node.children.append(new_node)
            elif isinstance(block, UnorderedList):
                root_list_node = ParentNode("ul")

                for item in block.items:
                    child_list_node = LeafNode("li", item)
                    root_list_node.children.append(child_list_node)

                root_node.children.append(root_list_node)
            elif isinstance(block, OrderedList):
                root_list_node = ParentNode("ol")

                for item in block.items:
                    child_list_node = LeafNode("li", item)
                    root_list_node.children.append(child_list_node)

                root_node.children.append(root_list_node)
            else:
                new_node = ParentNode("p", children=[
                    TextNode(block.text, "text").text_node_to_html_node()
                ])

                root_node.children.append(new_node)

        return root_node
