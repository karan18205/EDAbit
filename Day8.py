## Burglary Series (04): Add its Name
# Given three arguments ⁠— a dictionary obj, a key name and a value ⁠— return a dictionary with that name and value in
# it (as key-value pairs).
# Example: add_name({}, "Brutus", 300) ➞ { "Brutus": 300 }

def add_name(obj, name, value):
    obj[name] = value
    return obj

add_name({}, "Brutus", 300)
add_name({ "piano": 500 }, "Brutus", 400)



## Scrambled Letters
# Write a function that receives a list of words and a mask. Return a list of words, sorted alphabetically, that match the
# given mask.

recede = ["cee","dee","eer","erd","ere","red","ree","cede","cere","cree","deer","dere","dree","rede","reed","ceder","cedre","cered","creed","decree","recede"]

def scrambled(words, mask):
    newlist = []
    final = []
    maskDict = {}

    for item in words:
        if len(item)==len(mask):
            newlist.append(item)

    for i in mask:
        if i.isalpha():
            maskDict[i] = mask.index(i)

    for item in newlist:
        count = 0
        for i in maskDict:
            if maskDict[i] == item.index(i):
                # print(item)
                count = count+1
        if count == len(maskDict):
            final.append(item)

    return final

print(scrambled(['red', 'dee', 'cede', 'reed', 'creed', 'decree'], '*re**'))
print(scrambled(['red', 'dee', 'cede', 'reed', 'creed', 'decree'], '***'))
print(scrambled(recede, "c*d**"))
print(scrambled(['red', 'dee', 'cede', 'reed', 'creed', 'decr'], "d***"))







