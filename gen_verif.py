import os
import time

ts = int(time.time())

html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Verificação de Logos</title><style>
body {{ background: #0b1120; color: #f8fafc; font-family: system-ui, -apple-system, sans-serif; padding: 30px; }}
h1 {{ font-size: 22px; margin-bottom: 8px; color: #38bdf8; }}
p.desc {{ color: #94a3b8; font-size: 14px; margin-bottom: 24px; }}
.grid {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 20px; }}
.card {{ background: #131d33; border: 1px solid #1e293b; border-radius: 10px; padding: 18px; text-align: center; }}
.img-box {{ width: 100px; height: 100px; margin: 0 auto 12px auto; display: flex; align-items: center; justify-content: center; background: #070c18; border: 1px solid #273552; border-radius: 8px; padding: 10px; }}
.img-box img {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
h4 {{ margin: 0 0 4px 0; font-size: 15px; font-weight: 600; color: #f1f5f9; }}
p.slug {{ margin: 0; font-size: 12px; font-family: monospace; color: #64748b; }}
</style></head><body>
<h1>Auditoria das 20 Logos Oficiais da Stack</h1>
<p class="desc">Renderização visual direta dos arquivos em <code>assets/logos/</code> (Timestamp: {ts})</p>
<div class="grid">
"""

files = [
    ('claude.png', 'Claude 3.5 Sonnet'),
    ('gpt.png', 'ChatGPT / GPT-4o'),
    ('hermes.png', 'Nous Hermes'),
    ('gemini.png', 'Google Gemini 2.5'),
    ('n8n.png', 'n8n Workflows'),
    ('supabase.png', 'Supabase'),
    ('gsap.png', 'GSAP'),
    ('nextjs.png', 'Next.js'),
    ('react.png', 'React'),
    ('typescript.png', 'TypeScript'),
    ('python.png', 'Python'),
    ('fastapi.png', 'FastAPI'),
    ('threejs.png', 'Three.js'),
    ('tailwind.png', 'Tailwind CSS'),
    ('docker.png', 'Docker'),
    ('postgresql.png', 'PostgreSQL'),
    ('nodejs.png', 'Node.js'),
    ('redis.png', 'Redis'),
    ('git.png', 'Git'),
    ('vercel.png', 'Vercel')
]

for f, name in files:
    html += f'<div class="card"><div class="img-box"><img src="assets/logos/{f}?ts={ts}" alt="{name}"></div><h4>{name}</h4><p class="slug">{f}</p></div>\n'

html += """</div></body></html>"""

with open("verificacao-logos.html", "w", encoding="utf-8") as out:
    out.write(html)
print("verificacao-logos.html regerado com timestamp fresco!")
