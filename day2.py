file = open('input.txt', 'r', encoding='utf-8')
content = file.read()
file.close()

def is_safe(a):
    if is_increasing(a) and is_valid_diff_amount(a):
        return True
    elif is_decreasing(a) and is_valid_diff_amount(a):
        return True
    else:
        return False

def is_increasing(a):
    for i in range(len(a) - 1):
        if a[i] <= a[i+1]:
            return False;
    return True

def is_decreasing(a):
    for i in range(0, len(a) - 1):
        if a[i] >= a[i+1]:
            return False;
    return True

def is_valid_diff_amount(a):
    for i in range(len(a) - 1):
        diff = abs(int(a[i]) - int(a[i + 1]))
        if diff > 3 or diff == 0: 
            return False
    return True

def dampener(a: list) :
    for i in range(len(a)):
        test = a[:i] + a[i+1:]
        if is_safe(test):
            return True
    return False

arrays = []
for line in content.split('\n'):
    numbers = [int(x) for x in line.split()]
    arrays.append(numbers)

count = 0
for array in arrays:
    if is_safe(array) or dampener(array):
        count += 1

print(count)
    