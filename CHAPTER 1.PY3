1.1 – Sum of three numbers

a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

1.2 – Hi John

name = input()
print('Hi', name)

1.3 – Square

a = int(input())
print(a ** 2)

1.4 – Area of right-angled triangle

a = int(input())
b = int(input())
print(a * b / 2)

1.5 – Hello, Harry!

print('Hello, ' + input() + '!')

1.6 – Apple sharing

n = int(input())
k = int(input())
print(k // n)
print(k % n)

1.7 – Previous and next

n = int(input())
print(‘The next number for the number ‘ + str(n) + ‘ is ‘ + str(n + 1) + ‘.’)
print(‘The previous number for the number ‘ + str(n) + ‘ is ‘ + str(n – 1) + ‘.’)

1.8 – Two timestamps

hours_1 = int(input())
minutes_1 = int(input())
seconds_1 = int(input())
hours_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())
print(hours_2 * 3600 + minutes_2 * 60 + seconds_2
- hours_1 * 3600 - minutes_1 * 60 - seconds_1

1.9 – School desks

a = int(input())
b = int(input())
c = int(input())
print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)
