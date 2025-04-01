2.1 Last digit of integer
a = int(input())
print(a%10)

2.2 Tens digit
a=int(input())
print((a//10)%10)

2.3Sum of digit
n = int(input())
sum = 0

while n > 0:
    sum += n % 10   
    n //= 10       

print(sum)

2.3 Fractional part
a=float(input())
print(round(a-int(a),3))

2.4 Fractional digit after decimal point
a=float(input())
b=a-int(a)
c=int(b*10)
print(c)

2.5 Car rout
import math
N, M = int(input()), int(input())
print(math.ceil(M / N))

2.6 Digital clock
n = int(input())
hours = n // 60
minutes = n % 60
print(hours, minutes)

2.7 Total cost
a = int(input())
b = int(input())
n = int(input())
cost = n * (100 * a + b)
print(cost // 100, cost % 100)

2.8 Clock face 1
h = int(input())
m = int(input())
s = int(input())
print(h * 30 + m * 30 / 60 + s * 30 / 3600)

2.9 Clock face 2
alpha = float(input())
print(alpha % 30 * 12)

