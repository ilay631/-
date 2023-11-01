file = open(r"C:\Users\Ольга\Downloads\26_9793.txt")
N = int(file.readline())
grinding = []
coloring = []
for i, line in enumerate(file):
    a, b = map(int, line.split())
    grinding.append((a, i + 1))
    coloring.append((b, i + 1))

grinding.sort()
coloring.sort()
belt = [0] * N
left = 0
right = N - 1
while len(grinding) != 0 and len(coloring) != 0:
    if grinding[0][0] < coloring[0][0]:
        if grinding[0][1] not in belt:
            belt[left] = grinding[0][1]
            left += 1
        grinding.pop(0)
    elif grinding[0][0] > coloring[0][0]:
        if coloring[0][1] not in belt:
            belt[right] = coloring[0][1]
            right -= 1
        coloring.pop(0)

print(belt[left - 1], left - 1)

