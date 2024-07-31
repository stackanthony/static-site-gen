import unittest

from src.classes.Block import Block
from src.classes.blocks.BlockFactory import BlockFactory
from src.classes.blocks.Code import Code
from src.classes.blocks.Heading import Heading
from src.classes.blocks.OrderedList import OrderedList
from src.classes.blocks.Quote import Quote
from src.classes.blocks.UnorderedList import UnorderedList


class TestBlockFactory(unittest.TestCase):
    def test_create_blocks_heading(self):
        markdown = '### This is a heading.\n\n'

        expected_return_list = [Heading('This is a heading.', 3)]

        self.assertListEqual(
            BlockFactory.create_blocks(markdown), expected_return_list
        )

    def test_create_blocks_code(self):
        markdown = '```test```'

        expected_return_list = [Code('test')]

        self.assertListEqual(
            BlockFactory.create_blocks(markdown), expected_return_list
        )

    def test_create_blocks_code_complex(self):
        markdown = '```test1\ntest2\ntest3    faskfnsajdfasf   dfasfjasf\n```'

        expected_return_list = [Code(markdown.split('```')[1])]

        self.assertListEqual(
            BlockFactory.create_blocks(markdown), expected_return_list
        )

    def test_create_block_quote(self):
        markdown = '> Test\n> Test2\n> Test3'

        expected_return_list = [Quote('Test\nTest2\nTest3')]

        self.assertListEqual(
            BlockFactory.create_blocks(markdown), expected_return_list
        )

    def test_create_unordered_list(self):
        markdown = '* test1\n* test2\n- test3'

        expected_return_list = [UnorderedList('test1\ntest2\ntest3\n')]

        self.assertListEqual(
            BlockFactory.create_blocks(markdown), expected_return_list
        )

    def test_create_ordered_list(self):
        markdown = '1. test\n2. test2\n3. dsafkdsajnf'

        expected_return_list = [OrderedList(markdown)]

        self.assertListEqual(
            BlockFactory.create_blocks(markdown), expected_return_list
        )

    def test_create_blocks_empty(self):
        markdown = ''
        expected_return_list = []
        self.assertListEqual(
            BlockFactory.create_blocks(markdown), expected_return_list
        )

    def test_create_blocks_plain_text(self):
        markdown = 'This is just plain text.'
        expected_return_list = [Block(markdown)]
        self.assertListEqual(
            BlockFactory.create_blocks(markdown), expected_return_list
        )

    def test_create_blocks_multiple_headings(self):
        markdown = '### Heading1\n\n### Heading2\n\n### Heading3'
        expected_return_list = [
            Heading('Heading1', 3),
            Heading('Heading2', 3),
            Heading('Heading3', 3),
        ]
        self.assertListEqual(
            BlockFactory.create_blocks(markdown), expected_return_list
        )

    def test_create_blocks_multiple_code_blocks(self):
        markdown = '```code1```\n\n```code2```\n\n```code3```'
        expected_return_list = [Code('code1'), Code('code2'), Code('code3')]
        self.assertListEqual(
            BlockFactory.create_blocks(markdown), expected_return_list
        )

    def test_create_blocks_mixed_content(self):
        markdown = '### Heading\n\nThis is a paragraph.\n\n* item1\n* item2\n\n> Quote'
        expected_return_list = [
            Heading('Heading', 3),
            Block('This is a paragraph.'),
            UnorderedList('item1\nitem2\n'),
            Quote('Quote'),
        ]

        self.assertListEqual(
            BlockFactory.create_blocks(markdown), expected_return_list
        )


if __name__ == '__main__':
    unittest.main()
