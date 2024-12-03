import re
file = open('input.txt', 'r', encoding='utf-8')
content = file.read()
file.close()

# content = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

enable =  True
pattern = r'(do|don\'t)\(\)|mul\((\d+),(\d+)\)'
matches = re.finditer(pattern, content)
total = 0;
for match in matches:
    if match.group(1) == "don't":
        enable = False
        continue
    if match.group(1) == "do":
        enable =  True
        continue
    if match.group(1) is None and enable:
        total += int(match.group(2)) * int(match.group(3));
    
print(total);
        
    
