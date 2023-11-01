# Цикл for и while
"""for i in 1, 5, 30, 40, 1, 2:
    print(i % 10)

for i in range(100):  # 0..99
    print(i)

for i in range(10, 20):  # 10..19
    print(i)

for i in range(10, 20, 2):  # 10, 12, 14, 16, 18
    print(i)

for i in "Hello":
    print(i * 2)
print("END")


# Цикл while
while True:  # бесконечный цикл
    print(12431246124)


k = 10
while k < 20:
    print(k)
    k += 2  # k = k + 2


# break, continue - сломать, продолжить

for i in range(1, 100):
    print(i)
    if i % 25 == 0 and i % 3 == 0:
        break


for i in range(5000):
    if i % 2 == 0:
        continue
    print(i)


for i in range(10):
    break
    print(i)
"""

for i in range(10):
    for j in range(10):  # вложенный цикл
        print(i, j)
