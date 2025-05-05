import os
import re
from collections import defaultdict

docs_path = 'docs'
output_file = os.path.join(docs_path, 'links.md')

link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

external_links = set()

for root, _, files in os.walk(docs_path):
    for file in files:
        if file.endswith('.md') and file != 'links.md':
            path = os.path.join(root, file)
            with open(path, encoding='utf-8') as f:
                content = f.read()
                matches = link_pattern.findall(content)
                for text, url in matches:
                    if url.startswith('http://') or url.startswith('https://'):
                        external_links.add((text.strip(), url.strip()))

# Categorize by first letter of link text
external_sorted = defaultdict(list)
for text, url in sorted(external_links, key=lambda x: x[0].lower()):
    first_letter = text[0].upper() if text else '#'
    if not first_letter.isalpha():
        first_letter = '#'
    external_sorted[first_letter].append((text, url))

# Write output to Markdown
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# Links\n\n")
    f.write("External links used across the documentation, sorted alphabetically by link text.\n\n")
    f.write("This list is generated automatically, so it may be a little messy.\n\n")

    for letter in sorted(external_sorted):
        f.write(f"## {letter}\n\n")
        for text, url in external_sorted[letter]:
            f.write(f"- [{text}]({url})\n")
        f.write("\n")
