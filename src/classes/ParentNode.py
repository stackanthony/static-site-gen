from src.classes.HTMLNode import HTMLNode
from typing import Optional


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: Optional[str] = None,
        children: Optional[list[HTMLNode]] = None,
        props: Optional[dict[str, str]] = None,
    ):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError('No tags provided')
        if not self.children:
            raise ValueError('No children provided')

        s: list[str] = []

        if self.props:
            s.append(f'<{self.tag} {self.props_to_html()}>')
        else:
            s.append(f'<{self.tag}>')

        for child in self.children:
            s.append(child.to_html())

        s.append(f'</{self.tag}>')

        return ''.join(s)
