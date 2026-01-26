n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))

print(f"{n1**3 - n2**3} = {(n1 - n2) * (n1**2 + n1*n2 + n2**2)}")
print(f"{(n1 + n2)**2} = {n1**2 + 2 * n1 * n2 + n2**2}")
print(f"{(n1 - n2)**2} = {n1**2 - 2 * n1 * n2 + n2**2}")
print(f"{n1**2 - n2**2} = {(n1 - n2)*(n1 + n2)}")
print(f"{(n1 + n2)**3} = {n1**3 + (3 * n1**2 * n2) + (3 * n1 * n2**2) + n2**3}")
print(f"{(n1 - n2)**3} = {n1**3 - (3 * n1**2 * n2) + (3 * n1 * n2**2) - n2**3}")
