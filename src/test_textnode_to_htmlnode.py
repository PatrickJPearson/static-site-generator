import unittest
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType
from functions.textnode_to_htmlnode import text_node_to_html_node


class TestParentNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("Click me!", TextType.LINK, url="https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">Click me!</a>')