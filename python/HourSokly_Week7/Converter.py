class Converter:
 def binarytodecimal (binary):
    decimal = 0 

    for digit in binary:
        decimal = decimal * 2 + int (digit)
    print("The decimal value is: ", decimal)

 def decimaltobinary (number):
    num= int(number)
    if num>=1: 
        Converter.decimaltobinary(num // 2)
        print(num % 2, end='')
