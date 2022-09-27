a, b, c = map(int, input().split())

d = b * b - 4 * a * c

x1 = (-b - d ** 0.5) / (2 * a)
x2 = (-b + d ** 0.5) / (2 * a)

print(x1, x2)
