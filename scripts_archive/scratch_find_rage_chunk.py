import os
import glob

chunk_dir = r"C:\Users\mikaa\Downloads\www.khaledoghli.com\_next\static\chunks"
files = glob.glob(os.path.join(chunk_dir, "**", "*.js"), recursive=True)

for f in files:
    try:
        with open(f, "r", encoding="utf-8") as fp:
            c = fp.read()
            if "skeleton-rage-layer" in c:
                print(f"Found in {os.path.basename(f)} ({len(c)} bytes)")
                pos = c.find("skeleton-rage-layer")
                print("Snippet:", c[max(0, pos-150):min(len(c), pos+400)])
    except:
        pass
