import unittest
from functions.split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        nodes = split_nodes_link([TextNode("This is text with a [link](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)])
        res = [TextNode("This is text with a ", TextType.TEXT), TextNode("link", TextType.LINK, url="https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(res, nodes)
        res = [TextNode("This is text with a ", TextType.TEXT), TextNode("rick roll", TextType.LINK, url="https://i.imgur.com/aKaOqIh.gif"),TextNode(" and ", TextType.TEXT), TextNode("obi wan", TextType.LINK, url="https://i.imgur.com/fJRm4Vk.jpeg")]
        nodes = split_nodes_link([TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)])
        self.assertListEqual(res, nodes)

    def test_split_link(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
    )
