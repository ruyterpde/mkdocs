import xml.etree.ElementTree as ET
from urllib.parse import urlparse
from pathlib import Path
from collections import defaultdict

# CONFIGURATION
SITEMAP_PATH = "site/sitemap.xml"
OUTPUT_MD = "docs/sitemap.md"
SITE_URL = "https://dms.ruyter.og"  # Change to your actual site URL


def parse_sitemap(sitemap_path):
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    # Include all URLs
    urls = [
        url.find("ns:loc", ns).text
        for url in root.findall("ns:url", ns)
    ]
    return urls


def build_tree(paths):
    tree = lambda: defaultdict(tree)
    root = tree()
    for path in paths:
        parts = path.strip("/").split("/")
        current = root
        for part in parts:
            # Check if the part is part of the "blog" section
            if "/blog/" in "/".join(parts):
                current['blog'] = {}  # Add a single "blog" node without expanding
                break  # Stop expanding the blog section further
            current = current[part]
    return root


def format_label(slug):
    # Replace underscores with spaces and capitalize each word
    return slug.replace("_", " ").title() if slug else "Home"


def walk_tree(node, parent_id=None, prefix="N", counter=[0], path_parts=[], mermaid_lines=[], click_lines=[]):
    for key in sorted(node.keys()):
        counter[0] += 1
        node_id = f"{prefix}{counter[0]}"
        label = format_label(key)
        full_path = "/" + "/".join(path_parts + [key]) + ("/" if key else "")

        # If it's the "blog" section, we don't expand it further
        if key == "blog":
            label = "Blog"
            full_path = "/blog/"
        
        mermaid_lines.append(f'{node_id}["{label}"]')
        if parent_id:
            mermaid_lines.append(f"{parent_id} --> {node_id}")
        click_lines.append(f'click {node_id} "{full_path}"')

        # If it's not the blog section, walk deeper
        if key != "blog":
            walk_tree(node[key], node_id, prefix, counter, path_parts + [key], mermaid_lines, click_lines)

    return mermaid_lines, click_lines


def generate_mermaid(tree_dict):
    mermaid_lines, click_lines = walk_tree(tree_dict, None)
    # Change layout to 'LR' (left-right) for vertical orientation
    return "\n".join(["```mermaid", "graph LR"] + mermaid_lines + click_lines + ["```"])


def write_markdown(output_path, mermaid_code):
    md_content = "# Sitemap\n\n" + mermaid_code + "\n"
    Path(output_path).write_text(md_content, encoding="utf-8")


def main():
    urls = parse_sitemap(SITEMAP_PATH)
    paths = [urlparse(u).path for u in urls if not u.endswith("sitemap.xml")]
    tree_dict = build_tree(paths)
    mermaid_code = generate_mermaid(tree_dict)
    write_markdown(OUTPUT_MD, mermaid_code)


if __name__ == "__main__":
    main()

print("INFO    -  Successfully generated sitemap.md")