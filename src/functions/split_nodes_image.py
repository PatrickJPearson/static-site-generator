from textnode import TextNode, TextType
from functions.extract_markdown_images import extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text:
            images = extract_markdown_images(node.text)
            if not images:
                new_nodes.append(node)
            text = node.text
            for image in images:
                delim = f"![{image[0]}]({image[1]})"
                lis = text.split(delim)
                if len(lis) > 1:
                    new_nodes.append(TextNode(lis[0], TextType.TEXT))
                    text = lis[1]
                new_nodes.append(TextNode(image[0], TextType.IMAGE, url=image[1]))
                if images[len(images)-1] == image and text:
                    new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes