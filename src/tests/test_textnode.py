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

    def test_split_nodes_delimeter(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = TextNode.split_nodes_delimiter([node], "`", "code")

        expectedReturnValue = "[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None)]"

        self.assertEqual(str(new_nodes), expectedReturnValue)

    def test_invalid_text_type(self):
        node = TextNode()
        with self.assertRaises(ValueError):
            TextNode.split_nodes_delimiter([node], "`", "fasdjfnsafj")

    def test_invalid_delimeter(self):
        node = TextNode()
        with self.assertRaises(ValueError):
            TextNode.split_nodes_delimiter([node], "asdnsd", "*")

    def test_not_enclosed_delimiter(self):
        node = TextNode("test this with a `code", "text")


        with self.assertRaises(Exception):
            TextNode.split_nodes_delimiter([node], "`", "code")

    def test_split_nodes_delimiter_mixed_delimiters(self):
            node = TextNode("This is `code` and **bold** text", "text")
            split_code_nodes = TextNode.split_nodes_delimiter([node], "`", "code")
            split_bold_nodes = TextNode.split_nodes_delimiter([node], "**", "bold")

            expected_split_code_nodes = "[TextNode(This is , text, None), TextNode(code, code, None), TextNode( and **bold** text, text, None)]"
            expected_split_bold_nodes = "[TextNode(This is `code` and , text, None), TextNode(bold, bold, None), TextNode( text, text, None)]"
            self.assertEqual(str(split_code_nodes), expected_split_code_nodes)
            self.assertEqual(str(split_bold_nodes), expected_split_bold_nodes)

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            "text",
        )

        TextNode.split_nodes_image([node])




if __name__ == "__main__":
    unittest.main()
