'''print(bin(100))  # Переводит в двоичную
print(oct(100))  # Переводит в восьмеричную
print(hex(100))  # Переводит в шестнадцетиричную

print(int("1100100", 36))  # Переводит из какой-то (от 2 до 36) в десятичную'''

for N in range(1, 100):
    t = bin(N)[2:]
    if N % 3 == 0:
        t = t + t[-3:]
    else:
        t = t + bin((N % 3) * 3)[2:]
    R = int(t, 2)
    if R > 151:
        print(R)

# 163
