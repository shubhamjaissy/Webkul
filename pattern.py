

print('Enter the value of n  ')
n = int(input())

for i in range(1, n+1):
    print("*", end="")
for j in range(n-2):
    print(" ", end="")
for k in range(1, n+1):
    print("*", end="")
print()

for r in range(n-1):

    for i in range(1, n + 1):
        if i == n:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(n - 2):
        if r == n-2:
            print('*', end="")
        else:
            print(" ", end="")
    for k in reversed(range(n+1)):
        if k == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()


for k in range(1, n):
    for i in range(n):
        print(" ", end="")
    for j in range(3, n, 2):
        print(" ", end="")

    print("*")
