


def print_square(n):
    """
    Print a square of asterisks with side length n.

    For example, if n is 3, the output should be:
    ***
    ***
    ***
    """
   
    for _ in range(n):
        print("*" * n)

# The loop runs n times. For each iteration, the interpter prints a string of n asterisks. 


def is_odd(n):
    """
    Return True if n is odd, False otherwise.
    """
    
    if n % 2 != 0:
     return True
    else:
     return False

# Expression n % 2 checks for remainder after n is divided by 2.
# If the remainder is not equal to 0, the number is indeed odd. 
# If the remainder is equal to 0, the number is even. 



def median_of_three(a, b, c):
    """
    Return the median of three numbers a, b, and c.
    """
    nums = [a, b, c]
    nums.sort()
    return nums[1]

# Creates a list named "nums" containing three values. 
# Utilizes .sort() function to sort list from least to greatest
# Uses an index to return the middle value (median) in list. 


def is_palindrome(s):
    """
    Return True if the string s is a palindrome, False otherwise.

    A palindrome reads the same forwards and backwards. You can
    implement it as a simple check to see if s is equal to its
    reversal.
    """
    return s == s[::-1]

# Returns "True" if s is equal to itself written backwards, or "False" otherwise.
# s[::-1] uses string slicing with step -1 to create a reversed copy of string. 


def factorial(n):
    """
    Return the factorial of n.

    The factorial of a non-negative integer n is the product of all
    positive integers less than or equal to n. Please implement this
    function with a for loop.
    """
    product=1
    for i in range (1, n+1):
        product *= i
    return product

# For loop iterates through a range (1, and up to, but not including n+1).
# Each number, represented by variable "i"in the range, is multiplied by previous product.
# Result of previous step becomes new value of "product" variable, and previous step repeats through entire range. 


def count_of_latin_vowels(s):
    """
    Return the number of vowels in the string s.

    The vowels are 'a', 'e', 'i', 'o', and 'u'. You can implement this
    function using a for loop to iterate through the string.
    """
    vowel_count = 0
    for c in s:
        if c.lower() in "aeiou":
            vowel_count += 1
    return vowel_count

# Creates a variable called "vowel_count" and sets it equal to 0
# Lowercases each character in word s and checks if each character is in string "aeiou"
# If so, the "vowel_count" variable is incremented by one.
# Number of vowels found is returned. 


def at_beginning_or_end(part, whole):
    """
    Return True if the part is a prefix or a suffix of whole.
    """
    if whole.startswith(part) or whole.endswith(part):
        return True
    else:
        return False

# Utilizes .startswith() and .endswith() functions to determine if argument "whole" starts with or ends with argument "part".


def longest_string(strings):
    """
    Return the longest string from a list of strings.

    If there are multiple strings with the same maximum length, return
    the first one encountered.
    """
    longest_so_far = ""
    for s in strings:
        if len(s) > len(longest_so_far):
            longest_so_far = s
    return longest_so_far
 
response = input("Enter strings separated by commas: ")
strings = response.split(",")

print(longest_string(strings))

# response is created to allow user to input a comma-separated list.
# The list is then separated into individual strings and set equal to variable strings. 
# for loop compares each string with the current longest_so_far value
# If the string compared is longer than the current longest_so_far value, it becomes the new value for longest_so_far
# This process repeats until every string is compared. 
# Function returns longest string in initial list.


    
def collatz(n):
    """
    Return the Collatz sequence starting from n.

    The Collatz sequence is defined as follows:
    - If n is even, the next term is n / 2.
    - If n is odd, the next term is 3n + 1.
    - The sequence ends when it reaches 1.
    """
    numbers = [n]
    while n > 1:
        if n % 2 != 0:
            n = 3 * n + 1
        else:
            n = n // 2
        numbers.append(n)
    return numbers

# Creates a variable named "numbers" containing initial value n.
# Loop continues until n becomes 1. 
# If the remainder after n is divided by 2 is not equal to 0 (n is odd): perform 3 times n plus 1, and set n equal to result of this operation.
# if the remainder after n is divided by 2 is equal to 0 (n is even): perform floor division by 2, and set n equal to result of this operation.
# Add new n values to end of list.
# Return completed list.

def test_print_square():
    import io
    import contextlib
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        print_square(2)
    assert f.getvalue() == "**\n**\n"
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        print_square(5)
    assert f.getvalue() == "*****\n*****\n*****\n*****\n*****\n"
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        print_square(1)
    assert f.getvalue() == "*\n"
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        print_square(0)
    assert f.getvalue() == ""


def test_is_odd():
    assert is_odd(3) is True
    assert is_odd(8) is False
    assert is_odd(-3) is True
    assert is_odd(-8) is False


def test_median_of_three():
    assert median_of_three(1, 2, 3) == 2
    assert median_of_three(10, 30, 20) == 20
    assert median_of_three(25, 15, 35) == 25
    assert median_of_three(900, 9999, -1050) == 900
    assert median_of_three(193, 191, 192.5) == 192.5
    assert median_of_three(99999, 0, -1000) == 0


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(6) == 720
    assert factorial(20) == 2432902008176640000


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("madam") is True
    assert is_palindrome("python") is False


def test_count_of_latin_vowels():
    assert count_of_latin_vowels("hello world") == 3
    assert count_of_latin_vowels("aeiou") == 5
    assert count_of_latin_vowels("xyz") == 0
    assert count_of_latin_vowels("Python programming") == 4
    assert count_of_latin_vowels("Aeiou") == 5


def test_at_beginning_or_end():
    assert at_beginning_or_end("pre", "prefix") is True
    assert at_beginning_or_end("fix", "suffix") is True
    assert at_beginning_or_end("middle", "start middle end") is False
    assert at_beginning_or_end("dog", "doghouse") is True
    assert at_beginning_or_end("doghouse", "dog") is False
    assert at_beginning_or_end("cat", "dog") is False
    assert at_beginning_or_end("", "anything") is True


def test_longest_string():
    assert longest_string(["apple", "banana", "cherry"]) == "banana"
    assert longest_string(["cat", "dog", "elephant"]) == "elephant"
    assert longest_string(["short", "longer", "longest"]) == "longest"
    assert longest_string(["a", "ab", "abc"]) == "abc"
    assert longest_string(["one", "two", "three", "four"]) == "three"


def test_collatz():
    assert collatz(1) == [1]
    assert collatz(2) == [2, 1]
    assert collatz(3) == [3, 10, 5, 16, 8, 4, 2, 1]
    assert collatz(4) == [4, 2, 1]
    assert collatz(5) == [5, 16, 8, 4, 2, 1]
    assert collatz(15) == [
        15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1
    ]


test_print_square()
test_is_odd()
test_median_of_three()
test_factorial()
test_is_palindrome()
test_count_of_latin_vowels()
test_at_beginning_or_end()
test_longest_string()
test_collatz()
print("All tests passed!")
