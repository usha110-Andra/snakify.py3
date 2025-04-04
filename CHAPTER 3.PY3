3.1 Minimum of two numbers
a=int(input())
b=int(input())
if a>b:
    print(b)
else:
    print(a)

3.2 Sign function
a=int(input())
if a>0:
    print("1")
elif a<0:
    print("-1")
else:
    print("0")
3.3 Minimum of three numbers
a=int(input())
b=int(input())
c=int(input())
if a<b and a<c:
    print(a)
elif b<c:
    print(b)
else:
    print(c)
3.4 Equal numbers
a = int(input())
b = float(input())
c=int(input())
if a==b and b==c and a==c:
    print("3")
elif a==b or a==c or b==c:
    print("2")
else:
    print("0")

3.5 Rook move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')

3.6 Chess board-same colour
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print("YES")
else:
    print("NO")

3.7 King move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 - x2 < 2 and y1 - y2 < 2 and x1 - x2 > -2 and y1 - y2 > -2 :
    print('YES')
else:
    print('NO')

3.8 Bishop moves
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 - x2 == y1 - y2 or x1 - x2 == y2 - y1:
    print('YES')
else:
    print('NO')

3.9 Queen move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2 or x1 - x2 == y1 - y2 or x1 - x2 == y2 - y1:
    print('YES')
else:
    print('NO')

3.10 Knight move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == 2 and abs(y1 - y2) == 1 or abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
    print('YES')
else:
    print('NO')

3.11 Chocolate bar
n = int(input())
m = int(input())
k = int(input())
if k <= n * m and (k % n == 0 or k % m == 0):
    print('YES')
else:
    print('NO')

3.12 Leap year
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('LEAP')
else:
    print('COMMON')
