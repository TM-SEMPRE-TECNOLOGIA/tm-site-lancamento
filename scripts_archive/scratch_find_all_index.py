import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if f == 'index.html' and 'node_modules' not in root and '.git' not in root:
            print(os.path.join(root, f))
