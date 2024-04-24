num = input().split()
cnt = 0
for i in num:
    if int(i) > 0:
        cnt+=1
print(cnt)