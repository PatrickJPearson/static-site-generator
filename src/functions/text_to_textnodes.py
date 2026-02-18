from functions.split_nodes_delimiter import split_nodes_delimiter
from functions.split_nodes_image import split_nodes_image
from functions.split_nodes_link import split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    return split_nodes_link(split_nodes_image(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(nodes, "_", TextType.ITALIC), "**", TextType.BOLD), "`", TextType.CODE)))