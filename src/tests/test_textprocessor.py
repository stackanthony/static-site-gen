import unittest

from src.classes.TextProcessor import TextProcessor

class TestTextProcessor(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        tp = TextProcessor(text)

        expectedReturn = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertListEqual(tp.extract_markdown_images(), expectedReturn)
    
    def test_no_text_extract_markdown_images(self):
        tp = TextProcessor("")

        with self.assertRaises(ValueError):
            tp.extract_markdown_images()

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        tp = TextProcessor(text)

        expectedReturn = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]

        self.assertListEqual(tp.extract_markdown_links(), expectedReturn)

