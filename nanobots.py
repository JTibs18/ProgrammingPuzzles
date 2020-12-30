# #Problem from https://hunt.reaktor.com/nanobots 
# The control signal you receive from the nanobot swarm looks like garbage. Something in this girl's body is interfering with all your instruments.
# To get the correct readings and allow your nanobots to function, you need to do a recalibration by finding a new base value. The base value is embedded in the signal.
# What you know now:
# The first character of the base value is the single most frequently occurring character in the signal.
# Each following character of the base value is the one that occurs the most frequently in the signal immediately after the previous character of the base value. For example, if the first character of the base value is A, then the second character of the base value is the one that occurs the most frequently immediately after A in the signal.
# The most frequently occurring character after the last character of the base value is ;.

#This function finds the maximum frequency of character appearances from the keys in a dictionary 
#INPUT: frequency; a dictionary with characters as keys and their frequency as values 
#OUTPUT: max_keys[0]; the first key with the maximum frequency in the dictonary 
def findChar(frequency):
    max_value = max(frequency.values()) 
    max_keys = [k for k, v in frequency.items() if v == max_value] 
    return max_keys[0]

#This function finds the next character that appears immediately after the largest frequency character 
#INPUT: characters; a string of characters from the given input text. baseVal; the current character with the largest frequency  
#OUTPUT: nextChar; a list of characters that appear immediately after the baseVal character in the input text 
def findNextChar(characters, baseVal):
    nextChar = []
    for count, c in enumerate(characters): 
        if c == baseVal: 
            nextChar.append(characters[count + 1])
    return nextChar 

#This function finds the number of times each character appears in the given input text
#INPUT: signal; a string of characters from the given input text. 
#OUTPUT: frequency; a dictionary of characters as keys and the frequency, number of appearances, as values  
def getFrequency(signal): 
    frequency = {} 
    for c in signal: 
        if c in frequency: 
            val = frequency.get(c)
            val = val + 1
            frequency[c] = val 
        else: 
            frequency[c] = 1
    return frequency

#This main function controls the flow of the program by reading the input text and using the above functions to create the base value
def main(): 
    baseValue = ""
    f1 = open("nanobotsInput.txt") 
    
    for line in f1: 
        line = line.rstrip()

    frequency = getFrequency(line)
    newC = findChar(frequency)
    
    while newC != ";": 
        baseValue = baseValue + newC  
        nChars = findNextChar(line, newC)
        frequency = getFrequency(nChars)
        newC = findChar(frequency)
    
    print(baseValue)

if __name__ == "__main__":
    main() 