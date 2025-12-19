numbers = [10, 501, 22, 37, 100, 999, 87, 351]
print("Task 1: Even and Odd Numbers")
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print(even_numbers)
print(odd_numbers)