def extract_title(md):
    if md.startswith('#'):
        title = md.split('\n', 1)
        return title[0][1:].strip()
    else:
        raise Exception("Error: title missing #")