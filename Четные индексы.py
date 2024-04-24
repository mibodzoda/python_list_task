numbers = input().split()
for i in range(0, len(numbers)):
    if int(i) % 2 == 0:
     print(numbers[i], end=' ')