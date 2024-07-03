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

        expected_html = "test"
        self.assertEqual(node.text_node_to_html_node().to_html(), expected_html)

    def test_bold_text_node(self):
        node = TextNode("test", "bold")

        expected_html = "<b>test</b>"
        self.assertEqual(node.text_node_to_html_node().to_html(), expected_html)

    def test_italic_text_node(self):
        node = TextNode("test", "italic")

        expected_html = "<i>test</i>"
        self.assertEqual(node.text_node_to_html_node().to_html(), expected_html)

    def test_code_text_node(self):
        node = TextNode("test", "code")

        expected_html = "<code>test</code>"
        self.assertEqual(node.text_node_to_html_node().to_html(), expected_html)

    def test_no_link_text_node(self):
        node = TextNode("test", "link")

        with self.assertRaises(ValueError):
            node.text_node_to_html_node().to_html()

    def test_link_text_node(self):
        node = TextNode("test", "link", "google.com")

        expected_html = '<a href="google.com">test</a>'
        self.assertEqual(node.text_node_to_html_node().to_html(), expected_html)

    def test_no_image_text_node(self):
        node = TextNode("test", "link")

        with self.assertRaises(ValueError):
            node.text_node_to_html_node().to_html()
    
    def test_image_text_node(self):
        node = TextNode("test", "image", "www.test.com/image.png")

        expected_html = '<img src="www.test.com/image.png"></img>'
        self.assertEqual(node.text_node_to_html_node().to_html(), expected_html)

    def test_split_nodes_delimeter(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = TextNode.split_nodes_delimiter([node], "`", "code")

        expected_return_value = "[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None)]"

        self.assertEqual(str(new_nodes), expected_return_value)

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

        expected_return_list = [
            TextNode("This is text with an ", "text"),
            TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", "text"),
            TextNode(
                "second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]

        self.assertListEqual(TextNode.split_nodes_image([node]), expected_return_list)

    def test_split_nodes_image_no_images(self):
        node = TextNode("This is plain text with no images.", "text")

        expected_return_list = [
            TextNode("This is plain text with no images.", "text")
        ]

        self.assertListEqual(TextNode.split_nodes_image([node]), expected_return_list)

    def test_split_nodes_image_image_at_start(self):
        node = TextNode(
            "![image1](http://example.com/1.png) and some text after.",
            "text"
        )

        expected_return_list = [
            TextNode("image1", "image", "http://example.com/1.png"),
            TextNode(" and some text after.", "text")
        ]

        self.assertListEqual(TextNode.split_nodes_image([node]), expected_return_list)

    def test_split_nodes_image_image_at_end(self):
        node = TextNode(
            "Some text before the image ![image1](http://example.com/1.png)",
            "text"
        )

        expected_return_list = [
            TextNode("Some text before the image ", "text"),
            TextNode("image1", "image", "http://example.com/1.png")
        ]

        self.assertListEqual(TextNode.split_nodes_image([node]), expected_return_list)

    def test_split_nodes_image_multiple_text_nodes(self):
        node1 = TextNode(
            "First node with ![image1](http://example.com/1.png) and text.",
            "text"
        )
        node2 = TextNode(
            "Second node with text and ![image2](http://example.com/2.png).",
            "text"
        )

        expected_return_list = [
            TextNode("First node with ", "text"),
            TextNode("image1", "image", "http://example.com/1.png"),
            TextNode(" and text.", "text"),
            TextNode("Second node with text and ", "text"),
            TextNode("image2", "image", "http://example.com/2.png"),
            TextNode(".", "text")
        ]

        self.assertListEqual(TextNode.split_nodes_image([node1, node2]), expected_return_list)

    def test_split_nodes_image_no_text_nodes(self):
        expected_return_list = []

        self.assertListEqual(TextNode.split_nodes_image([]), expected_return_list)

    def test_split_nodes_image_broken_image_syntax(self):
        node = TextNode(
            "This text has a broken image ![image1(http://example.com/1.png) syntax.",
            "text"
        )

        expected_return_list = [
            TextNode("This text has a broken image ![image1(http://example.com/1.png) syntax.", "text")
        ]

        self.assertListEqual(TextNode.split_nodes_image([node]), expected_return_list)

if __name__ == "__main__":
    unittest.main()
