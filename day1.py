file = open('input.txt', 'r', encoding='utf-8')
content = file.read()
file.close()

pairs = []
for line in content.split('\n'):
    left, right = map(int, line.split())
    pairs.append((left, right))
    
left_nums = [pair[0] for pair in pairs]
right_nums = [pair[1] for pair in pairs]

similarity_score = 0

for x in left_nums:
    similarity_score += int(x) * right_nums.count(x);

print(similarity_score)    
    
