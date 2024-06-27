import unittest

from src.classes.HTMLNode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "test")
        node2 = HTMLNode("a", "test")
        self.assertEqual(node, node2)

    def test_empty_props_to_html(self):
        node = HTMLNode()

        with self.assertRaises(Exception):
            node.props_to_html()
    
    def test_props_to_html_no_properties(self):
        node = HTMLNode("a", "test text", props={})
        
        with self.assertRaises(Exception):
            node.props_to_html()

    def test_props_to_html(self):
        node = HTMLNode("a", "test text", props={"href" : "https://www.google.com", "target" : "_blank"})

        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

        
    def test_props_to_html_single_property(self):
        node = HTMLNode("img", "", props={"src": "image.png"})
        
        self.assertEqual(node.props_to_html(), 'src="image.png"')

    def test_props_to_html_boolean_property(self):
        node = HTMLNode("input", "", props={"type": "checkbox", "checked": True})
        
        self.assertEqual(node.props_to_html(), 'type="checkbox" checked="True"')

    def test_props_to_html_mixed_properties(self):
        node = HTMLNode("input", "", props={"type": "text", "value": "input value", "required": True, "maxlength": 10})
        
        self.assertEqual(node.props_to_html(), 'type="text" value="input value" required="True" maxlength="10"')
