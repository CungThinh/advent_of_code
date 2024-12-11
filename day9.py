file = open('input.txt', 'r', encoding='utf-8')
content = file.read().strip()

i = 0
switch = 0
new_string = ""

for c in content:
    if switch == 0:
        for j in range(0, int(c)):
            new_string += f"{i}"
        i += 1
        switch = 1
    else:
        for j in range(0, (int(c))):
            new_string += "."
        switch = 0
        
new_string = list(new_string)
last_digit_index = 0

for j in range(len(new_string)):
    for i in range(len(new_string) - 1, j,  -1):
        if new_string[i] != ".":
            last_digit_index = i
            break
    if j == last_digit_index:
        break
    if new_string[j] == ".":
        new_string[j] = new_string[last_digit_index]
        new_string[last_digit_index] = "."

total = 0
for i in range(len(new_string)):
    if new_string[i] != ".":
        total += i * int(new_string[i])
    
print(total)
        
    