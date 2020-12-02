import math

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

bunja = a1 * b2 + a2 * b1
bunmo = b1 * b2

my = math.gcd(bunja, bunmo)
bunja //= my
bunmo //= my

print(bunja, bunmo)