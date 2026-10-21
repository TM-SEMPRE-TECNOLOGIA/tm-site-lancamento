with open(r'C:\Users\mikaa\Downloads\www.khaledoghli.com\_next\static\chunks\04nwbzv778w-3.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in CSS: {len(lines)}")
start = max(0, 18890)
end = min(len(lines), 18950)
for i in range(start, end):
    print(f"{i+1}: {lines[i].strip()}")
