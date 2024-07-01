from typing import Optional

class HTMLNode:
    def __init__(self, tag: Optional[str] = None, value: Optional[str] = None, children: list['HTMLNode'] | None = None , props: Optional[dict[str, str]] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, HTMLNode):
            return NotImplemented
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if not self.props or self.props is {}:
            return ""

        s: list[str] = []
        for key, value in self.props.items():
            s.append(f'{key}="{str(value)}"')
        return " ".join(s)
