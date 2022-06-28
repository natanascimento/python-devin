a1 = 1 
a2 = 1
count = 2

print(a1)
print(a2)

while count < 15:
    a3 = a1 + a2
    print(a3)
    a1 = a2
    a2 = a3
    count += 1