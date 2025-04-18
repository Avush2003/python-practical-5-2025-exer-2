List = []

for i in range(4):
    num = int(input("Enter a number: "))
    List.append(num)

x = min(List)
y = max(List)
print(f"Least: {x}")
print(f"Most: {y}")

ave = (int(x) + int(y) )/(2)
print(f"Average: {ave}")