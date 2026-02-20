def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    block_list = []
    for block in blocks:
        strip_block = block.strip()
        if strip_block:
            block_list.append(strip_block)
    return block_list
