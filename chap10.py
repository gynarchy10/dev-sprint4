# 10.7

def letter_word(string1,string2):
    """
    Check if letters in string1 exist in string2.
    The output will be the number of letters in string1 that exist in string2.
    """
    count = 0
    for letter in string2:
        if letter in string1:
            count += 1
        else:
            return 0
    return count

def if_anagrams(string1,string2):
    """
    Check if string1 and string2 are anagrams.
    """
    check = letter_word(string1, string2)
    if check == len(string1):
        return True
    else:
        return False

#print letter_word('ban','nab')
#print if_anagrams('nab','ban')

#10.13

def iinterlock(string1,string2):
    """
    Interlocking letters from two strings that have the same length.
    """
    s1 = list(string1)
    s2 = list(string2)
    word = []
    for i in range(len(string1)):
        combined = s1[i] + s2[i]
        word += combined
    return ''.join(word)

print interlock('shoe', 'cold')
    
    