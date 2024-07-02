import re


class TextProcessor:
    def __init__(self, text) -> None:
        self.text = text

    def extract_markdown_images(self) -> list[tuple[str, str]]:
        if not self.text:
            raise ValueError("No text to process")
        return re.findall(r"!\[(.*?)\]\((.*?)\)", self.text)

    def extract_markdown_links(self) -> list[tuple[str, str]]:
        if not self.text:
            raise ValueError("No text to process")
        return re.findall(r"\[(.*?)\]\((.*?)\)", self.text)

