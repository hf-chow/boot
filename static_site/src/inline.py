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

