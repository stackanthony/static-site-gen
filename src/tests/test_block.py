import unittest

from src.classes.Block import Block


class TestBlock(unittest.TestCase):
    def test_eq(self):
        block = Block('test')
        block2 = Block('test')

        self.assertEqual(block, block2)

    def test_markdown_to_blocks(self):
        markdown = '# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item'

        expected_return_list = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item',
        ]

        return_list = [
            block.text for block in Block.markdown_to_blocks(markdown)
        ]
        self.assertListEqual(return_list, expected_return_list)
