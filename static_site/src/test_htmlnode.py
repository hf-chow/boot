import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLtNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
        "div",
        "Hello, world!",
        None,
        {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
                node.props_to_html(), 
                " class='greeting' href='https://boot.dev'"
                )
    def test_to_html(self):
        node = LeafNode(
                "p", "This is a paragraph of text")
        node2 = LeafNode("a", "Click me!", {"href: 'https://www.google.com'"})
        self.assertEqual(node, "<p>This is a paragraph of text.</p>")
        self.assertEqual(node2, "<a href='https://www.google.com'>Click me!</a>")

if __name__ == "__main__":
    unittest.main()
