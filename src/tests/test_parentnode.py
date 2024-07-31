import unittest

from src.classes.ParentNode import ParentNode
from src.classes.LeafNode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            'p',
            [
                LeafNode('b', 'Bold text'),
                LeafNode(None, 'Normal text'),
                LeafNode('i', 'italic text'),
                LeafNode(None, 'Normal text'),
            ],
        )

        expectedHTML = (
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

        self.assertEqual(node.to_html(), expectedHTML)

    def test_nested_nodes(self):
        node = ParentNode(
            'div',
            [
                ParentNode(
                    'p',
                    [
                        LeafNode('b', 'Bold Text'),
                        LeafNode(None, 'Normal Text'),
                    ],
                ),
                LeafNode('i', 'italic text'),
            ],
        )

        expectedHTML = (
            '<div><p><b>Bold Text</b>Normal Text</p><i>italic text</i></div>'
        )

        self.assertEqual(node.to_html(), expectedHTML)

    def test_parent_nodes_no_leafs(self):
        node = ParentNode('div', [ParentNode('p')])

        with self.assertRaises(ValueError):
            node.to_html()

    def test_empty_parent_node(self):
        node = ParentNode('div')

        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_node_without_text(self):
        node = ParentNode(
            'p',
            [
                LeafNode('b'),
                LeafNode(None),
                LeafNode('i'),
                LeafNode(None),
            ],
        )

        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_node_with_attributes(self):
        node = ParentNode(
            'div',
            [LeafNode('span', 'Some text')],
            {'class': 'container', 'id': 'main'},
        )
        expectedHTML = (
            '<div class="container" id="main"><span>Some text</span></div>'
        )
        self.assertEqual(node.to_html(), expectedHTML)

    def test_mixed_nested_and_leaf_nodes(self):
        node = ParentNode(
            'div',
            [
                ParentNode(
                    'p',
                    [
                        LeafNode('b', 'Bold Text'),
                        ParentNode('span', [LeafNode(None, 'Span text')]),
                        LeafNode(None, 'Normal Text'),
                    ],
                ),
                LeafNode('i', 'italic text'),
            ],
        )
        expectedHTML = '<div><p><b>Bold Text</b><span>Span text</span>Normal Text</p><i>italic text</i></div>'
        self.assertEqual(node.to_html(), expectedHTML)

    def test_node_with_no_tag(self):
        node = ParentNode()

        with self.assertRaises(ValueError):
            node.to_html()

    def test_single_leaf_node(self):
        node = ParentNode('a', [LeafNode('b', 'Bold Text')])

        expectedHTML = '<a><b>Bold Text</b></a>'

        self.assertEqual(node.to_html(), expectedHTML)
