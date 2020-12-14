## Exact Factorial Bounds
# Create a recursive function that tests if a number is the exact upper bound of the factorial of n. If so, return a list
# that contains the exact factorial bound and n, or otherwise, the string "Not exact!".

def is_exact(n):
    orig = n
    i = 1;
    while (True):
        if (n % i == 0):
            n //= i;
        else:
            break;
        i += 1;
    if (n == 1):
        return [orig,i-1];
    else:
        return 'Not Exact';

# print(is_exact(720))


########################################################################################################################

## The Centrifuge Problem
# A centrifuge, as you probably know, is a laboratory device used to separate fluids based on density. The separation is
# achieved through centripetal force by spinning a collection of test tubes at high speeds. This means, the configuration
# needs to be in balance.
#
# Create a function that takes two numbers as arguments n and k and returns True if the configuration is balanced and
# False if it's not. To check out the formula, look at the resources tab.

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


def subArraySum(arr, sum):
    n = len(arr)
    for i in range(n):
        curr_sum = arr[i]
        j = i + 1
        while j <= n:
            if curr_sum == sum:
                return 1
            if curr_sum > sum or j == n:
                break
            curr_sum = curr_sum + arr[j]
            j += 1
    return 0

def c_fuge(n, k):
    num = [k,n-k]
    primeDiv = prime_divisors(n)
    if subArraySum(primeDiv,n-k) == 1 and subArraySum(primeDiv, n) == 1:
        return True
    else:
        return False

print(c_fuge(3, 3))