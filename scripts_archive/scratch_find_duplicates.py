with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's find all occurrences of "Perguntas frequentes" and "Solicite um"
import re
print("Occurrences of 'Perguntas frequentes':")
for m in re.finditer(r'Perguntas frequentes', text):
    print(" - pos:", m.start())

print("Occurrences of 'Solicite um':")
for m in re.finditer(r'Solicite um', text):
    print(" - pos:", m.start())

print("Occurrences of 'class=\"footer style-2\"':")
for m in re.finditer(r'class="footer style-2"', text):
    print(" - pos:", m.start())

print("Occurrences of 'copyright':")
for m in re.finditer(r'class="[^"]*copyright[^"]*"', text):
    print(" - pos:", m.start())
