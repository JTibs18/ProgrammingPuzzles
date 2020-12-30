#Problem from https://hunt.reaktor.com/tattoo
# Each channel is a data stream that uses a big-endian 8-bit encoding. Every byte in the channel points to another byte in the stream, i.e. the value of the byte is the offset in bytes from the beginning.
# The channels can contain invalid bytes, which means following their pointer would cause an overflow off the stream.
# Start reading data from the beginning of the channel, and ignore any invalid bytes until you encounter the first valid byte. After this, follow valid byte pointers until you reach another invalid byte.
# This invalid byte contributes one character to the password. Repeat this process for all 14 channels to read the complete password.

#This function converts 8 bit binary code into a decimal number 
#INPUT: num, an eight digit binary number (a byte) 
#OUTPUT: Returns val, the decimal number calculated from the binary number  
def toDecimal (num):
    count = 7
    val = 0
    for n in num: 
        if int(n) == 1: 
            val = val + (2 ** count)
        count = count - 1
    return val

#This function recursively finds the next byte to go to based on the pointer (previous valid number)
#INPUT: num, a valid decimal number that is a pointer. l, the number of bytes in the channel. bytes, the array of bytes in a channel that is being traversed 
#OUTPUT: num, the invalid byte that cannot act as a pointer but will represent a character in the password 
def goTo (num, l, bytes):
    if num < l:
        return goTo(bytes[num], l, bytes)
    else: 
        return num

#This main function reads in the textfile with different binary number channels, creates bytes based on the bits, 
#and finds and prints the password using the above functions 
def main(): 
    f1 = open("tattooInput.txt") 
    pw = []
    n = 8
    password = ""

    for line in f1: 
        line = line.rstrip()
        bite = []
        nums = []
        n = 8
        
        for i in range(0, len(line), n):
            bite.append(line[i:i+n])

        for b in bite: 
            nums.append(toDecimal(b))

        for count, n in enumerate(nums): 
            if nums[count] < len(nums): 
                n = goTo(nums[count], len(nums), nums)
                pw.append(n)
                break

    for a in pw: 
        password = password + chr(a)

    print(password)

if __name__ == "__main__":
    main() 