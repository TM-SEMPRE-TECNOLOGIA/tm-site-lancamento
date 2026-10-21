with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
print("Occurrences of 'Perguntas frequentes':", len(re.findall(r'Perguntas frequentes', text)))
print("Occurrences of 'Solicite um':", len(re.findall(r'Solicite um', text)))
print("Occurrences of 'footer style-2':", len(re.findall(r'footer style-2', text)))
print("Occurrences of 'copyrights':", len(re.findall(r'class="algin-center copyrights"', text)))

# Print the last 1500 chars of index.html
print("\n--- END OF FILE ---")
print(text[-2000:])
