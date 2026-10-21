import os
import subprocess

skills = [
    {"name": "designer-skills", "url": "https://github.com/Owl-Listener/designer-skills.git"},
    {"name": "inclusive-design-skills", "url": "https://github.com/Owl-Listener/inclusive-design-skills.git"},
    {"name": "wireframer-skill", "url": "https://github.com/agilek/wireframer-skill.git"},
    {"name": "motion-design-skill", "url": "https://github.com/LottieFiles/motion-design-skill.git"},
    {"name": "color-expert-skill", "url": "https://github.com/meodai/skill.color-expert.git"},
    {"name": "icon-generator-skill", "url": "https://github.com/anhao/icon-generator-skill.git"},
    {"name": "responsive-craft", "url": "https://github.com/kylezantos/responsive-craft.git"},
    {"name": "brand-to-design-md-skill", "url": "https://github.com/shaom/brand-to-design-md-skill.git"},
    {"name": "ux-flow-designer", "url": "https://github.com/ThomasPraun/ux-flow-designer.git"},
    {"name": "frontend-designer-skill", "url": "https://github.com/kozz36/frontend-designer-skill.git"}
]

base_dir = r"c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\.agents\skills"
os.makedirs(base_dir, exist_ok=True)

for s in skills:
    target = os.path.join(base_dir, s["name"])
    if os.path.exists(target):
        print(f"[ALREADY EXISTS] {s['name']}")
    else:
        print(f"[CLONING] {s['name']} from {s['url']}...")
        try:
            res = subprocess.run(["git", "clone", "--depth", "1", s["url"], target], capture_output=True, text=True)
            if res.returncode == 0:
                print(f"[SUCCESS] {s['name']}")
            else:
                print(f"[ERROR] {s['name']}: {res.stderr}")
        except Exception as e:
            print(f"[EXCEPTION] {s['name']}: {e}")

print("\nVerifying SKILL.md in each cloned repository...")
for s in skills:
    target = os.path.join(base_dir, s["name"])
    if os.path.exists(target):
        files = os.listdir(target)
        has_skill_md = any(f.lower() == "skill.md" for f in files)
        has_readme = any(f.lower() == "readme.md" for f in files)
        print(f"-> {s['name']}: SKILL.md={has_skill_md}, README.md={has_readme}")
        
        # If no SKILL.md exists, let's create one referencing the skill instructions if needed
        skill_md_path = os.path.join(target, "SKILL.md")
        if not has_skill_md and has_readme:
            readme_path = os.path.join(target, "README.md")
            try:
                with open(readme_path, "r", encoding="utf-8", errors="ignore") as rf:
                    content = rf.read()
                header = f"---\nname: {s['name']}\ndescription: Open source design skill\n---\n\n"
                with open(skill_md_path, "w", encoding="utf-8") as wf:
                    wf.write(header + content)
                print(f"   Created SKILL.md from README for {s['name']}")
            except Exception as ex:
                print(f"   Failed to create SKILL.md: {ex}")
