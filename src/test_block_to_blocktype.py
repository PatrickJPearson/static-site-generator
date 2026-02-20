import unittest
from functions.block_to_blocktype import block_to_blocktype
from blocktype import BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_code(self):
        md = """```
code
block
text
```"""
        self.assertEqual(block_to_blocktype(md), BlockType.CODE)
        md2 = """````
too
many
ticks
```"""
        self.assertEqual(block_to_blocktype(md2), BlockType.PARAGRAPH)

    def test_heading(self):
        md = """#### heading
heading
text
"""
        self.assertEqual(block_to_blocktype(md), BlockType.HEADING)
        md2 = """######## Bees
too
many
#
"""
        self.assertEqual(block_to_blocktype(md2), BlockType.PARAGRAPH)

    def test_quote(self):
        md = """>quote
>text
>"""
        self.assertEqual(block_to_blocktype(md), BlockType.QUOTE)
        md2 = """>missing
greater than
>"""
        self.assertEqual(block_to_blocktype(md2), BlockType.PARAGRAPH)

    def test_unordered(self):
        md = """-un
-ordered
-list"""
        self.assertEqual(block_to_blocktype(md), BlockType.UNORDERED_LIST)
        md2 = """-missing
-last
hyphen"""
        self.assertEqual(block_to_blocktype(md2), BlockType.PARAGRAPH)

    def test_ordered(self):
        md = """1. ordered
2. list
3. test"""
        self.assertEqual(block_to_blocktype(md), BlockType.ORDERED_LIST)
        md2 = """1. numbers
3. out of
4. order"""
        self.assertEqual(block_to_blocktype(md2), BlockType.PARAGRAPH)


