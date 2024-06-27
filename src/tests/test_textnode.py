import unittest

from src.classes.TextNode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_fields(self):
        node = TextNode("This is a text node", "bold", "http://stackanthony.com")

        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, "bold")
        self.assertEqual(node.url, "http://stackanthony.com")

    def test_text_type_mismatch(self):
        node = TextNode("Test Node", "bold")
        node2 = TextNode("Test Node", "italic")
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_empty_url(self):
        node = TextNode("Test Node", "bold")
        self.assertEqual(node.url, None)
    
    def test_empty_text(self):
        node = TextNode()

        self.assertEqual(node.text, "")

    def test_empty_text_type(self):
        node = TextNode("test")

        self.assertEqual(node.text_type, "")


if __name__ == "__main__":
    unittest.main()
