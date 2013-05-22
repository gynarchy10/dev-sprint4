#11.9
def histogram(list):
    """
    Creating a dictionary from string or list. The key is the letter and the value is the number of times it appears in the string/list.
    """
    d = dict()
    for c in list:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
    
    
def has_duplicates (word):
    """
    Checks if any value in the dictionary have a value > 1 or appears more than once in the list using the histogram function.
    """
    d = histogram(word)
    for k in d:
        if d[k] > 1:
            return True 
        else:
            return False
    
#print histrogram("word")
#print has_duplicates("ap")


#11.10

def rotate_char(char,shift):
    """
    Shifts a character a number of times.
    """
    if char.isupper():
        number = ord(char) - 65
        newNumber = (number + shift) % 26
        newChar = chr(newNumber + 65)
    elif char.islower():
        number = ord(char) - ord('a')
        newNumber = (number + shift) % 26
        newChar = chr(newNumber + ord('a'))
    else:
        return char
    return newChar

def rotate_word(string,shift):
    """
    Shifts characters in a word a number of times.
    """
    word = ""
    index = 0
    while index < len(string):
        letter = string[index]
        word += rotate_char(letter,shift)
        index += 1
    return word
 
def word_shifts(word):
    """
    Creating a list for all 25 ways to rotate the word.
    """
    d = []
    shift = 0
    while shift < 26:
        words = rotate_word(word,shift)
        d.append(words)
        shift += 1
    return d

def word_dict():
    """
    Creating a dictionary from the word list - making it easier to search with Python.
    """
    fin = open('words.txt')
    d = dict()
    i = 0
    for line in fin:
        word = line.strip()
        d[word] = i
        i += 1
    return d

def rotate_pair(word):
    """
    Checking if the any of the rotated words exist in the word list.
    """
    allwords = word_dict()
    shifted = word_shifts(word)
    meh = dict()
    list = []
    for i in shifted:
        if i in allwords:
            list.append(i)
    if len(list) == 1:
        pass
    else:
        meh[word] = list
    if len(meh) == 0:
        pass
    else:
        return meh
    

        
print rotate_pair('baa')                
