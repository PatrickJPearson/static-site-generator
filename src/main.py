from textnode import *
from functions.copy_source import copy_source
from functions.generate_pages_recursive import generate_pages_recursive

def main():
    copy_source("/home/pears/workspace/username/static-site-generator/public", "/home/pears/workspace/username/static-site-generator/static", True)
    generate_pages_recursive("content", "template.html", "public")
main()