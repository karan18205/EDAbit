## Prime Divisors

#Given a number, return all its prime divisors in a list. Create a function that takes a number as an argument and
# returns all its prime divisors.
# n = 27
# All divisors: [3, 9, 27]
# Finally, from that list of divisors, return the prime ones: [3]

def prime_divisors(num):
    factors=[1]
    final = []
    d=2
    while(d*d<=num):
        while(num>1):
            while num%d==0:
                factors.append(d)
                num=num/d
            d+=1
    final_set = set(factors)
    final = list(final_set)
    return final

# print(prime_divisors(100))

########################################################################################################################

## Numbers to English
# Write a function that accepts a positive integer between 0 and 999 inclusive and returns a string representation of that
# integer written in English.
#num_to_eng(0) ➞ "zero"

ones = {
        0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
        7: 'seventy', 8: 'eighty', 9: 'ninety'}

def _divide(dividend, divisor, magnitude):
    return _join(
        _say_number_pos(dividend // divisor),
        magnitude,
        _say_number_pos(dividend % divisor),
    )

def _join(*args):
    return ' '.join(filter(bool, args))

def _say_number_pos(i):
    if i < 20:
        return ones[i]
    if i < 100:
        return _join(tens[i // 10], ones[i % 10])
    if i < 1000:
        return _divide(i, 100, 'hundred')

def num_to_eng(n):

    if n == 0 :
        return "zero"
    else:
        return _say_number_pos(n)

print(num_to_eng(99))
print(num_to_eng(106))
print(num_to_eng(519))
print(num_to_eng(0))








