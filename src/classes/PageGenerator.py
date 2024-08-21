from classes.MarkdownProcessor import MarkdownProcessor
from src.classes.FileHandler import FileHandler
from src.classes.TextProcessor import TextProcessor

import os


class PageGenerator:
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

    @staticmethod
    def generate_pages_recursive(
        dir_path_content: str, template_path: str, dest_path: str
    ):
        try:
            dir_entries: list[str] = FileHandler.list_dir_entries(
                dir_path_content
            )

            for dir_entry in dir_entries:
                cur_path = os.path.join(dir_path_content, dir_entry)

                if cur_path.endswith('.md') and FileHandler.is_file(cur_path):
                    # Create the destination path for the HTML file
                    new_file_dest: str = os.path.join(
                        dest_path,
                        cur_path.split('/')[-1].replace('.md', '.html'),
                    )

                    # Generate the page using the provided context
                    PageGenerator.generate_page(
                        cur_path, template_path, new_file_dest
                    )
                    continue

                # If it's a directory, create the directory in the destination and recurse
                new_dest_path = os.path.join(
                    dest_path, cur_path.split('/')[-1]
                )
                FileHandler.create_dir(new_dest_path)

                # Recursive call to process subdirectories
                PageGenerator.generate_pages_recursive(
                    cur_path, template_path, new_dest_path
                )

        except Exception as e:
            print(f'An error occurred: {e}')
            raise
