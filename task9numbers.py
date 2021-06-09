a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
arr = [a, b, c, d, e]
print(max(arr))
print(min(arr))
for i in arr:
    if (i == max(arr)):
        continue
    elif (i == min(arr)):
        continue
    print(i)