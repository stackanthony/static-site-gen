from typing import Optional, Text

from src.classes.LeafNode import LeafNode
from src.classes.TextProcessor import TextProcessor

class TextNode:
    def __init__(self, text: str="", text_type: str="", url: Optional[str] = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, TextNode):
            return NotImplemented
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self) -> LeafNode:
        match self.text_type:
            case "text":
                return LeafNode(value=self.text)
            case "bold":
                return LeafNode("b", self.text)
            case "italic":
                return LeafNode("i", self.text)
            case "code":
                return LeafNode("code", self.text)
            case "link":
                if not self.url:
                    raise ValueError("No URL to parse")
                return LeafNode("a", self.text, {"href": self.url})
            case "image":
                if not self.url:
                    raise ValueError("No Image URL in Node")
                return LeafNode("img", "", {"src": self.url})
            case _:
                raise Exception("Not a valid text type. Couldn't convert to LeafNode")

    @staticmethod
    def split_nodes_delimiter(old_nodes: list['TextNode'], delimeter: str, text_type: str) -> list['TextNode']:
        new_nodes: list['TextNode'] = []
        text_types: dict[str, str] = {
            "bold" : "**",
            "italic": "*",
            "code": "`",
        }

        if text_type not in text_types: 
            raise ValueError(f"{text_type} - not a valid text type to convert")

        if delimeter not in text_types.values():
            raise ValueError(f"{delimeter} - not a valid delimeter to convert")

        for node in old_nodes:
            split_nodes_text: list[str] = node.text.split(delimeter)

            if len(split_nodes_text) > 2:
                # valid delimeter enclosed word
                
                for i, split_node_text in enumerate(split_nodes_text):
                    node = TextNode(split_node_text)
                    node.text_type = "text" if i % 2 == 0 else text_type
                    new_nodes.append(node)

        if not new_nodes:
            raise Exception("No valid delimeters to split / not properly enclosed")

        return new_nodes
    
    @staticmethod
    def split_nodes_image(old_nodes: list['TextNode']) -> list['TextNode']:
        new_nodes: list['TextNode'] = []

        for node in old_nodes:
            tp = TextProcessor(node.text)
            images = tp.extract_markdown_images()
            print(images)
            # split_nodes_text: list[str] = node.text.split("!")
            #
            # for split_node_text in split_nodes_text:
            #     tp = TextProcessor(split_node_text)
            #     images = tp.extract_markdown_images()
            #     print(images)




