import unittest

from src.classes.blocks.BlockFactory import BlockFactory
from src.classes.blocks.Code import Code
from src.classes.blocks.Heading import Heading
from src.classes.blocks.Quote import Quote

class TestBlockFactory(unittest.TestCase):
    def test_create_blocks_heading(self):
        markdown = "### This is a heading.\n\n"

        expected_return_list = [
            Heading("### This is a heading.")
        ]

        self.assertListEqual(BlockFactory.create_blocks(markdown), expected_return_list)

    def test_create_blocks_code(self):
        markdown = "```test```"

        expected_return_list = [
            Code(markdown)
        ]

        self.assertListEqual(BlockFactory.create_blocks(markdown), expected_return_list)

    def test_create_block_quote(self):
        markdown = ">Test\n>Test2\n>Test3"

        expected_return_list = [
            Quote(markdown)
        ]

        self.assertListEqual(BlockFactory.create_blocks(markdown), expected_return_list)
