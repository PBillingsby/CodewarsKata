def getCount(inputStr):
    num_vowels = 0
    for i in inputStr:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            num_vowels += 1
    return num_vowels
