# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# # 1. Print out a list of the even integers:
print("Question 1")
def even_numbers(list):
    even_list = []
    for even_integer in numbers:
        if even_integer % 2 == 0:
            even_list.append(even_integer)
    return even_list
print(even_numbers(numbers))
            

# # 2. Print the difference between the largest and smallest value:
print("Question 2")
largest_number = max(numbers)
smallest_number = min(numbers)
difference_value = largest_number - smallest_number
print(difference_value)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
print("Question 3")
def find_two(list):
    for i in range(len(list) - 1):
        if list[i] == list[i + 1] and list[i] == 2:
            return True

# solution 2. works on any identical numbers
# def find_same_number(numbers):
#     for i in range(len(numbers) - 1):
#         if numbers[i] == numbers[i + 1]:
#             return True

print(find_two(numbers))

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

# ignore 6 until 7
print("Question 4")
def ignore_six_until_seven(list):
    sum = 0
    ignore_number = False
    for i in range(len(list)):
        if list[i] == 6:
            ignore_number = True
            continue
        elif list[i] == 7:
            ignore_number = False
            continue
        if not ignore_number:
            sum += list[i]
    return sum
print(ignore_six_until_seven(numbers))

# numbers starting with a 6, then how about if there's a 61 in the list?


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

print("Question 5")
def find_lucky_numbers(list):
    sum_of_number = 0
    unlucky_number = False
    for i in range(len(list)):
        if list[i] == 13:
            unlucky_number = True
        elif list[i] != 13:
            if list[i - 1] == 13:
                unlucky_number = True
            else:
                unlucky_number = False
                sum_of_number += list[i]
    return sum_of_number
print(find_lucky_numbers(numbers))