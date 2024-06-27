from typing import Optional, Self

class HTMLNode:
    def __init__(self, tag: Optional[str] = None, value: Optional[str] = None, children: Optional[list[Self]] = None, props: Optional[dict[str, str | bool | int]] = None):
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
        if not self.props:
            raise Exception("No Props to Parse")

        s: list[str] = []
        for key, value in self.props.items():
            s.append(f'{key}="{str(value)}"')
        return " ".join(s)
