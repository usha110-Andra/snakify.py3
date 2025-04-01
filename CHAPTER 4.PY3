4.1 series-1
A = int(input())
B = int(input())
for i in range(A, B + 1):
    print(i)

4.2 Series-2
A = int(input())
B = int(input())
if A < B:
    for i in range(A, B + 1):
        print(i, end=' ')
else:
    for i in range(A, B - 1, -1):
        print(i, end=' ')

4.3 Sum of ten numbers
S = 0
for i in range(0, 10):
    n = int(input())
    S += n
print(S)

4.4 Sum of N numbers
S = 0
for i in range(0, 10):
    n = int(input())
    S += n
print(S)

4.5 Sum of cubes
res = 0
for i in range(1, int(input()) + 1):
    res += i ** 3
print(res)

4.6 Factorial
n = int(input())
f = 1
for i in range(1, n +1):
    f *= i
print(f)

4.7 The number of zeroes
num_zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        num_zeroes += 1
print(num_zeroes)

4.8 Adding factorial
n = int(input())
partial_factorial = 1
partial_sum = 0
for i in range(1, n + 1):
    partial_factorial *= i
    partial_sum += partial_factorial
print(partial_sum)

4.9 Ladder
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

4.10 Losr card
n = int(input())
sum_cards = 0
for i in range(1, n + 1):
    sum_cards += i
# One can prove the following:
# sum_cards == n * (n + 1) // 2
# However, we'll calculate that using the loop.
for i in range(n - 1):
    sum_cards -= int(input())
print(sum_cards)