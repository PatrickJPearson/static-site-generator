from blocktype import BlockType

def block_to_blocktype(block):
    lines = block.split('\n')
    if lines[0].startswith('#') and ("#######" not in lines[0]) and "# " in lines[0]:
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    else:
        ordered = True
        ind = 1
        unordered = True
        quote = True
        for line in lines:
            if quote and line[0] == '>':
                pass
            else:
                quote = False
            if unordered and line[0] == '-':
                pass
            else:
                unordered = False
            if ordered and line.startswith(f"{ind}. "):
                ind += 1
            else:
                ordered = False
        if ordered:
            return BlockType.ORDERED_LIST
        elif unordered:
            return BlockType.UNORDERED_LIST
        elif quote:
            return BlockType.QUOTE
        else:
            return BlockType.PARAGRAPH
