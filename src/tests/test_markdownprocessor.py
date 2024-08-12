import unittest

from src.classes.HTMLNode import HTMLNode
from src.classes.LeafNode import LeafNode
from src.classes.MarkdownProcessor import MarkdownProcessor


class TestMarkdownProcessor(unittest.TestCase):
    def test_simple_markdown(self):
        markdown = '### This is a heading.'

        expected_return_value = HTMLNode(
            'div',
            children=[
                HTMLNode(
                    'h3', children=[LeafNode('text', 'This is a heading.')]
                )
            ],
        )

        mp = MarkdownProcessor(markdown)
        self.assertEqual(mp.markdown_to_html_node(), expected_return_value)

    def test_code_markdown(self):
        markdown = '```test1\ntest2\ntest3    faskfnsajdfasf   dfasfjasf```'

        expected_return_value = HTMLNode(
            'div',
            children=[
                HTMLNode(
                    'pre',
                    children=[
                        LeafNode(
                            'code',
                            'test1\ntest2\ntest3    faskfnsajdfasf   dfasfjasf',
                        )
                    ],
                )
            ],
        )

        mp = MarkdownProcessor(markdown)
        self.assertEqual(mp.markdown_to_html_node(), expected_return_value)

    def test_quote_markdown(self):
        markdown = '> quote1\n> quote2 sadasd'

        expected_return_value = HTMLNode(
            'div',
            children=[
                HTMLNode(
                    'blockquote',
                    children=[LeafNode('text', 'quote1\nquote2 sadasd')],
                )
            ],
        )

        mp = MarkdownProcessor(markdown)
        self.assertEqual(mp.markdown_to_html_node(), expected_return_value)

    def test_unordered_list_markdown(self):
        markdown = '- First item\n- Second item\n- Third item'

        expected_return_value = HTMLNode(
            'div',
            children=[
                HTMLNode(
                    'ul',
                    children=[
                        HTMLNode(
                            'li', children=[HTMLNode('text', 'First item')]
                        ),
                        HTMLNode(
                            'li', children=[HTMLNode('text', 'Second item')]
                        ),
                        HTMLNode(
                            'li', children=[HTMLNode('text', 'Third item')]
                        ),
                    ],
                )
            ],
        )

        mp = MarkdownProcessor(markdown)
        self.assertEqual(mp.markdown_to_html_node(), expected_return_value)

    def test_unordered_list_markdown_special_text(self):
        markdown = '- This is _italic_ text\n- Second item\n- Third item'

        expected_return_value = HTMLNode(
            'div',
            children=[
                HTMLNode(
                    'ul',
                    children=[
                        HTMLNode(
                            'li',
                            children=[
                                HTMLNode('text', 'This is '),
                                HTMLNode('i', 'italic'),
                                HTMLNode('text', ' text'),
                            ],
                        ),
                        HTMLNode(
                            'li',
                            children=[HTMLNode('text', 'Second item')],
                        ),
                        HTMLNode(
                            'li',
                            children=[HTMLNode('text', 'Third item')],
                        ),
                    ],
                )
            ],
        )
        mp = MarkdownProcessor(markdown)
        self.assertEqual(mp.markdown_to_html_node(), expected_return_value)

    def test_ordered_list_markdown(self):
        markdown = '1. First item\n2. Second item\n3. Third item'

        expected_return_value = HTMLNode(
            'div',
            children=[
                HTMLNode(
                    'ol',
                    children=[
                        HTMLNode(
                            'li', children=[HTMLNode('text', 'First item')]
                        ),
                        HTMLNode(
                            'li', children=[HTMLNode('text', 'Second item')]
                        ),
                        HTMLNode(
                            'li', children=[HTMLNode('text', 'Third item')]
                        ),
                    ],
                )
            ],
        )

        mp = MarkdownProcessor(markdown)
        self.assertEqual(mp.markdown_to_html_node(), expected_return_value)

    def test_paragraph_markdown(self):
        markdown = 'hey this is just a normal paragraph'

        expected_return_value = HTMLNode(
            'div',
            children=[
                HTMLNode(
                    'p',
                    children=[
                        LeafNode('text', 'hey this is just a normal paragraph')
                    ],
                )
            ],
        )

        mp = MarkdownProcessor(markdown)
        self.assertEqual(mp.markdown_to_html_node(), expected_return_value)


if __name__ == '__main__':
    unittest.main()
