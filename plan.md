# Architecture and Project Plan

---
## Flow
1. Markdown files will be in /content dir. A template.html file will be in root on project.
2. The static site generator (Python code in /src) reads MD files and the template file.
3. Generator converts the MD to a final HTML for each page and writes them to /public
4. Start a local HTTP server to serve the contents to /public.
5. Rendered site will be in browser.

---
## How it Will Work
1. Delete everything in /public
2. Copy any static assets to the /public dir
3. Generate an HTML file for each MD file in the /content dir. For each MD file:
	1. Open the file and read its contents
	2. Split the MD into "blocks"
	3. Convert each block into a tree of ```HTMLNode``` objects. For inline elements (like bold text, links etc), convert:
		- Raw markdown -> ```TextNode``` -> ```HTMLNode```
	4. Join all ```HTMLNode``` blocks under one large parent ```HTMLNode``` for the pages.
	5. Use a recursive ```to_html()``` method to convert the ```HTMLNode``` and all its nested nodes to a giant HTML string and inject it in the HTML template.
	6. Write the full HTML string to a file for that page in the ```/public``` directory.
