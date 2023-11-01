'''# Строки
a = "abcde123-="
n = 1234
b = str(n)

# Специальное символы
s = "abcde\tHello"
# \n - символ переноса строки
# \t - символ табуляции
print(s)


# Операции со строками
a = 'abc'
b = 'defg'
# Математические
print(a + b)
print(a * 3)  # a + a + a

# Логические операции
print(a > b)
print('1' > '120')
# aa
# ab
# ac
# ...
# ba
# bb


# Индексы
s = 'abcdefgh'
#    01234567
#           -1
if s[0] == 'b':
    ...
print(s[-1])
print(s[10])  # IndexError


# Срезы
s = 'abcdefgh'
#    01234567
print(s[2:5])
print(s[2:])
print(s[:5])

# Методы и фунции строк
s = 'aabbAAbAba'
print(len(s))  # Считает длину строки
print(s.count('ab'))  # Считает сколько раз что-то встречается в строке
print(s.replace('a', '1'))  # Заменяет что-то на что-то в строке
print(s.replace('b', ''))
s1 = '1231247654271648'
print(s1.isdigit())  # Проверяет состоит ли строка только из цифр
print(s.isalpha())  # Проверяет состоит ли строка только из букв

if s.isdigit():
    ...
if s.count('a') == 3:
    ...

s = 'aabbAAbAba'
print('ac' in s)  # Проверяет есть ли что-то в чем-то
print('ac' not in s)
if 'abc' in s:
    ...
'''

n = int(input())
a = str(n)
print(a.count('1'))



