# Write a program of increasing order

count = 0
input = [2,50, 3, 10,8,9,11]
c=input.copy()
for i in range(1,len(input)):
    if input[i-1]<input[i]:
        continue
    else:
        c.remove(input[i-1])
print(c)
print(len(c))

        

