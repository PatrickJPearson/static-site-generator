import unittest
from functions.markdown_to_html_node import markdown_to_html_node
from textnode import TextNode, TextType

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_lists(self):
        md = """
- This is the first list item in a list block
- This is a list item
- This is another list item
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul></div>")
        md2 = """
1. This is the first list item in a list block
2. This is a list item
3. This is another list item
    """
        node = markdown_to_html_node(md2)
        html = node.to_html()
        self.assertEqual(html, "<div><ol><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ol></div>")

    def test_heading(self):
        md = """
##### This is a five heading block

# This is a one heading block

####### This is a paragraph
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><h5> This is a five heading block</h5><h1> This is a one heading block</h1><p>####### This is a paragraph</p></div>")

    def test_quote(self):
        md = """
> This
> is a
> quoteblock
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><blockquote>This is a quoteblock</blockquote></div>")