file = open('input.txt', 'r', encoding='utf-8')
content = file.read()
file.close()

page_rule = []
page_order = []

flag = 0

for line in content.split("\n"):
    if line == "":
        flag = 1
        continue
    if flag == 1:
        numbers = [int(x) for x in line.split(",")]
        page_order.append(numbers)
    else: 
        page_rule.append((int(line.split("|")[0]), int(line.split("|")[1])))

right_order = []
incorrect_order = []

def check(order: list):
    flag = 0
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            for pair in page_rule:
                if order[i] in pair and order[j] in pair:
                    if order[i] != pair[0] and order[j] != pair[1]:
                        temp = order[i]
                        order[i] = order[j]
                        order[j] = temp
                        flag = 1
    if flag == 0:
        right_order.append(order)
    else:
        incorrect_order.append(order)
        
def get_middle_value(arr):
    if not arr:  # Kiểm tra mảng rỗng
        return None
    
    mid = len(arr) // 2  # Chia lấy phần nguyên
    
    # Nếu mảng chẵn, lấy phần tử bên trái giữa
    if len(arr) % 2 == 0:
        return arr[mid-1]
    # Nếu mảng lẻ, lấy phần tử chính giữa
    return arr[mid]



for order in page_order:
    check(order)

total = 0
# for order in right_order:
#     total += get_middle_value(order)

for order in incorrect_order:
    total += get_middle_value(order)
    
print(total)
