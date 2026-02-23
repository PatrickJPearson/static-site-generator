from functions.markdown_to_html_node import markdown_to_html_node
from functions.extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    split_dest = dest_path.split('.')
    f = open(from_path)
    md = f.read()
    f = open(template_path)
    html = f.read()
    md_as_html_node = markdown_to_html_node(md)
    md_as_html = md_as_html_node.to_html()
    title = extract_title(md)
    html_with_title = html.replace("{{ Title }}", title)
    html_with_both = html_with_title.replace("{{ Content }}", md_as_html)
    print(split_dest)
    os.makedirs(split_dest[0], exist_ok=True)
    with open(dest_path, 'w') as a:
        a.write(html_with_both)


