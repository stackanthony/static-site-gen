from src.classes.HTMLNode import HTMLNode
from typing import Optional

class LeafNode(HTMLNode):
    def __init__(self, tag: Optional[str] = None, value: str = "", props: Optional[dict[str, str | bool | int]] = None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError

        if not self.tag:
            return self.value

        return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"

