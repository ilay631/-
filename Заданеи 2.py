'''a = "abcdef1234_+/*-"
n = 1234
b = str(n)


s = r"Привет\nПривет"
print(s)
# \n - символ переноса строки


a = "abc"
b = "efg"
print(a + b)
print(a * 3)

s = "abcdefgh"
#    01234567

print(s[-1])

# Срезы
print(s[2:5])
print(s[:5])
print(s[4:])

print(len(s))


s = "abcdefgh"
#    01234567
for i in s:
    print(i)

for i in range(len(s)):  # 0..7
    print(i, s[i])

for i in range(len(s) - 1):  # 0..6
    print(s[i] + s[i + 1])


s = "aaabbbAAbB"

if 'aA' in s:
    ...

print(s.count('a'))
print(s.replace('b', '2'))
print(s.replace('aa', '2'))
print(s.replace('b', '2', 2))
a = "1234512"
if a.isdigit():
    ...
print(s.isalpha())


s = "ab,cd,de,a"
print(s.split(','))
s = 'abc 123 hdf 123 jr'
print(s.split())
'''
n = 1235641762546125461245
t = str(n)
print(t.count('1'))




