#  Евгения составляет 4-значные числа в 8-ичной системе счисления. Числа
# должны начинаться с чётной цифры, и цифры в них располагаются в
# невозрастающем порядке. Сколько различных чисел может составить
# Евгения?


from itertools import product
k = 0
for _ in product('01234567', repeat=4):
    s = ''.join(_)
    if s[0] in '246' and s[0] >= s[1] >= s[2] >= s[3]:
        k += 1
print(k)
