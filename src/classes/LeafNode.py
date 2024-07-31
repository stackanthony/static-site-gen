from src.classes.HTMLNode import HTMLNode
from typing import Optional


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: Optional[str] = None,
        value: str = '',
        props: Optional[dict[str, str]] = None,
    ):
        super().__init__(tag, value, props=props)

    def __str__(self) -> str:
        return f'Tag: {self.tag}\nValue: [{self.value}]\nProps: {self.props}\n'

    def to_html(self) -> str:
        if not self.value and self.tag != 'img':
            raise ValueError

        if not self.tag or self.tag == 'text':
            return self.value if self.value else ''

        if not self.props:
            return f'<{self.tag}>{self.value}</{self.tag}>'

        return (
            f'<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>'
        )
