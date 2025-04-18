a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a % 2 == 0 and b % 2 !=0:
    print(f"The first number entered ({a}) is even and the second number entered ({b}) is odd")

elif a % 2 !=0 and b % 2 ==0:
    print(f"The first number entered ({a}) is odd and the second number entered ({b}) is even")

if a % 2 == 0 and b % 2 == 0:
    print(f"Both numbers entered ({a}) and ({b}) are even")
elif a % 2 != 0 and b % 2 != 0:
    print(f"Both numbers entered ({a}) and ({b}) are odd")
    exit()

#Proof
#Example 1: if a = 2 and b = 4 > both even > same type.
#Example 2: if a = 3 and b = 5 > both odd > same type.
#Example 3: if a = 2 and b = 3 > first number even and second number odd > different type
#Example 3: if a = 3 and b = 2 > first number odd and second number even > different type