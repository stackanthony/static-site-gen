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

    def test_text_node_to_html_node(self):
        node = TextNode("test", "text")

        expectedHTML = "test"
        self.assertEqual(node.text_node_to_html_node().to_html(), expectedHTML)

    def test_bold_text_node(self):
        node = TextNode("test", "bold")

        expectedHTML = "<b>test</b>"
        self.assertEqual(node.text_node_to_html_node().to_html(), expectedHTML)

    def test_italic_text_node(self):
        node = TextNode("test", "italic")

        expectedHTML = "<i>test</i>"
        self.assertEqual(node.text_node_to_html_node().to_html(), expectedHTML)

    def test_code_text_node(self):
        node = TextNode("test", "code")

        expectedHTML = "<code>test</code>"
        self.assertEqual(node.text_node_to_html_node().to_html(), expectedHTML)

    def test_no_link_text_node(self):
        node = TextNode("test", "link")

        with self.assertRaises(ValueError):
            node.text_node_to_html_node().to_html()

    def test_link_text_node(self):
        node = TextNode("test", "link", "google.com")

        expectedHTML = '<a href="google.com">test</a>'
        self.assertEqual(node.text_node_to_html_node().to_html(), expectedHTML)

    def test_no_image_text_node(self):
        node = TextNode("test", "link")

        with self.assertRaises(ValueError):
            node.text_node_to_html_node().to_html()
    
    def test_image_text_node(self):
        node = TextNode("test", "image", "www.test.com/image.png")

        expectedHTML = '<img src="www.test.com/image.png"></img>'
        self.assertEqual(node.text_node_to_html_node().to_html(), expectedHTML)


if __name__ == "__main__":
    unittest.main()
