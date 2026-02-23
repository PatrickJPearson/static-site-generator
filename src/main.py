from textnode import *
import sys
from functions.copy_source import copy_source
from functions.generate_pages_recursive import generate_pages_recursive

def main():
    basepath = '/'
    if sys.argv:
        basepath = sys.argv
    copy_source("/home/pears/workspace/username/static-site-generator/docs", "/home/pears/workspace/username/static-site-generator/static", True)
    generate_pages_recursive("content", "template.html", "docs", basepath)
main()