import unittest
from functions.markdown_to_html_node import markdown_to_html_node

class testtest(unittest.TestCase):
    def test_test(self):
        f = open("/home/pears/workspace/username/static-site-generator/content/blog/glorfindel/index.md")
        md = f.read()
        node = markdown_to_html_node(md)
        print(node.to_html())
