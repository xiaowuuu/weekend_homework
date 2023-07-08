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
# def find_same_number(numbers):
#     for i in range(len(numbers) - 1):
#         if numbers[i] == numbers[i + 1]:
#             return True
# def find_two(numbers):
#     for i in range(len(numbers) - 1):
#         if numbers[i] == numbers[i + 1] and numbers[i] == 2:
#             return True

# print(find_two(numbers))




# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
def sum_without_six_untill_seven(list):
    sum = 0
    ignore_number = False

    for number in list:
        if str(number).startswith("6"):
            ignore_number = True
            continue
        
        elif number == 7:
            ignore_number = True
        else:
            sum += number

print(sum_without_six_untill_seven(numbers))

            



# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 




