from functions.markdown_to_blocks import markdown_to_blocks
from functions.block_to_blocktype import block_to_blocktype
from functions.text_to_textnodes import text_to_textnodes
from functions.textnode_to_htmlnode import text_node_to_html_node
from parentnode import ParentNode
from blocktype import BlockType
from textnode import TextNode, TextType


def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    parents = []
    for block in blocks:
        type = block_to_blocktype(block)
        parent = None
        if type == BlockType.CODE:
            node = TextNode(block[4:len(block) -3], TextType.CODE)
            child = text_node_to_html_node(node)
            parent = ParentNode("pre", [child])
        elif type == BlockType.ORDERED_LIST or type == BlockType.UNORDERED_LIST:
            children = text_to_children_list(block)
            if type == BlockType.ORDERED_LIST:
                parent = ParentNode("ol", children)
            else:
                parent = ParentNode("ul", children)
        else:
            children, head = text_to_children(block)
        match type:
            case BlockType.HEADING:
                tag = f"h{head}"
                parent = ParentNode(tag, children)
            case BlockType.PARAGRAPH:
                parent = ParentNode('p', children)
            case BlockType.QUOTE:
                parent = ParentNode("blockquote", children)
        parents.append(parent)
    return ParentNode("div", parents)


def text_to_children(block):
    lines = block.split('\n')
    head = 0
    lis = []
    strip_block = ""
    if lines[0][0] == '#' and "#######" not in lines[0]:
        head = lines[0].count('#')
        lines[0] = lines[0][head:]
    elif lines[0].startswith('> '):
        for line in lines:
            lis.append(line[2:])
    if not lis:
        strip_block = ' '.join(lines)
    else:
        strip_block = ' '.join(lis)
    nodes = text_to_textnodes(strip_block)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children, head

def text_to_children_list(block):
    parent_list = []
    split_list_items = block.split('\n')
    for line in split_list_items:
        children = []
        text = line.split(' ', 1)
        nodes = text_to_textnodes(text[1])
        for node in nodes:
            children.append(text_node_to_html_node(node))
        parent_list.append(ParentNode("li", children))
    return parent_list

