file = open(r"C:\Users\Ольга\Downloads\kompege.ru_files_hu1aYNTAb.txt")
# file = open('test.txt')
N = int(file.readline())
K = int(file.readline())
clients = []
for line in file:
    a, b = map(int, line.split())
    clients.append([a - 420, b - 420])
    # clients.append([a, b])
clients.sort()

tables = [-1] * K
count = 0
for client in clients:
    in_time = 0
    for i in range(K):
        if tables[i] < client[0]:
            table_id = i
            in_time = 1
            break
    if in_time == 1:
        count += 1
        last_table = table_id + 1
        tables[table_id] = client[1] + 5

    else:
        min_time = 1000
        for i in range(K):
            if tables[i] < min_time:
                min_time = tables[i]
                table_id = i

        d = min_time - client[0] + 1
        if d <= 10 and client[1] + d <= 960:
            count += 1
            last_table = table_id + 1
            tables[table_id] = client[1] + 5 + d
print(count, last_table)

