import unittest

from htmlnode import HTMLNode


class HTMLNodeTest(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
                tag="p",
                value="text",
                children=[],
                props={}
                )
        node2 = HTMLNode(
                tag="p",
                value="text",
                children=[],
                props={}
                )
        self.assertEqual(node, node2)

    def test_tag(self):
        node = HTMLNode(tag="p")
        node2 = HTMLNode(tag="h1")
        self.assertNotEqual(node, node2)

    def test_props(self):
        node = HTMLNode()
        node2 = HTMLNode(
                "This node has attributes", 
                props={"href":"https://www.google.com"}
                )


if __name__ == "__main__":
    unittest.main()
