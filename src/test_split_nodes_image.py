import unittest
from functions.split_nodes_image import split_nodes_image
from textnode import TextNode, TextType

class TestSplitImages(unittest.TestCase):
    def test_split_image(self):
        nodes = split_nodes_image([TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)])
        res = [TextNode("This is text with an ", TextType.TEXT), TextNode("image", TextType.IMAGE, url="https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(res, nodes)
        res = [TextNode("This is text with a ", TextType.TEXT), TextNode("rick roll", TextType.IMAGE, url="https://i.imgur.com/aKaOqIh.gif"),TextNode(" and ", TextType.TEXT), TextNode("obi wan", TextType.IMAGE, url="https://i.imgur.com/fJRm4Vk.jpeg")]
        nodes = split_nodes_image([TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)])
        self.assertListEqual(res, nodes)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
    )
