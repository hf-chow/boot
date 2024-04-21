block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    splits = markdown.split("\n\n")
    results = [s.strip() for s in splits if s != ""]
    return results

def block_to_block_type(md_block):
    if md_block[:2] == "# ":
        return block_type_heading
    if md_block[:3] == "## ":
        return block_type_heading
    if md_block[:4] == "### ":
        return block_type_heading
    if md_block[:5] == "#### ":
        return block_type_heading
    if md_block[:6] == "##### ":
        return block_type_heading
    if md_block[:7] == "######":
        return block_type_heading

    if md_block[:3] == "```" and md_block[-3:] == "```":
        return block_type_code

    lines = md_block.split("\n")

    if md_block[0] == ">":
        for line in lines:
            if line[0] != ">":
                return block_type_paragraph
        return block_type_quote

    if md_block[0] == "*":
        for line in lines:
            if line[0] != "*":
                return block_type_paragraph
        return block_type_unordered_list

    if md_block[:2] == "- ":
        for line in lines:
            if line[:2] != "- ":
                return block_type_paragraph
        return block_type_unordered_list

    if md_block[:3] == "1. ":
        i = 1
        for line in lines:
            print(line[:3])
            if line[:3] != f"{i}. ":
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    return block_type_paragraph
