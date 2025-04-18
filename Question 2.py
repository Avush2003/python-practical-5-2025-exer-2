List = [2, 4, 2, 6, 26, 2, 3, 68, 9, 10, 71, 68]

new_List = list(set(List))
new_List.sort()

print(new_List)

List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

even_numbers = []
odd_numbers = []

for x in List1:
    if x % 2 == 0:
        even_numbers.append(x)
    else:
        odd_numbers.append(x)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)