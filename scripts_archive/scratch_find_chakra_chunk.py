import os
import glob

chunk_dir = r"C:\Users\mikaa\Downloads\www.khaledoghli.com\_next\static\chunks"
files = glob.glob(os.path.join(chunk_dir, "**", "*.js"), recursive=True)
print(f"Searching {len(files)} JS chunk files...")

found = []
for f in files:
    try:
        with open(f, "r", encoding="utf-8") as fp:
            c = fp.read()
            if "skills-chakra" in c or "chakra" in c.lower():
                found.append((f, len(c)))
    except Exception as e:
        pass

print(f"Found {len(found)} files with chakra mentions:")
for path, sz in found:
    print(f"  {os.path.basename(path)} ({sz} bytes)")
    # let's extract a snippet around chakra
    with open(path, "r", encoding="utf-8") as fp:
        c = fp.read()
        idx = c.lower().find("chakra")
        print("  Snippet:", c[max(0, idx-50):min(len(c), idx+150)])
