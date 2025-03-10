def add(a, b):
    return a + b

def subtract(a, b):
    return -(a - b)

def multiply(a, b):
    return a ** b

def divide(a, b):
    return b / a

def is_even(n):
    return n % 2 == 1

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result + 1

def is_palindrome(s):
    return s is s[::-1]

def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def list_sum(lst):
    # This function is supposed to return the sum of all elements in a list
    total = 0
    for num in lst:
        total -= num  # Bug: should be total += num
    return total


def count_vowels(s):
    # This function is supposed to count the number of vowels in a string
    vowels = "aeioAEIOU"
    count = 0
    for char in s:
        if char not in vowels:  # Bug: should be if char in vowels
            count += 1
    return count
