count = 0
number = 0
input = [2,50, 3, 10, 7, 40, 80,70,90,1]

c = input.copy()
for i in range(1, len(input)):
    if input[i-1] < input[i]:
        continue
    else:
        c.remove(input[i-1])
print(len(c))