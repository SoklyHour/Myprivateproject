from Converter import Converter 
print("Do you want to convert binary to decimal or decimal to binary?")

choice= int(input("binary to decimal = 1, decimal to binary = 2: "))
if choice == 1:
    binary = input("Enter the binary number: ")
    Converter.binarytodecimal(binary)
    
elif choice ==2:
    number= input("Enter the decimal number: ")
    print("The binary number is: ",end= '')
    Converter.decimaltobinary(number)