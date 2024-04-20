import re

from textnode import (
        TextNode, 
        text_type_bold, 
        text_type_code, 
        text_type_link, 
        text_type_bold,
        text_type_text,
        text_type_image,
        text_type_italic
        )

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        splits = []
        segements = node.text.split(delimeter)
        if len(segements) % 2 == 0:
            raise ValueError("Invalid markdown syntax")

        for i in range(len(segements)):
            if segements[i] == "":
                continue
            if i % 2 == 0:
                splits.append(TextNode(segements[i], text_type_text))
            else:
                splits.append(TextNode(segements[i], text_type))
        new_nodes.extend(splits)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:

        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        original_text = node.text

        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue

        for image in images:
            tag = image[0]
            url = image[1]
            segements = original_text.split(
                    f"![{tag}]({url})", 
                    maxsplit = 1
                    )
            if len(segements) != 2:
                raise ValueError("Invalid markdown syntax, problematic image section")
            if segements[0] != "":
                new_nodes.append(TextNode(segements[0], text_type_text))

            new_nodes.append(TextNode(tag, text_type_image, url=url))
            original_text = segements[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))

    return new_nodes
    


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
           new_nodes.append(node)
           continue

        original_text = node.text

        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            tag = link[0]
            url = link[1]
            segements = original_text.split(
                    f"[{tag}]({url})", 
                    maxsplit = 1
                    )
            if len(segements) != 2:
                raise ValueError("Invalid markdown syntax, problematic link section")
            if segements[0] != "":
                new_nodes.append(TextNode(segements[0], text_type_text))

            new_nodes.append(TextNode(tag, text_type_link, url=url))
            original_text = segements[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))

    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
