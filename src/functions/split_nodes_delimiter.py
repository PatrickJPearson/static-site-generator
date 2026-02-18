from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if (text_type == TextType.ITALIC or text_type == TextType.BOLD or text_type == TextType.CODE) and delimiter in node.text:
            text = node.text.split(delimiter)
            new_nodes.append(TextNode(text[0], TextType.TEXT))
            new_nodes.append(TextNode(text[1], text_type))
            new_nodes.append(TextNode(text[2], TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes