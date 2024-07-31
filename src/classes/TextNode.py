from typing import Optional

from src.classes.LeafNode import LeafNode
from src.classes.TextProcessor import TextProcessor


class TextNode:
    def __init__(
        self, text: str = '', text_type: str = '', url: Optional[str] = None
    ) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, TextNode):
            return NotImplemented
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f'TextNode({self.text}, {self.text_type}, {self.url})'

    def text_node_to_html_node(self) -> LeafNode:
        match self.text_type:
            case 'text':
                return LeafNode('text', self.text)
            case 'bold':
                return LeafNode('b', self.text)
            case 'italic':
                return LeafNode('i', self.text)
            case 'code':
                return LeafNode('code', self.text)
            case 'link':
                if not self.url:
                    raise ValueError('No URL to parse')
                return LeafNode('a', self.text, {'href': self.url})
            case 'image':
                if not self.url:
                    raise ValueError('No Image URL in Node')
                return LeafNode('img', '', {'src': self.url})
            case _:
                raise Exception(
                    "Not a valid text type. Couldn't convert to LeafNode"
                )

    @staticmethod
    def text_to_textnodes(text: str) -> list['TextNode']:
        if text == '':
            return []

        text_nodes: list['TextNode'] = [TextNode(text, 'text')]
        try:
            for bold_node in TextNode.split_nodes_delimiter(
                [text_nodes.pop()], '**', 'bold'
            ):
                text_nodes.append(bold_node)

            for italic_node in TextNode.split_nodes_delimiter(
                [text_nodes.pop()], '*', 'italic'
            ):
                text_nodes.append(italic_node)

            for code_node in TextNode.split_nodes_delimiter(
                [text_nodes.pop()], '`', 'code'
            ):
                text_nodes.append(code_node)

            for image_node in TextNode.split_nodes_image([text_nodes.pop()]):
                text_nodes.append(image_node)

            for link_node in TextNode.split_nodes_link([text_nodes.pop()]):
                text_nodes.append(link_node)
        except:
            pass

        return text_nodes

    @staticmethod
    def split_nodes_delimiter(
        old_nodes: list['TextNode'], delimeter: str, text_type: str
    ) -> list['TextNode']:
        new_nodes: list['TextNode'] = []
        text_types: dict[str, str] = {
            'bold': '**',
            'italic': '*',
            'code': '`',
        }

        if text_type not in text_types:
            raise ValueError(f'{text_type} - not a valid text type to convert')

        if delimeter not in text_types.values():
            raise ValueError(f'{delimeter} - not a valid delimeter to convert')

        for node in old_nodes:
            split_nodes_text: list[str] = node.text.split(delimeter)

            if len(split_nodes_text) > 2:
                # valid delimeter enclosed word
                for i, split_node_text in enumerate(split_nodes_text):
                    if not split_node_text:
                        continue
                    new_node = TextNode(split_node_text)
                    new_node.text_type = 'text' if i % 2 == 0 else text_type
                    new_nodes.append(new_node)

        if not new_nodes:
            new_nodes.append(old_nodes[0])

        return new_nodes

    @staticmethod
    def split_nodes_image(old_nodes: list['TextNode']) -> list['TextNode']:
        new_nodes: list['TextNode'] = []

        for node in old_nodes:
            if TextProcessor(node.text).extract_markdown_images():
                split_nodes_text = node.text.split('!')

                for split_node_text in split_nodes_text:
                    try:
                        if split_node_text == '':
                            continue

                        tp = TextProcessor('!' + split_node_text)
                        extract_markdown_images = tp.extract_markdown_images()

                        if not extract_markdown_images:
                            new_nodes.append(TextNode(split_node_text, 'text'))
                            continue

                        new_nodes.append(
                            TextNode(
                                extract_markdown_images[0][0],
                                'image',
                                extract_markdown_images[0][1],
                            )
                        )

                        trailing_text = tp.get_trailing_text(')')

                        if not trailing_text:
                            continue

                        new_nodes.append(TextNode(trailing_text, 'text'))
                    except:
                        continue
            else:
                new_nodes.append(node)

        return new_nodes

    @staticmethod
    def split_nodes_link(old_nodes: list['TextNode']) -> list['TextNode']:
        new_nodes: list['TextNode'] = []

        for node in old_nodes:
            try:
                tp = TextProcessor(node.text)
                if not tp.extract_markdown_links():
                    # doesn't contain link
                    new_nodes.append(node)
                    continue

                split_nodes_text = node.text.split('[')

                for split_node_text in split_nodes_text:

                    tp = TextProcessor('[' + split_node_text)
                    extract_markdown_links = tp.extract_markdown_links()

                    if not extract_markdown_links:
                        new_nodes.append(TextNode(split_node_text, 'text'))
                        continue

                    new_nodes.append(
                        TextNode(
                            extract_markdown_links[0][0],
                            'link',
                            extract_markdown_links[0][1],
                        )
                    )

                    trailing_text = tp.get_trailing_text(')')

                    if not trailing_text:
                        continue

                    new_nodes.append(TextNode(trailing_text, 'text'))
            except:
                continue

        return new_nodes
