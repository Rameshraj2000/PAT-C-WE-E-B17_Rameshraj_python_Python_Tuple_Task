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
# Program 2 prime numbers
# numbers = [10, 501, 22, 37, 100, 999, 87, 351]
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
#
# prime_count = 0
# prime_num = []
# for number in numbers:
#     if is_prime(number):
#         prime_count += 1
#         prime_num.append(number)
#
# print(f"Prime numbers: {prime_count}")
# print(f"Prime numbers: {prime_num}")
#
# program 3 happy number
# numbers = [10, 501, 22, 37, 100, 999, 87, 351]
#
# def happy_number(n):
#     """
#     Check if a number is a happy number
#     A happy number eventually reaches 1 when replaced by sum of squares of digits
#     An unhappy number enters a cycle that doesn't include 1
#     """
#     # Set to store seen numbers (to detect cycles)
#     seen = set()
#
#     while n != 1 and n not in seen:
#         seen.add(n)
#         # Calculate sum of squares of digits
#         digit_sum = 0
#         while n > 0:
#             digit = n % 10  # Get last digit
#             digit_sum += digit ** 2  # Add square of digit
#             n = n // 10  # Remove last digit
#
#         n = digit_sum  # Update n for next iteration
#
#     return n == 1  # Happy if we reached 1
# # Count happy numbers
# happy_count = 0
# happy_numbers = []
#
# for num in numbers:
#     if happy_number(num):
#         happy_count += 1
#         happy_numbers.append(num)
#
# print(f"Total Happy Numbers: {happy_count}")
# print(f"Happy Numbers: {happy_numbers}")
#
# Program4 sum of first and last digit
# def sum_first_last_digit(number):
#
#     #This function calculates the sum of the first and last digit of a number.
#     # Convert number to string to easily access digits
#     num_str = str(number)
#
#     # Handle negative numbers by removing the minus sign
#     if num_str[0] == '-':
#         num_str = num_str[1:]  # Remove the negative sign
#
#     # Get first and last digits
#     first_digit = int(num_str[0])
#     last_digit = int(num_str[-1])
#
#     # Calculate and return sum
#     return first_digit + last_digit
# # Test with different numbers
# test_numbers = [12345, 74, 100, 987654, -123, -4567]
# print("Number\t\tFirst Digit\tLast Digit\tSum")
# for num in test_numbers:
#     result = sum_first_last_digit(num)
#     num_str = str(num)
#     if num_str[0] == '-':
#         first_digit = num_str[1]
#         last_digit = num_str[-1]
#     else:
#         first_digit = num_str[0]
#         last_digit = num_str[-1]
#     print(f"{num:8}\t{first_digit:12}\t{last_digit:10}\t{result}")
#
# Program 5 how to make Rs 10
# def count_coin_combinations(target_amount=10):
#     """
#     Find all combinations of coins (Rs. 1, Rs. 2, Rs. 5, Rs. 10) to make target amount.
#     """
#     coins = [10, 5, 2, 1]
#     combinations = []
#
#     # Using nested loops for all coin types
#     for count_10 in range(target_amount // 10 + 1):  # Maximum Rs. 10 coins
#         for count_5 in range(target_amount // 5 + 1):  # Maximum Rs. 5 coins
#             for count_2 in range(target_amount // 2 + 1):  # Maximum Rs. 2 coins
#                 for count_1 in range(target_amount + 1):  # Maximum Rs. 1 coins
#                     total = (count_10 * 10) + (count_5 * 5) + (count_2 * 2) + (count_1 * 1)
#
#                     if total == target_amount:
#                         combinations.append({
#                             'Rs. 10': count_10,
#                             'Rs. 5': count_5,
#                             'Rs. 2': count_2,
#                             'Rs. 1': count_1
#                         })
#
#     return combinations
#
#
# # Find all combinations for Rs. 10
# combinations = count_coin_combinations(10)
#
# # Display results
# print(f"\nTotal ways to make Rs. 10: {len(combinations)}\n")
# print("No.  | Rs. 10 | Rs. 5 | Rs. 2 | Rs. 1 |")
# print("-" * 40)
#
# for i, combo in enumerate(combinations, 1):
#     print(f"{i:3} | {combo['Rs. 10']:6} | {combo['Rs. 5']:5} | {combo['Rs. 2']:5} | {combo['Rs. 1']:5} |")
#
# Program 6 fund duplicate in three list
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [2, 4, 6, 8, 10, 12, 14, 16]
# list3 = [3, 6, 9, 12, 15, 10]
#
# print("Sample Lists:")
# print(f"List 1: {list1}")
# print(f"List 2: {list2}")
# print(f"List 3: {list3}")
#
# # Convert lists to sets for easy intersection
# set1 = set(list1)
# set2 = set(list2)
# set3 = set(list3)
#
# # Find common elements in all three lists
# common_in_all = set1.intersection(set2, set3)
# print(f"Common elements in all three lists: {sorted(common_in_all)}")
#
# Program 7 non repeating elements
# def find_first_non_repeating(numbers):
#     """
#     Find the first element that appears only once in the list.
#     Returns the element or None if all elements repeat.
#     """
#     # Count frequency of each element
#     frequency = {}
#
#     # First pass: count occurrences
#     for num in numbers:
#         if num in frequency:
#             frequency[num] += 1
#         else:
#             frequency[num] = 1
#     # Second pass: find first element with count 1
#     for num in numbers:
#         if frequency[num] == 1:
#             return num
#     return None  # If no non-repeating element found
# # Test cases
# test_lists = [
#     [4, 5, 1, 2, 0, 4],
#     [1, 2, 3, 4, 5],
#     [1, 1, 2, 3, 3],
#     [7, 7, 8, 8, 9, 1],
#     [10, 20, 30, 40]
# ]
# print("List\t\t\t\t\tFirst Non-Repeating")
# for lst in test_lists:
#     result = find_first_non_repeating(lst)
#     print(f"{lst}\t\t\t\t{result if result is not None else 'None (all repeat)'}")
#
# Program 8 minimum element sorted list
# def find_minimum_simple(numbers):
#     """Simple method to find minimum element."""
#     if not numbers:
#         return None
#
#     minimum = numbers[0]
#     for num in numbers:
#         if num < minimum:
#             minimum = num
#     return minimum
# # Test simple method
# test_list = [45, 23, 67, 12, 89, 34, 11]
# print(f"List: {test_list}")
# print(f"Minimum (using min()): {min(test_list)}")
# print(f"Minimum (using our function): {find_minimum_simple(test_list)}")
#
# program 9 find the triplet
# def find_triplet_with_sum(numbers, target_sum):
#     """
#     Find three numbers in list that add up to target sum.
#     Returns the triplet or None if not found.
#     """
#     n = len(numbers)
#     triplets = []
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 if numbers[i] + numbers[j] + numbers[k] == target_sum:
#                     triplets.append((numbers[i], numbers[j], numbers[k]))
#     if triplets:
#         print(f"Triplet(s) found: {triplets}")
#         return triplets
#     else:
#         print(f"No triplet found with sum {target_sum}")
#         return None
# # Test with given list
# numbers = [10, 20, 30, 9]
# target = 59
# print(f"List: {numbers}")
# print(f"Target sum: {target}")
# result = find_triplet_with_sum(numbers, target)
#
# Program 10 sub list with sum 0
# def has_zero_sum_sublist(numbers):
#     """
#     Check if there exists a contiguous sublist with sum zero.
#     Uses prefix sum technique.
#     """
#     n = len(numbers)
#
#     for start in range(n):
#         current_sum = 0
#         for end in range(start, n):
#             current_sum += numbers[end]
#             if current_sum == 0:
#                 print(f"Zero sum sublist found: {numbers[start:end + 1]}")
#                 return True, numbers[start:end + 1]
#
#     print("No zero sum sublist found")
#     return False, None
# # Test with given list
# numbers_list = [4, 2, -3, 1, 6]
# print(f"List: {numbers_list}")
# found, sublist = has_zero_sum_sublist(numbers_list)