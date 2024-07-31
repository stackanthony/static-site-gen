import unittest
from src.classes.LeafNode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode('a', 'test', {'hey': 'this is a test'})
        node2 = LeafNode('a', 'test', {'hey': 'this is a test'})
        node3 = LeafNode('b', 'test', {'hey': 'this is a test'})
        node4 = LeafNode('a', 'different', {'hey': 'this is a test'})
        node5 = LeafNode('a', 'test', {'hey': 'different'})

        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node1, node4)
        self.assertNotEqual(node1, node5)

    def test_to_html(self):
        node = LeafNode('a', 'test', {'href': 'https://www.google.com'})
        expectedHTML = '<a href="https://www.google.com">test</a>'
        self.assertEqual(node.to_html(), expectedHTML)

        node_no_props = LeafNode('a', 'test')
        expectedHTML_no_props = '<a>test</a>'
        self.assertEqual(node_no_props.to_html(), expectedHTML_no_props)

        node_no_tag = LeafNode(value='test')
        expectedHTML_no_tag = 'test'
        self.assertEqual(node_no_tag.to_html(), expectedHTML_no_tag)

    def test_to_html_empty_value(self):
        node = LeafNode('a', '')
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_special_characters(self):
        node = LeafNode('p', 'Special <>&"\' chars', {'class': 'special'})
        expectedHTML = '<p class="special">Special <>&"\' chars</p>'
        self.assertEqual(node.to_html(), expectedHTML)

    def test_to_html_boolean_prop(self):
        node = LeafNode('input', 'value', {'disabled': True, 'type': 'text'})
        expectedHTML = '<input disabled="True" type="text">value</input>'
        self.assertEqual(node.to_html(), expectedHTML)

    def test_to_html_integer_prop(self):
        node = LeafNode('span', 'number', {'data-count': 5})
        expectedHTML = '<span data-count="5">number</span>'
        self.assertEqual(node.to_html(), expectedHTML)


if __name__ == '__main__':
    unittest.main()
