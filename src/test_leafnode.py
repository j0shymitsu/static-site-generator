import unittest

from leafnode import LeafNode


class LeafNodeTest(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag="p", value="text")
        node2 = LeafNode(tag="p", value="text")
        self.assertEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h(self):
        node = LeafNode("h1", "Hello, heading world!")
        self.assertEqual(node.to_html(), "<h1>Hello, heading world!</h1>")
