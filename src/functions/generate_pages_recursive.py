import os
from functions.generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if os.path.isdir(dir_path_content):
        for item in os.listdir(dir_path_content):
            new_dir_path = os.path.join(dir_path_content, item)
            new_dest_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(new_dir_path, template_path, new_dest_path, basepath)
    else:
        file_path = dest_dir_path.split('.')
        ext_file = file_path[0] + ".html"
        generate_page(dir_path_content, template_path, ext_file, basepath)