even_num = input().split()

for i in even_num:
    if int(i) % 2 == 0:
        print(i, end=" ")