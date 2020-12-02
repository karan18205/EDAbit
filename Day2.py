print('Starting with Hard Problems')
print('Take 10 everyday')

## Combinations

# Create a function that takes a variable number of arguments, each argument representing the number of items in a group,
# and returns the number of permutations (combinations) of items that you could get by taking one item from each group.
# Examples
# combinations(2, 3) ➞ 6
# combinations(3, 7, 4) ➞ 84
# combinations(2, 3, 4, 5) ➞ 120

def combinations(*items):
    ans = 1
    numbers = len(items)
    for i in range(numbers):
        if items[i]==0:
            continue
        ans = ans*items[i]
    print(ans)

# combinations(2,3,0)

########################################################################################################################

## Basic Arithmetic Operations on a String Number

# Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division
# on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
#
# Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have
# only two numbers between 1 valid operator. The return value should be a number.
#
# eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

def arithmetic_operation(n):
    arr = n.split()
    if('+' in n):
        print(float(arr[0])+float(arr[2]))
    elif('-' in n):
        print(float(arr[0])-float(arr[2]))
    elif ('*' in n):
        print(float(arr[0]) * float(arr[2]))
    elif ('/' in n):
        if float(arr[2])==0:
            print(-1)
        else:
            print(float(arr[0]) / float(arr[2]))


# arithmetic_operation("12 // 0")

########################################################################################################################

## RegEx VII-A: Negative Lookbehind

# Write a regular expression that will help us count how many bad cookies are produced every day. You must use RegEx
# negative lookbehind.

import re
lst = ['bad cookie', 'good cookie', 'bad cookie', 'good cookie', 'good cookie']
pattern = "yourregularexpressionhere"

# z=re.findall(r'[\w\.-]+', lst)

# print(z)

########################################################################################################################

## The Karaca's Encryption Algorithm

# Make a function that encrypts a given input with these steps:
#
# Input: "apple"
#
# Step 1: Reverse the input: "elppa"
#
# Step 2: Replace all vowels using the following chart:
#
# a => 0
# e => 1
# i => 2
# o => 2
# u => 3
#
# # "1lpp0"
# Step 3: Add "aca" to the end of the word: "1lpp0aca"
#
# Output: "1lpp0aca"

def encrypt(word):
    final = ''
    lst = list(word[::-1])
    for i in range(len(lst)):
        if lst[i]=='a':
            lst[i]='0'
        elif lst[i]=='e':
            lst[i] = '1'
        elif lst[i]=='i':
            lst[i] = '2'
        elif lst[i]=='o':
            lst[i] = '2'
        elif lst[i]=='u':
            lst[i] = '3'
    final = final.join(lst)
    print(final)

# encrypt('Karan')

########################################################################################################################

## Friday the 13th

# Given the month and year as numbers, return whether that month contains a Friday 13th.
# Examples
# has_friday_13(3, 2020) ➞ True
# has_friday_13(10, 2017) ➞ True
# has_friday_13(1, 1985) ➞ False

import datetime
def has_friday_13(month, year):
    if datetime.datetime.strptime('13 ' + ' ' + str(month) + ' ' + str(year), '%d %m %Y').weekday() == 4:
        print(True)
    else:
        print(False)

# has_friday_13(3, 2020)

########################################################################################################################

## Combined Consecutive Sequence

# Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence is
# a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.

def consecutive_combo(lst1, lst2):
    total = []
    for i in lst2:
        lst1.append(i)
    total = sorted(lst1, reverse=True)
    count = 0
    for i in range(len(total)-1):
        if total[i]-total[i+1]==1:
            count = count+1
    if count==len(total)-1:
        print('True')
    else:
        print('False')

# consecutive_combo([7, 4, 5, 1], [2, 3, 6])

########################################################################################################################

## Algorithms: Binary Search

# Create a function that finds a target number in a list of prime numbers. Implement a binary search algorithm in your
# function. The target number will be from 2 through 97. If the target is prime then return "yes" else return "no".

def is_prime(primes, num, left=0, right=None):
    if num in primes:
        return 'yes'
    else:
        return 'no'

########################################################################################################################

## The Snake — Area Filling

def snakefill(n):
    total_space = n*n
    # 1,2,4,8,16,32,64
    if n==1:
        return 0
    for i in range(n*n):
        if((n*n/2**i)<1):
            print(i-1)
            break

# snakefill(24)

########################################################################################################################

## Encode Morse

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

def encode_morse(message):
    lst = list(message)
    morse = []
    final = ''
    for char in lst:
        m = char_to_dots[char.upper()]
        morse.append(m+' ')
    final = final.join(morse)
    print(final[:-1])

encode_morse("EDABBIT CHALLENGE")

########################################################################################################################

## Pentagonal Number

# Write a function that takes a positive integer num and calculates how many dots exist in a pentagonal shape around the
# center dot on the Nth iteration.
#
# In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots. On the third,
# there are 16 dots, and on the fourth there are 31 dots.

def pentagonal(num):
    if n>1:
        return (5*n*n-5*n+2)/2
    else:
        return 1

