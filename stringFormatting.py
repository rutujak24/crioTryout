'''Given an integer,n , print the following values for each integer 1 from n to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n.
Each value should be space-padded to match the width of the binary value of .'''

def print_formatted(number):
    # your code goes here
    
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        deci=str(i)
        octa=oct(i)[2:]
        hexa=(hex(i)[2:]).upper()
        bina=bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))
