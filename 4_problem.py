file = open('input.txt', 'r', encoding='utf-8')
content = file.read()
file.close()

line_length = 0

for i in range(len(content)):
    if content[i] == "\n":
        line_length = i;
        break;

count = 0
content = content.replace("\n", "")

def check_horizontal(content, i):
    found_count = 0
    string = ""
    for j in range(0, 4):
        index = i + (j * line_length)
        if index < 0 or index >= len(content):
            break;
        string += content[index]
        
    if string == "XMAS":
        found_count += 1
        
    string = ""
        
    for j in range(0, 4):
        index = i - (j * line_length)
        if index < 0 or index >= len(content):
            break;
        string += content[index]

    if string == "XMAS":
        found_count += 1
    
    return found_count

def check_diagonal(content, i):
    curr_row = i // line_length
    curr_col = i % line_length 
    found_count = 0
    
    # Chéo xuống phải
    string = ""
    for j in range(0, 4):
        index = i + (j * (line_length + 1))
        if index < 0 or index >= len(content):
            break
        new_row = index // line_length
        new_col = index % line_length
        # Row và col phải tăng
        if (new_row - curr_row) != j or (new_col - curr_col) != j:
            break
        string += content[index]
        
    if string == "XMAS":
        found_count += 1
        
    # Chéo lên trái
    string = ""
    for j in range(0, 4):
        index = i - (j * (line_length + 1))
        if index < 0 or index >= len(content):
            break
        new_row = index // line_length
        new_col = index % line_length
        # Row và col phải giảm
        if (curr_row - new_row) != j or (curr_col - new_col) != j:
            break
        string += content[index]
        
    if string == "XMAS":
        found_count += 1
        
    # Chéo lên phải
    string = ""
    for j in range(0, 4):
        index = i - (j * (line_length - 1))
        if index < 0 or index >= len(content):
            break
        new_row = index // line_length
        new_col = index % line_length
        # Row giảm, col tăng
        if (curr_row - new_row) != j or (new_col - curr_col) != j:
            break
        string += content[index]
        
    if string == "XMAS":
        found_count += 1

    # Chéo xuống trái
    string = ""
    for j in range(0, 4):
        index = i + (j * (line_length - 1))
        if index < 0 or index >= len(content):
            break
        new_row = index // line_length
        new_col = index % line_length
        # Row tăng, col giảm
        if (new_row - curr_row) != j or (curr_col - new_col) != j:
            break
        string += content[index]
        
    if string == "XMAS":
        found_count += 1
        
    return found_count


for i in range(len(content)):
    curr_row = i // line_length
    curr_col = i % line_length
    
    # Kiểm tra ngang phải
    if curr_col + 4 <= line_length:  # Đảm bảo không vượt quá độ dài hàng
        if content[i: i + 4] == "XMAS":
            count += 1
            
    if curr_col >= 3:  # Đảm bảo có đủ ký tự phía trước
        if content[i-4: i][::-1] == "XMAS":
            count += 1
    
    count += check_horizontal(content, i)
    count += check_diagonal(content, i)

print(count)