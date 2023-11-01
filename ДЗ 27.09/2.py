'''# Перемнные
bac = 100
a1 = 0
A1 = 10

# Типы переменных
a = 100  # int - integer - целое число
b = 1.5  # float - числа с плавающей точкой - вещественые числа
c = True  # bool - логический (True/False)
d = "Hello +_)(*2t1y4e"  # str - string - строковый

print(d + str(a))
print(type(a))

# Ввод/вывод
print(1234, a, b, "Hello")
f = int(input())
print(f)
print(type(f))

# Математические операции
print(10 + 20)
print(10 - 20)
print(10 * 20)
print(10 / 3)
print(2**10)
print(10 % 3)
print(10 // 3)

# Условия
a = int(input())
if a > 10:
    print("YAY")
elif a > 0:  # else if - иначе если
    print("positive")
elif a == 0:
    print("ZERO")
else:
    print("NAY")


# >, <, >=, <=, ==, !=

# not, and, or - не, и, или
a = int(input())
b = int(input())
if a > 10 and b > 20:
    ...


# Циклы
# for
for i in 1, 5, 8, 100, 'abc':
    print(i)
print('END')

for i in range(100):  # 0..99
    print(i)

for i in range(10, 20):  # 10..19
    print(i)

for i in range(10, 20, 2):  # 10, 12, 14, 16, 18
    print(i)

for i in "Hello":
    print(i + i)


for i in range(10):
    for j in range(10):  # вложенный
        print(i, j)

# while - пока
while True:  # бесконечный цикл
    print(123)

k = 0
while k < 10:
    print(k)
    k += 1
'''

