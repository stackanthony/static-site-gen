from src.classes.Block import Block
from src.classes.HTMLNode import HTMLNode
from src.classes.ParentNode import ParentNode
from src.classes.TextNode import TextNode
from src.classes.blocks.BlockFactory import BlockFactory
from src.classes.blocks.Code import Code
from src.classes.blocks.Heading import Heading
from src.classes.blocks.OrderedList import OrderedList
from src.classes.blocks.Paragraph import Paragraph
from src.classes.blocks.UnorderedList import UnorderedList
from src.classes.blocks.Quote import Quote


class MarkdownProcessor:
    def __init__(self, markdown: str):
        self.markdown = markdown

    def markdown_to_html_node(self) -> HTMLNode:
        blocks: list[Block] = BlockFactory.create_blocks(self.markdown)
        root_node: ParentNode = ParentNode('div')

        for block in blocks:
            new_node: ParentNode | None = None
            block.text = block.text.strip()

            if isinstance(block, Heading):
                new_node = ParentNode(f'h{block.count}')
                new_node.children = [
                    text_node.text_node_to_html_node()
                    for text_node in TextNode.text_to_textnodes(block.text)
                ]
                root_node.children.append(new_node)
            elif isinstance(block, Code):
                new_node = ParentNode(
                    'pre',
                    children=[
                        TextNode(block.text, 'code').text_node_to_html_node()
                    ],
                )
                root_node.children.append(new_node)
            elif isinstance(block, Quote):
                new_node = ParentNode('blockquote')
                new_node.children = [
                    text_node.text_node_to_html_node()
                    for text_node in TextNode.text_to_textnodes(block.text)
                ]
                root_node.children.append(new_node)
            elif isinstance(block, UnorderedList):
                root_list_node = ParentNode('ul')

                for item in block.items:
                    child_list_node = ParentNode('li')

                    child_list_node.children = [
                        text_node.text_node_to_html_node()
                        for text_node in TextNode.text_to_textnodes(item)
                    ]
                    root_list_node.children.append(child_list_node)

                root_node.children.append(root_list_node)
            elif isinstance(block, OrderedList):
                root_list_node = ParentNode('ol')

                for item in block.items:
                    child_list_node = ParentNode('li')

                    child_list_node.children = [
                        text_node.text_node_to_html_node()
                        for text_node in TextNode.text_to_textnodes(item)
                    ]

                    root_list_node.children.append(child_list_node)

                root_node.children.append(root_list_node)
            elif isinstance(block, Paragraph):
                new_node = ParentNode('p')
                for text_node in TextNode.text_to_textnodes(block.text):
                    if text_node.text == '':
                        continue
                    new_node.children.append(
                        text_node.text_node_to_html_node()
                    )
                root_node.children.append(new_node)

        return root_node
