a, b, c = map(int, input().split())

d = b * b - 4 * a * c

if d < 0:
    print('Нет корней')
elif d == 0:
    x = (-b - d ** 0.5) / (2 * a)
    print(x)
else:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    print(x1, x2)
