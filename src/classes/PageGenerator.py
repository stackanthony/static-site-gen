from classes.MarkdownProcessor import MarkdownProcessor
from src.classes.FileHandler import FileHandler
from src.classes.TextProcessor import TextProcessor


class PageGenerator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_page(from_path: str, template_path: str, dest_path: str):
        print(
            f'Generating page from {from_path} to {dest_path} using {template_path}'
        )

        markdown_file_contents: str = ''
        with open(from_path) as f:
            markdown_file_contents = f.read()
        mp = MarkdownProcessor(markdown_file_contents)
        tp = TextProcessor(markdown_file_contents)
        markdown_html: str = mp.markdown_to_html_node().to_html()
        page_title: str = tp.extract_markdown_title()

        FileHandler.replace_word_file(
            template_path, dest_path, '{{ Title }}', page_title
        )
        FileHandler.replace_word_file(
            dest_path, dest_path, '{{ Content }}', markdown_html
        )
