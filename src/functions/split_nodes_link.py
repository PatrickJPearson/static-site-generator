from textnode import TextNode, TextType
from functions.extract_markdown_links import extract_markdown_links

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text:
            links = extract_markdown_links(node.text)
            if not links:
                new_nodes.append(node)
            else:
                text = node.text
                for link in links:
                    delim = f"[{link[0]}]({link[1]})"
                    lis = text.split(delim)
                    if len(lis) > 1:
                        new_nodes.append(TextNode(lis[0], TextType.TEXT))
                        text = lis[1]
                    new_nodes.append(TextNode(link[0], TextType.LINK, url=link[1]))
    return new_nodes