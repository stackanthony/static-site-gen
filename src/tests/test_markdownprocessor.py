import unittest

from src.classes.HTMLNode import HTMLNode
from src.classes.LeafNode import LeafNode
from src.classes.MarkdownProcessor import MarkdownProcessor

class TestMarkdownProcessor(unittest.TestCase):
    def test_simple_markdown(self):
        markdown = "### This is a heading."

        expected_return_value = HTMLNode("div", children=[HTMLNode("h3", children=[LeafNode("text", "This is a heading.")])])

        mp = MarkdownProcessor(markdown)
        self.assertEqual(mp.markdown_to_html_node(), expected_return_value)

    def test_code_markdown(self):
        markdown = "```test1\ntest2\ntest3    faskfnsajdfasf   dfasfjasf```"

        expected_return_value = HTMLNode("div", children=[
            HTMLNode("pre", children=[LeafNode("code", "test1\ntest2\ntest3    faskfnsajdfasf   dfasfjasf")])
        ])

        mp = MarkdownProcessor(markdown)
        self.assertEqual(mp.markdown_to_html_node(), expected_return_value)

    def test_quote_markdown(self):
        markdown = "> quote1\n> quote2 sadasd"

        expected_return_value = HTMLNode("div", children=[
            HTMLNode("blockquote", children=[
                LeafNode("text", markdown)
            ])
        ])

        mp = MarkdownProcessor(markdown)
        self.assertEqual(mp.markdown_to_html_node(), expected_return_value)

    def test_unordered_list_markdown(self):
        markdown = "- First item\n- Second item\n- Third item"

        expected_return_value = HTMLNode("div", children=[
            HTMLNode("ul", children=[
                HTMLNode("li", "First item"),
                HTMLNode("li", "Second item"),
                HTMLNode("li", "Third item")
            ])
        ])

        mp = MarkdownProcessor(markdown)
        self.assertEqual(mp.markdown_to_html_node(), expected_return_value)
