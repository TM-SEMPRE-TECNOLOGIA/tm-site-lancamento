with open('upolitico-clone/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
start_idx = html.find('class="banner style-3"')
end_idx = html.find('<div class="waves-bottom2"></div>')
if start_idx != -1 and end_idx != -1:
    print("--- HERO HTML ---")
    print(html[start_idx-20:end_idx+60])
