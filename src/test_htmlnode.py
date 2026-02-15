import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode(props={
        "href": "https://www.google.com",
        "target": "_blank",
        }
        )
        self.assertEqual(node1.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
        node2 = HTMLNode(tag="tag")
        self.assertNotEqual(node1, node2)
        node3 = HTMLNode(tag="tag", value="value", children="children", props=node1.props)
        self.assertIn("tag",str(node3))
        self.assertIn("value",str(node3))
        self.assertIn("children", str(node3))
        self.assertIn("blank", str(node3))

