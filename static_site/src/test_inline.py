import unittest

from inline import (
        split_nodes_delimiter,
        extract_markdown_images,
        extract_markdown_links
        )

from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code
)

class TestInline(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
                [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("bolded", text_type_bold),
                    TextNode(" word", text_type_text),
                    ], 
                new_nodes
                )
    def test_delim_bold_double(self):
        node = TextNode("This text has **two** separately **bolded** words", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
                [ 
                    TextNode("This text has ", text_type_text),
                    TextNode("two", text_type_bold),
                    TextNode(" separately ", text_type_text),
                    TextNode("bolded", text_type_bold),
                    TextNode(" words", text_type_text)
                    ],
                new_nodes
                )

    def test_delim_bold_multiword(self):
        node = TextNode("This text has a **multiword bolded** text" , text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
                [
                    TextNode("This text has a " , text_type_text),
                    TextNode("multiword bolded", text_type_bold),
                    TextNode(" text", text_type_text)
                ],
                new_nodes
                )

    def test_delim_italic(self):
        node = TextNode("This text has a *itallic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
                [
                    TextNode("This text has a ", text_type_text),
                    TextNode("itallic", text_type_italic),
                    TextNode(" word", text_type_text)
                ], 
                new_nodes
                )
    def test_delilm_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
                [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode(" word", text_type_text)
                ], 
                new_nodes
                )

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/\
                qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and \
                ![another](https://storage.googleapis.com/qvault-webapp-\
                dynamic-assets/course_assets/dfsdkjfd.png)"
        extracted = [
                ("image", "https://storage.googleapis.com/\
                qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                ("another", "https://storage.googleapis.com/qvault-webapp-\
                dynamic-assets/course_assets/dfsdkjfd.png")]

        self.assertListEqual(extract_markdown_images(text), extracted)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and \
                [another](https://www.example.com/another)"
        extracted = [
                ("link","https://www.example.com"),
                ("another", "https://www.example.com/another")                 ]
        self.assertListEqual(extract_markdown_links(text), extracted)



if __name__ == "__main__":
    unittest.main()
