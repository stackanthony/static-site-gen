from src.classes.HTMLNode import HTMLNode
from typing import Optional

class LeafNode(HTMLNode):
    def __init__(self, tag: Optional[str] = None, value: Optional[str] = None, props: Optional[dict[str, str]] = None):
        super().__init__(tag, value, props=props)

    def to_html(self) -> str:
        if not self.value and self.tag != "img":
            raise ValueError

        if not self.tag or self.tag == "text":
            return self.value if self.value else ""

        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"

