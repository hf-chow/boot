from textnode import TextNode
from htmlnode import LeafNode

def main():
    test_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(test_node)

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        text_node = LeafNode(None, text_node.text)
    if text_node.text_type == "bold":
        text_node = LeafNode("b", text_node.text)
    if text_node.text_type == "italic":
        text_node = LeafNode("i", text_node.text)
    if text_node.text_type == "code":
        text_node = LeafNode("code", text_node.text)
    if text_node.text_type == "link":
        text_node = LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == "img":
        text_node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception("Type not supported")



if __name__ == "__main__":
    main()

