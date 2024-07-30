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

    def extract_markdown_title(self) -> str: 
        if not self.text:
            raise ValueError("No text to processs")

        split_text: list[str] = self.text.split(" ")

        if len(split_text) < 2 or split_text[0] != "#":
            raise ValueError("Not a Valid Title")

        return split_text[1]
    
    def get_trailing_text(self, delimeter: str) -> str | None:
        if not self.text:
            raise ValueError("No text to process")

        trailing_text = self.text.split(delimeter, maxsplit=1)
        if len(trailing_text) > 1 and trailing_text[1] != '':
            if self.extract_markdown_links() or self.extract_markdown_images():
                trailing_text[0] += delimeter
            return trailing_text[1]

        return None


