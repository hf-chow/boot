import unittest
from htmlnode import HTMLNode

class TestHTMLtNode(unittest.TestCase):
    def test_to_html_pops(self):
        node = HTMLNode(
        "div",
        "Hello, world!",
        None,
        {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(node.props_to_html(), " class='greeting' href='https://boot.dev'")


if __name__ == "__main__":
    unittest.main()
