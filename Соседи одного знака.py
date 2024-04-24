numbers = input().split()


for i in range( len(numbers)-1):
    if int(numbers[i]) > 0 and int(numbers[i + 1]) > 0 or int(numbers[i]) < 0 and int(numbers[i + 1]) < 0:
        print(numbers[i], numbers[i+1])
        break