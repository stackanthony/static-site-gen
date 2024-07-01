from typing import Optional

from src.classes.LeafNode import LeafNode

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

    def split


