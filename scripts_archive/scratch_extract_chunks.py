import os

chunk_dir = r"C:\Users\mikaa\Downloads\www.khaledoghli.com\_next\static\chunks"
target = os.path.join(chunk_dir, "0sq1f.k7x33nq.js")

with open(target, "r", encoding="utf-8") as f:
    code = f.read()

print("Chunk length:", len(code))
with open("khaled_extracted_skills_shader.js", "w", encoding="utf-8") as out:
    out.write(code)

print("Saved to khaled_extracted_skills_shader.js")

# Let's also inspect 0t6vn810y7eqp.js
target2 = os.path.join(chunk_dir, "0t6vn810y7eqp.js")
with open(target2, "r", encoding="utf-8") as f:
    code2 = f.read()
with open("khaled_extracted_skills_ui.js", "w", encoding="utf-8") as out:
    out.write(code2)

print("Saved to khaled_extracted_skills_ui.js")
