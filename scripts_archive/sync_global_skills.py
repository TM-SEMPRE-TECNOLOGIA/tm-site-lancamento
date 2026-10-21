import os
import shutil

src_base = r"c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\.agents\skills"
dst_base = r"C:\Users\mikaa\.gemini\config\skills"

skills_to_sync = [
    "designer-skills",
    "inclusive-design-skills",
    "wireframer-skill",
    "motion-design-skill",
    "color-expert-skill",
    "icon-generator-skill",
    "responsive-craft",
    "brand-to-design-md-skill",
    "ux-flow-designer",
    "frontend-designer-skill",
    "landing-page-design"
]

os.makedirs(dst_base, exist_ok=True)

for skill in skills_to_sync:
    src = os.path.join(src_base, skill)
    dst = os.path.join(dst_base, skill)
    if os.path.exists(src):
        if not os.path.exists(dst):
            print(f"Syncing {skill} to global skills directory...")
            try:
                shutil.copytree(src, dst, dirs_exist_ok=True)
                print(f"[SYNCED] {skill}")
            except Exception as e:
                print(f"[ERROR SYNC] {skill}: {e}")
        else:
            print(f"[ALREADY GLOBAL] {skill}")

print("Sync completed!")
