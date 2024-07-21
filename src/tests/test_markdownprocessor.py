import unittest

from src.classes.HTMLNode import HTMLNode
from src.classes.LeafNode import LeafNode
from src.classes.MarkdownProcessor import MarkdownProcessor

class TestMarkdownProcessor(unittest.TestCase):
    def test_simple_markdown(self):
        markdown = "### This is a heading.\n\n"

        expected_return_value = HTMLNode("div", children=[HTMLNode("h3", children=[LeafNode(None, "This is a heading.")])])

        mp = MarkdownProcessor(markdown)
        self.assertEqual(mp.markdown_to_html_node(), expected_return_value)

    def test_code_markdown(self):
        markdown = "```test1\ntest2\ntest3    faskfnsajdfasf   dfasfjasf```\n\n"

        expected_return_value = HTMLNode("div", children=[
            HTMLNode("pre", children=[LeafNode("code", "test1\ntest2\ntest3    faskfnsajdfasf   dfasfjasf")])
        ])

        mp = MarkdownProcessor(markdown)
        self.assertEqual(mp.markdown_to_html_node(), expected_return_value)
