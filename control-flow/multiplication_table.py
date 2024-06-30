number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 10 + 1):
    result = number * i
    print(f"{number} * {i} = {result}")
