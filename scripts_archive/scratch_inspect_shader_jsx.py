with open('khaled_extracted_skills_shader.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the component structure
print("File size:", len(text))
# search for 'export' or React component function
import re
functions = re.findall(r'function\s+([a-zA-Z0-9_$]+)\s*\([^)]*\)\s*\{', text)
print("Function names:", set(functions[:20]))

# Search for return ( or JSX in this file
jsx_tags = re.findall(r'\.jsx\)\s*\(\s*["\']([a-zA-Z0-9_-]+)["\']', text)
print("JSX elements created in shader chunk:", set(jsx_tags))
