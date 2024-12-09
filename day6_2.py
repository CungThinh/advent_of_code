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
    
def is_obstacle_in_front(index, matrix):
    next_pos = get_next_pos(index, guard_direction)
    
    if matrix[next_pos] == "#" or matrix[next_pos] == "0":
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
        break

next_dir = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

count = 0
initial_guard_pos = guard_pos
initial_guard_dir = guard_direction

for i, c in enumerate(content):
    matrix = content.copy()
    matrix[i] = "0"
    visited_states = set() 
    guard_pos = initial_guard_pos
    guard_direction = initial_guard_dir
    while not is_finished(guard_pos):
        current_state = (guard_pos, guard_direction)
        if current_state in visited_states:
            count += 1
            break
        
        visited_states.add(current_state)
        
        has_obstacle, next_pos = is_obstacle_in_front(guard_pos, matrix)
        if has_obstacle:
            guard_direction = next_dir[guard_direction]
        else: 
            guard_pos = next_pos
        
print(count)