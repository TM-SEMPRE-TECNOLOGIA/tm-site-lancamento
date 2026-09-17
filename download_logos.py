import os
import urllib.request
import json

LOGOS_DIR = r"C:\Users\mikaa\Documents\antigravity\tm-site-lancamento\assets\logos"
os.makedirs(LOGOS_DIR, exist_ok=True)

# Dicionário de URLs de alta resolução (PNG com cores reais de cada marca)
SOURCES = {
    "claude.png": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Anthropic_logo.svg/512px-Anthropic_logo.svg.png",
        "https://avatars.githubusercontent.com/u/76263028?s=280&v=4"
    ],
    "gpt.png": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/512px-ChatGPT_logo.svg.png",
        "https://avatars.githubusercontent.com/u/14957082?s=280&v=4"
    ],
    "hermes.png": [
        "https://avatars.githubusercontent.com/u/105342415?s=280&v=4"  # Nous Research oficial
    ],
    "supabase.png": [
        "https://avatars.githubusercontent.com/u/54469796?s=280&v=4",  # Supabase oficial
        "https://raw.githubusercontent.com/supabase/supabase/master/packages/common/assets/images/supabase-logo-icon.png"
    ],
    "n8n.png": [
        "https://avatars.githubusercontent.com/u/45487711?s=280&v=4"   # n8n oficial
    ],
    "gsap.png": [
        "https://avatars.githubusercontent.com/u/2329415?s=280&v=4"    # GreenSock oficial
    ],
    "nextjs.png": [
        "https://raw.githubusercontent.com/github/explore/main/topics/nextjs/nextjs.png",
        "https://assets.vercel.com/image/upload/v1662130559/nextjs/Icon_dark_background.png"
    ],
    "python.png": [
        "https://raw.githubusercontent.com/github/explore/main/topics/python/python.png"
    ],
    "fastapi.png": [
        "https://raw.githubusercontent.com/github/explore/main/topics/fastapi/fastapi.png",
        "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    ],
    "typescript.png": [
        "https://raw.githubusercontent.com/github/explore/main/topics/typescript/typescript.png"
    ],
    "threejs.png": [
        "https://raw.githubusercontent.com/github/explore/main/topics/threejs/threejs.png"
    ],
    "tailwind.png": [
        "https://raw.githubusercontent.com/github/explore/main/topics/tailwind/tailwind.png"
    ],
    "docker.png": [
        "https://raw.githubusercontent.com/github/explore/main/topics/docker/docker.png"
    ],
    "gemini.png": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Google_Gemini_logo.svg/512px-Google_Gemini_logo.svg.png",
        "https://raw.githubusercontent.com/google-gemini/cookbook/main/images/gemini_logo.png"
    ],
    "postgresql.png": [
        "https://raw.githubusercontent.com/github/explore/main/topics/postgresql/postgresql.png"
    ],
    "react.png": [
        "https://raw.githubusercontent.com/github/explore/main/topics/react/react.png"
    ]
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

results = {}

for filename, urls in SOURCES.items():
    dest_path = os.path.join(LOGOS_DIR, filename)
    success = False
    for url in urls:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                content = response.read()
                if len(content) > 100:
                    with open(dest_path, "wb") as f:
                        f.write(content)
                    results[filename] = f"OK ({len(content)} bytes) from {url}"
                    success = True
                    break
        except Exception as e:
            continue
    if not success:
        results[filename] = "FAILED"

print(json.dumps(results, indent=2))
