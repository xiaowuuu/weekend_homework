# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# # 1. Print out a list of the even integers:
# for even_integer in numbers:
#     if even_integer % 2 == 0:

#         print(even_integer)

# # 2. Print the difference between the largest and smallest value:
# largest_number = max(numbers)
# smallest_number = min(numbers)
# difference_value = largest_number - smallest_number
# print(difference_value)



# 3. Print True if the list contains a 2 next to a 2 somewhere.

# def find_two(list):
#     for i in range(len(list) - 1):
#         if list[i] == list[i + 1] and list[i] == 2:
#             return True

# solution 2. works on any identical numbers
# def find_same_number(numbers):
#     for i in range(len(numbers) - 1):
#         if numbers[i] == numbers[i + 1]:
#             return True

# print(find_two(numbers))




# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

# ignore 6 until 7
# def ignore_six_until_seven(list):
#     sum = 0
#     ignore_number = False
#     for i in range(len(list)):
#         if list[i] == 6:
#             ignore_number = True
#             continue
#         elif list[i] == 7:
#             ignore_number = False
#             continue
#         if not ignore_number:
#             sum += list[i]
#     return sum
# print(ignore_six_until_seven(numbers))

# numbers starting with a 6, then how about if there's a 61 in the list?


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 


# def find_lucky_numbers(number):
#     lucky_number = []
#     i = 0
#     for i in range(len(number)):
#         if number[i] == 13:
            
#         else:
#             lucky_number.append(number[i])
#     return lucky_number
