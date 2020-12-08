print('Starting with Very Hard Problems')
print('Take 3 everyday')

## Identity Matrix
# An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom right.
# The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of relativity.
# Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge, if
# the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. It does not matter if the
# mirror image is left-right or top-bottom.

def id_mtrx(n):
    if n>0:
        m = [[0 for x in range(n)] for y in range(n)]
        for i in range(0, n):
            m[i][i] = 1
        return m
    elif n<0:
        m = [[0 for x in range(-n)] for y in range(-n)]
        for i in range(0, -n):
            m[i][i] = 1
        for i in range(len(m)):
            m[i].reverse()
        return m
    elif n==0:
        return []
    else:
        return 'Error'

# print(id_mtrx(-2))

########################################################################################################################

## Prison Break

# A prison can be represented as a list of cells. Each cell contains exactly one prisoner. A 1 represents an unlocked cell
# and a 0 represents a locked cell.
# [1, 1, 0, 0, 0, 1, 0]
# Starting inside the leftmost cell, you are tasked with seeing how many prisoners you can set free, with a catch. You
# are the prisoner in the first cell. If the first cell is locked, you cannot free anyone. Each time you free a prisoner,
# the locked cells become unlocked, and the unlocked cells become locked again.

def freed_prisoners(prison):
    if prison[0]==0:
        return 0
    else:
        if __name__ == "__main__":
            t = int(input())
            for _ in range(t):
                n = int(input())
                s = input()
                s2 = ""
                flag = True
                for i in range(0, len(s), n):
                    if flag:
                        s2 += s[i:i + n]
                    else:
                        t = s[i:i + n]
                        s2 += t[::-1]
                    flag = not flag
                res = ""
                for i in range(0, n):
                    for j in range(i, len(s2), n):
                        res += s2[j]
                print(res)

########################################################################################################################

## Splitting Up Numbers

# Create a function that takes a number num and returns each place value in the number.

def num_split(num):
    if num>0:
        lst = [int(d) for d in str(num)]
        w_lst = [ele for ele in reversed(lst)]
        finallst = []
        for i in range(len(lst)):
            finallst.append(w_lst[i]*(10**i))
        finallst = [ele for ele in reversed(finallst)]
        return finallst
    else:
        lst = [int(d) for d in str(-num)]
        w_lst = [ele for ele in reversed(lst)]
        finallst = []
        final = []
        for i in range(len(lst)):
            finallst.append(w_lst[i]*(10**i))
        finallst = [ele for ele in reversed(finallst)]
        for item in finallst:
            final.append(-item)
        return final

print(num_split(123))
print(num_split(-434))



