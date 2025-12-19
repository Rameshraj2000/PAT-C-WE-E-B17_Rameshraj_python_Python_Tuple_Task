# numbers = [10, 501, 22, 37, 100, 999, 87, 351]
# print("Task 1: Even and Odd Numbers")
# even_numbers = []
# odd_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
#     else:
#         odd_numbers.append(num)
# print(even_numbers)
# print(odd_numbers)

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_count = 0
prime_num = []
for number in numbers:
    if is_prime(number):
        prime_count += 1
        prime_num.append(number)

print(f"Prime numbers: {prime_count}")
print(f"Prime numbers: {prime_num}")