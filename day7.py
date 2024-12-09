from itertools import product
file = open('input.txt', 'r', encoding='utf-8')
content = file.read().strip()
line_length = 0

total = 0
operation = ["+" , "*", "||"]
    
for line in content.split('\n'):
    result = line.split(':')[0]
    element = line.split(':')[1].split()
    
    for combo in list(product(operation, repeat = len(element) - 1)):
        ans = int(element[0])
        for i in range(1, len(element)):
            if combo[i - 1] == "+":
                ans += int(element[i])
            elif combo[i - 1] == "||":
                ans = int(f"{ans}{element[i]}")
            else:
                ans *= int(element[i])
        if ans == int(result):
            total += ans
            break;
            
print(total)