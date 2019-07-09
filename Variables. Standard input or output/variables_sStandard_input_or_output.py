minutes = int(input())
h = int(input())
m = int(input())
r = minutes + h*60 + m
print(r//60)
print(r%60)