pentagonal(num)

















## Combinations

# Create a function that takes a variable number of arguments, each argument representing the number of items in a group,
# and returns the number of permutations (combinations) of items that you could get by taking one item from each group.
# Examples
# combinations(2, 3) ➞ 6
# combinations(3, 7, 4) ➞ 84
# combinations(2, 3, 4, 5) ➞ 120

def combinations(*items):
    ans = 1
    numbers = len(items)
    for i in range(numbers):
        if items[i]==0:
            continue
        ans = ans*items[i]
    print(ans)

# combinations(2,3,0)

########################################################################################################################

## Basic Arithmetic Operations on a String Number

# Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division
# on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
#
# Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have
# only two numbers between 1 valid operator. The return value should be a number.
#
# eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

def arithmetic_operation(n):
    arr = n.split()
    if('+' in n):
        print(float(arr[0])+float(arr[2]))
    elif('-' in n):
        print(float(arr[0])-float(arr[2]))
    elif ('*' in n):
        print(float(arr[0]) * float(arr[2]))
    elif ('/' in n):
        if float(arr[2])==0:
            print(-1)
        else:
            print(float(arr[0]) / float(arr[2]))


# arithmetic_operation("12 // 0")

########################################################################################################################

## RegEx VII-A: Negative Lookbehind

# Write a regular expression that will help us count how many bad cookies are produced every day. You must use RegEx
# negative lookbehind.

import re
lst = ['bad cookie', 'good cookie', 'bad cookie', 'good cookie', 'good cookie']
pattern = "yourregularexpressionhere"

# z=re.findall(r'[\w\.-]+', lst)

# print(z)

########################################################################################################################

## The Karaca's Encryption Algorithm

# Make a function that encrypts a given input with these steps:
#
# Input: "apple"
#
# Step 1: Reverse the input: "elppa"
#
# Step 2: Replace all vowels using the following chart:
#
# a => 0
# e => 1
# i => 2
# o => 2
# u => 3
#
# # "1lpp0"
# Step 3: Add "aca" to the end of the word: "1lpp0aca"
#
# Output: "1lpp0aca"

def encrypt(word):
    final = ''
    lst = list(word[::-1])
    for i in range(len(lst)):
        if lst[i]=='a':
            lst[i]='0'
        elif lst[i]=='e':
            lst[i] = '1'
        elif lst[i]=='i':
            lst[i] = '2'
        elif lst[i]=='o':
            lst[i] = '2'
        elif lst[i]=='u':
            lst[i] = '3'
    final = final.join(lst)
    print(final)

# encrypt('Karan')

########################################################################################################################

## Friday the 13th

# Given the month and year as numbers, return whether that month contains a Friday 13th.
# Examples
# has_friday_13(3, 2020) ➞ True
# has_friday_13(10, 2017) ➞ True
# has_friday_13(1, 1985) ➞ False

import datetime
def has_friday_13(month, year):
    if datetime.datetime.strptime('13 ' + ' ' + str(month) + ' ' + str(year), '%d %m %Y').weekday() == 4:
        print(True)
    else:
        print(False)

# has_friday_13(3, 2020)

########################################################################################################################

## Combined Consecutive Sequence

# Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence is
# a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.

def consecutive_combo(lst1, lst2):
    total = []
    for i in lst2:
        lst1.append(i)
    total = sorted(lst1, reverse=True)
    count = 0
    for i in range(len(total)-1):
        if total[i]-total[i+1]==1:
            count = count+1
    if count==len(total)-1:
        print('True')
    else:
        print('False')

# consecutive_combo([7, 4, 5, 1], [2, 3, 6])

########################################################################################################################

## Algorithms: Binary Search

# Create a function that finds a target number in a list of prime numbers. Implement a binary search algorithm in your
# function. The target number will be from 2 through 97. If the target is prime then return "yes" else return "no".

def is_prime(primes, num, left=0, right=None):
    if num in primes:
        return 'yes'
    else:
        return 'no'

########################################################################################################################

## The Snake — Area Filling

def snakefill(n):
    total_space = n*n
    # 1,2,4,8,16,32,64
    if n==1:
        return 0
    for i in range(n*n):
        if((n*n/2**i)<1):
            print(i-1)
            break

# snakefill(24)

########################################################################################################################

## Encode Morse

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

def encode_morse(message):
    lst = list(message)
    morse = []
    final = ''
    for char in lst:
        m = char_to_dots[char.upper()]
        morse.append(m+' ')
    final = final.join(morse)
    print(final[:-1])

encode_morse("EDABBIT CHALLENGE")

########################################################################################################################

## Pentagonal Number

# Write a function that takes a positive integer num and calculates how many dots exist in a pentagonal shape around the
# center dot on the Nth iteration.
#
# In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots. On the third,
# there are 16 dots, and on the fourth there are 31 dots.

def pentagonal(num):
    if n>1:
        return (5*n*n-5*n+2)/2
    else:
        return 1

pentagonal(num)

















