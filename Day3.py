print('Starting with Very Hard Problems')
print('Take 4 everyday')

## Magic Function

# Create a class with couple functions like these examples.
# magic.replace("string", 'char', char') is a function that replaces all of the specified characters with another characters.
# magic.str_length("string") is a function that returns the length of the string.
# magic.trim(" string ") is a function that returns a string that truncates spaces at both the beginning and end.
# magic.list_slice(list, tuple) is a function that returns the items in the list that are among the specified indexes.
# If the length of the new list is 0, return -1.

class magic:
    def replace(string,char1,char2):
        new_String = string.replace(char1,char2)
        print(new_String)

    def str_length(string):
        length = len(string)
        print(length)

    def trim(string):
        new_string = string.strip()
        print(new_string)

    def list_slice(list, tuple):
        if len(list)==0:
            print(-1)
        if tuple[0]==-1:
            print([list[tuple[1]-1]])
        else:
            newList = []
            for i in range(len(list)):
                if i>=tuple[0]-1 and i<=tuple[1]-1:
                    newList.append(list[i])
            print(newList)

magic.replace('String','S','t')
magic.str_length('String')
magic.trim("  Karan Bhai   ")
magic.list_slice([1, 2, 3, 4, 5], (-1, 4))
