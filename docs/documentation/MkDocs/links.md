---
Title: Extract External Links and Group by Name
Summary: A guide to creating a script that extracts all external links from documents and organizes them alphabetically by name on a single page.
Author:
  - Peter de Ruyter
Date: 2025-05-05
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# Links

## Extract External Links and Group by Name
   Extract and organize external links from documentation.

## Overview
   This guide explains how to create a script that scans all Markdown documents in a project, extracts external links, and generates a page listing them alphabetically grouped by their names.

### Technical Details
   - **Input**: Markdown files in the `docs` directory.
   - **Output**: A Markdown file (`links.md`) containing all external links grouped alphabetically.
   - **Tools**: Python, `os` module, `re` module.
   - **Outcome**: A centralized page for external links, improving navigation and accessibility.

### Infobox
   **Key Facts**:
   - **Language**: Python
   - **Platform**: MkDocs
   - **Features**: External link extraction, alphabetical grouping, Markdown generation.
   - **Use Case**: Documentation projects with numerous external references.

---

## Steps

### 1. Create the Script
   Write a Python script to extract external links and generate the `links.md` file.

   ```python
   # filepath: mkdocs.py
   import os
   import re
   from collections import defaultdict

   docs_path = 'docs'
   output_file = os.path.join(docs_path, 'links.md')

   link_pattern = re.compile(r'\[([^\]]+)\]\((http[s]?://[^\)]+)\)')

   external_links = set()

   for root, _, files in os.walk(docs_path):
       for file in files:
           if file.endswith('.md') and file != 'links.md':
               path = os.path.join(root, file)
               with open(path, encoding='utf-8') as f:
                   content = f.read()
                   matches = link_pattern.findall(content)
                   for text, url in matches:
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
       for letter in sorted(external_sorted):
           f.write(f"## {letter}\n\n")
           for text, url in external_sorted[letter]:
               f.write(f"- [{text}]({url})\n")
           f.write("\n")
   ```
   {: .code-copy }

### 2. Run the Script
   Execute the script to generate the `links.md` file.

   ```bash
   python mkdocs.py
   ```
   {: .code-copy }

### 3. Add the Generated Page to MkDocs
   Update the `mkdocs.yml` file to include the `links.md` page in the navigation.

   ```yaml
   nav:
     - Home: index.md
     - Links: links.md
   ```
   {: .code-copy }

### 4. Serve the Documentation Locally
   Test the changes by serving the documentation locally.

   ```bash
   mkdocs serve
   ```
   {: .code-copy }

   Open your browser and navigate to `http://127.0.0.1:8000` to verify the `Links` page.

---

## Examples

### Example Output in `links.md`
   ```markdown
   # Links

   External links used across the documentation, sorted alphabetically by link text.

   ## A
   - [API Documentation](https://api.example.com)

   ## G
   - [GitHub](https://github.com)

   ## M
   - [MkDocs](https://www.mkdocs.org)
   ```

---

## Resources
   - [Python Documentation](https://docs.python.org/3/)
   - [MkDocs Official Documentation](https://www.mkdocs.org/)
   - [Regular Expressions in Python](https://docs.python.org/3/library/re.html)

---

## Troubleshooting

### Issue: Script Does Not Detect Links
   **Resolution**: Ensure the Markdown files follow the `[text](url)` format for links.

### Issue: `links.md` Not Generated
   **Resolution**: Verify the script's file paths and permissions.

### Issue: Links Page Not Visible in Navigation
   **Resolution**: Check the `mkdocs.yml` file for correct navigation configuration.

---

*Generated using AI*