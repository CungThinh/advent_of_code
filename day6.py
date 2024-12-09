file = open('input.txt', 'r', encoding='utf-8')
content = file.read().strip()
line_length = 0

for i in range(len(content)):
    if content[i] == "\n":
        line_length = i;
        break;
    
content = content.replace("\n", "")
content = list(content)

guard_pos = 0
guard_direction = ""

def get_next_pos(index, guard_direction):
    direction = {
        "^": index - line_length,
        ">": index + 1,
        "v": index + line_length,
        "<": index - 1,
    }
    return direction[guard_direction]
    
def is_obstacle_in_front(index):
    next_pos = get_next_pos(index, guard_direction)
    
    if content[next_pos] == "#":
        return True, next_pos
    else: 
        return False, next_pos

def is_finished(index):
    curr_row = index // line_length
    next_pos = get_next_pos(index, guard_direction)
    
    if guard_direction == "^" and next_pos < 0:
        return True
    if guard_direction == ">" and next_pos // line_length > curr_row:
        return True
    if guard_direction == "<" and next_pos // line_length < curr_row:
        return True
    if guard_direction == "v" and next_pos > len(content):
        return True
    return False

for i, c in enumerate(content):
    if c == "^" or c == ">" or c == "v" or c == "<":
        guard_pos = i
        guard_direction = c
        content[i] = "X"
        break

next_dir = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

while not is_finished(guard_pos):
    has_obstacle, next_pos = is_obstacle_in_front(guard_pos)
    if has_obstacle:
        guard_direction = next_dir[guard_direction]
    else: 
        guard_pos = next_pos
        content[guard_pos] = "X"
    

count = 0
for c in content:
    if c == "X":
        count += 1

print(count)