import os
import markdown2

print("Converting README.md to HTML...")
markdown_file = os.path.join(os.path.dirname(__file__), "..", "README.md")
html = markdown2.markdown_path(markdown_file, extras=["tables"])

html_file = os.path.join(os.path.dirname(__file__), "..", "README.html")
with open(html_file, "w+") as f:
    f.write(html)

print("Writing to README.html complete!")
