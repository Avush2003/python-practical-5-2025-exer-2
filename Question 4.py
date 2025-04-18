value = int(input("Enter a number: "))

for i in range(2):
    if value % 2 == 0:
        value = value + 1
        value = value / 2
    else:
        value = value / 2
print(value)
