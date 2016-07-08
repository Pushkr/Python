#Problem#1:
#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
#string_times('Hi', 2) → 'HiHi'
#string_times('Hi', 3) → 'HiHiHi'
#string_times('Hi', 1) → 'Hi'

#Solution
def string_times(str, n):
    final_str = ''
    for i in range(0, n):
        final_str = final_str + str

    return final_str

#Problem#2:
#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is
# there if the string is less than length 3. Return n copies of the front;
#front_times('Chocolate', 2) → 'ChoCho'
#front_times('Chocolate', 3) → 'ChoChoCho'
#front_times('Abc', 3) → 'AbcAbcAbc'

#Solution
def front_times(str, n):
    final_str = ''
    chop = str[0:3]
    for i in range(0, n):
        final_str = final_str + chop

    return final_str

#Problem#3
#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
#string_bits('Hello') → 'Hlo'
#string_bits('Hi') → 'H'
#string_bits('Heeololeo') → 'Hello'

#Solution:
def string_bits(str):
    str_len = len(str)
    final_str = ''
    for i in range(0, str_len):
        if i % 2 == 0:
            final_str = final_str + str[i]

    return final_str


#Problem#4:
# Given a non-empty string like "Code" return a string like "CCoCodCode".
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'
#Solution:
def string_splosion(str):
    result = ''
    for i in range(0, len(str) + 1):
        chop = str[0:i]
        result = result + chop

    return result


# Problem#5
# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as
# the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

#Solution:

def last2(str):
    result = ''
    l2 = str[len(str) - 2:len(str)]
    chop = str[0:len(str) - 2]
    count = 0
    for i in range(0, len(chop)):
        sub = str[i:i + 2]
        if sub == l2:
            count += 1

    return count

## Problem#6
# Given an array of ints, return the number of 9's in the array.
#
# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

#Solution:
def array_count9(nums):
    count = 0
    for i in range(0, len(nums)):
        if nums[i] == 9:
            count += 1

    return count


# Problem#7
# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length
# may be less than 4.
# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

#Solution:
def array_front9(nums):
    if len(nums) < 4:
        arr_len = len(nums)
    else:
        arr_len = 4

    for i in range(0, arr_len):
        if nums[i] == 9:
            return True
            break

    return False


# Problem#8
# Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.
# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

#Solution:
def array123(nums):
    if len(nums) < 3:
        return False

    f= 0

    for i in range(0,len(nums)):
        if i <= len(nums) - 3 and nums[i] ==1 and nums[i+1]==2 and nums[i+2]==3:
           f = 1

    if f == 1:
        return True
    else:
        return False