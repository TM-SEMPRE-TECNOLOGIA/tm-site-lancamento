import urllib.request
import os

icons_meta = [
    {"slug": "claude", "file": "claude.png", "color": "#D97757", "name": "Claude"},
    {"slug": "openai", "file": "gpt.png", "color": "#10A37F", "name": "ChatGPT"},
    {"slug": "googlegemini", "file": "gemini.png", "color": "#38BDF8", "name": "Google Gemini"},
    {"slug": "n8n", "file": "n8n.png", "color": "#FF6D5A", "name": "n8n"},
    {"slug": "supabase", "file": "supabase.png", "color": "#3ECF8E", "name": "Supabase"},
    {"slug": "greensock", "file": "gsap.png", "color": "#88CE02", "name": "GSAP"},
    {"slug": "nextdotjs", "file": "nextjs.png", "color": "#FFFFFF", "name": "Next.js"},
    {"slug": "react", "file": "react.png", "color": "#61DAFB", "name": "React"},
    {"slug": "typescript", "file": "typescript.png", "color": "#3178C6", "name": "TypeScript"},
    {"slug": "fastapi", "file": "fastapi.png", "color": "#009688", "name": "FastAPI"},
    {"slug": "threedotjs", "file": "threejs.png", "color": "#FFFFFF", "name": "Three.js"},
    {"slug": "tailwindcss", "file": "tailwind.png", "color": "#06B6D4", "name": "Tailwind CSS"},
    {"slug": "docker", "file": "docker.png", "color": "#2496ED", "name": "Docker"},
    {"slug": "postgresql", "file": "postgresql.png", "color": "#4169E1", "name": "PostgreSQL"},
    {"slug": "nodedotjs", "file": "nodejs.png", "color": "#5FA04E", "name": "Node.js"},
    {"slug": "redis", "file": "redis.png", "color": "#DC382D", "name": "Redis"},
    {"slug": "git", "file": "git.png", "color": "#F05032", "name": "Git"},
    {"slug": "vercel", "file": "vercel.png", "color": "#FFFFFF", "name": "Vercel"},
    {"slug": "python", "file": "python.png", "color": "#FFD43B", "name": "Python"}
]

os.makedirs("temp_svgs", exist_ok=True)
svg_dict = {}

for item in icons_meta:
    url = f"https://cdn.jsdelivr.net/npm/simple-icons@v13/icons/{item['slug']}.svg"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode("utf-8")
            # Save raw svg
            with open(f"temp_svgs/{item['slug']}.svg", "w", encoding="utf-8") as sf:
                sf.write(content)
            svg_dict[item["slug"]] = content
            print(f"Downloaded {item['slug']}")
    except Exception as e:
        print(f"Error {item['slug']}: {e}")

print("Done downloading SVGs!")
