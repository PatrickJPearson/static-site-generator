import unittest
from textnode import TextNode, TextType
from functions.split_nodes_delimiter import split_nodes_delimiter


class TestParentNode(unittest.TestCase):
    def test_bold(self):
        node_list = [TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter(node_list, "**", TextType.BOLD), [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ])

    def test_code(self):
        node_list = [TextNode("This is text with a `code block` word", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter(node_list, "`", TextType.CODE), [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_code(self):
        node_list = [TextNode("This is text with an _italic phrase_ in the middle", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter(node_list, "_", TextType.ITALIC), [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic phrase", TextType.ITALIC),
            TextNode(" in the middle", TextType.TEXT),
        ])