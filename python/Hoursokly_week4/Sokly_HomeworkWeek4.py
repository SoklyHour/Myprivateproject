app=True
while app ==True:

    choice = input("Type'e' to encrypt, type'd'to decrypt: ")
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))

    upperalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    loweralphabets = "abcdefghijklmnopqrstuvwxyz"

    encrypt,decrypt="",""

    for letter in message:
        if letter in upperalphabets:
            new_position=(upperalphabets.find(letter)+shift)%len(loweralphabets)
            encrypt+=upperalphabets[new_position]
        elif letter in loweralphabets:
            new_position=(loweralphabets.find(letter)+shift)%len(loweralphabets)
            encrypt+=loweralphabets[new_position]

    for letter in message:
        if letter in upperalphabets:
            new_position=(upperalphabets.find(letter)-shift)%len(upperalphabets)
            decrypt+=upperalphabets[new_position]
        elif letter in loweralphabets:
            new_position=(loweralphabets.find(letter)-shift)%len(loweralphabets)
            decrypt+=loweralphabets[new_position]
            
    if choice == 'e':
        print("Your e message is",encrypt)


    if choice == 'd':
        print("Your d message is",decrypt)
    
    decision = input("Do you want restart the application?: (y/n)")

    if decision == "n":
        app = False
        print("Thank you for using our application!")
    else:
        print("invalid input")