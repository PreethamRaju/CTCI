# 1.

# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use data structures.


# stringCheck = input("Enter a string to check for duplicates: ").lower()
# length = len(stringCheck)
# print(length)
#
#
# def is_duplicate(string):
#     for i in range(0, int(length)):
#         for j in range(i+1, length):
#             if string[i] == string[j]:
#                 dup = string[i]
#                 return dup
#
#
# duplicate = is_duplicate(stringCheck)
#
# if duplicate:
#     print("There is a duplicate character = {}".format(duplicate))
# else:
#     print("There is no duplicate character")


# ===============================================================================================

# 2.

# Given two strings. write a method to decide if one is a permutation of the other.


# stringOne = input(" Enter the first string: ").lower()
# stringTwo = input("Enter the second string: ").lower()
#
#
# def is_permutation(strone, strtwo):
#     lengthone = len(strone)
#     lengthtwo = len(strtwo)
#
#     if lengthone != lengthtwo:
#         return 0
#     else:
#         for charone in strone:
#             charcheck = 0
#             for chartwo in strtwo:
#                 if charone == chartwo:
#                     charcheck = 1
#                     break
#
#             if charcheck == 0:
#                 return 0
#         return 1
#
#
# permutation = is_permutation(stringOne, stringTwo)
#
# if permutation == 1:
#     print("The two strings are permutations")
# else:
#     print("The two strings are NOT permutations")


# ==========================================================================

#3.

# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of a string.
#
# EXAMPLE:
# Input:  "Mr John Smith    ", 13
# Output: "Mr%20John%20Smith"


# string = input("Enter a string: ")
#
#
# def string_insert(strcpy):
#     length = len(strcpy)
#     returnstring = ''
#
#     for i in range(0, length):
#         if strcpy[i] == ' ':
#             returnstring = returnstring + '%20'
#         else:
#             returnstring = returnstring + strcpy[i]
#         if len(returnstring) == length:
#                 return returnstring
#     return returnstring
#
#
# result = string_insert(string)
#
# print(result)

# ===============================================================================

# 4.

# Given a string, write a function to check if it's a permutation of a palindrome.
# EXAMPLE:
#   Input: Tact Coa
#   Output: True (permutations: "taco cat", "atco cta", etc.)


string = input("Enter a stirng: ").lower()

def is_Permutation(strcpy):
    length = len(strcpy)
    array = []
    for j in range(0, length):
        array[j] = 0
        for i in range (0, length):
            if strcpy[j] == strcpy[i]:
                array[j]
        array[j] = count



permutation = is_Permutation(string)


if permutation:
    print("True")
else:
    print("False")