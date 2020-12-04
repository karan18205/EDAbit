print('Starting with Very Hard Problems')
print('Take 3 everyday')

## Atbash Cipher

# The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the
# alphabet: A <=> Z; B <=> Y; C <=> X; etc.
#
# Create a function that takes a string and applies the Atbash cipher to it.

atbash_cipher = {'A': 'Z', 'a': 'z', 'B': 'Y', 'b': 'y', 'C': 'X', 'c': 'x', 'D': 'W', 'd': 'w', 'E': 'V', 'e': 'v',
                 'F': 'U', 'f': 'u', 'G': 'T', 'g': 't', 'H': 'S', 'h': 's', 'I': 'R', 'i': 'r', 'J': 'Q', 'j': 'q',
                 'K': 'P', 'k': 'p', 'L': 'O', 'l': 'o', 'M': 'N', 'm': 'n', 'N': 'M', 'n': 'm', 'O': 'L', 'o': 'l',
                 'P': 'K', 'p': 'k', 'Q': 'J', 'q': 'j', 'R': 'I', 'r': 'i', 'S': 'H', 's': 'h', 'T': 'G', 't': 'g',
                 'U': 'F', 'u': 'f', 'V': 'E', 'v': 'e', 'W': 'D', 'w': 'd', 'X': 'C', 'x': 'c', 'Y': 'B', 'y': 'b',
                 'Z': 'A', 'z': 'a', ' ': ' ', '.': '.', ',': ',', '?': '?', '!': '!', '\'': '\'', '\"': '\"', ':': ':',
                 ';': ';', '\(': '\)', '\)': '\)', '\[': '\[', '\]': '\]', '\-': '\-', '1': '1', '2': '2', '3': '3',
                 '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0'}

def atbash(txt):
    final = []
    ans = ''
    for atbc in txt:
        if atbc in atbash_cipher.keys():
            final.append(atbash_cipher[atbc])
    ans = ans.join(final)
    return ans

# atbash("Hello world!")
# atbash("Hello")

########################################################################################################################

## Concert Seats

# Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if
# it is strictly greater than the number before it.
#
# Everyone can see the front-stage in the example below:
#
# # FRONT STAGE
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 2, 2],
# [5, 5, 5, 5, 4, 4],
# [6, 6, 7, 6, 5, 5]]
#
# # Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# # 6 > 5 > 4 > 2 - so all numbers can see, etc.

def can_see_stage(seats):
    count = 0
    flag = 0
    new_list = [list(i) for i in zip(*seats)]
    for i in range(len(new_list)):
        res = []
        if len(new_list[i]) != len([res.append(x) for x in new_list[i] if x not in res]):
            flag = 1
        if new_list[i] == sorted(new_list[i]):
            count = count + 1
    if flag == 1:
        print('No')
    elif count == len(new_list):
        print('Yes')
    else:
        print('No')

    print(seats)

# can_see_stage([
#     [1, 2, 2],
#     [1, 2, 3],
#     [4, 4, 4]
# ])
#
# can_see_stage(
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 2, 2],
# [5, 5, 5, 5, 4, 4],
# [6, 6, 7, 6, 5, 5]])

########################################################################################################################

# Shortest Subarray Whose Sum Exceeds N
# Write a function that returns the length of the shortest contiguous sublist whose sum of all elements strictly exceeds n.

def min_length(lst, n):

    min_len = len(lst) + 1

    for start in range(0, len(lst)):

        curr_sum = lst[start]

        if (curr_sum > n):
            return 1

        for end in range(start + 1, len(lst)):

            curr_sum += lst[end]
            if curr_sum > n and (end - start + 1) < min_len:
                min_len = (end - start + 1)
                # print(min_len,len(lst))

    if min_len>len(lst):
        return -1

    return min_len

print(min_length([5, 8, 2, -1, 3, 4], 9))
print(min_length([0, 1, 1, 0], 2))
print(min_length([-1, 1, 1, 0, 1, 1], 3))




