import os

# Define Welcome Message Function()
def welcome():
    print("Welcome to the Caesar Cipher \n This program encrypts and decrypts text with the Caesar Cipher.\n")

# Define enter_message to get the input prompt from the user
def enter_message():
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode == 'e' or mode == 'd':
            break
        else:
            print("Invalid mode")

# Initializing the global variable.
    file_source = None
    message = None
    filename = None
    shift= 0

# Prompting the file_source from the user.
    while True:
        file_source = input("Would you like to read from a file (f) or the console (c)? ").lower()

# Checking the file_source to prompt the message or filename as per the user input.
        if file_source == 'f':
            #Ask the user prompt for filename untill valid file name is given.
            while not filename:
                filename = input("Enter a filename: ")
                if not is_file(filename):
                    print("Invalid Filename")
                    filename = None
                else:
                    while True:
                        try:
                            shift= int(input("What is the shift number: "))
                            break
                        except:
                            print("Invalid Shift")

        elif file_source == 'c':           
            while True:
                try:
                    # Asking encrypting or decrypting message as per the user's prompt
                    if (mode == "e"):
                        message = input("What message would you like to encrypt: ").upper()
                    else:
                        message = input("What message would you like to decrypt: ").upper()

                    shift= int(input("What is the shift number: "))
                    break
                except:
                    print("Invalid Shift")
        else:
            print("Invalid source")
        return mode, message, filename, shift

# Define a function to encrypt a message using the Caesar Cipher
def encrypt(message, shift):
    ciphertext = ''
    for char in message:
        if char.isalpha():
            char = chr((ord(char) - 65 + shift) % 26 + 65)
        ciphertext += char
    return ciphertext


# Define a function to decrypt a message using the Caesar Cipher
def decrypt(ciphertext, shift):

# Returning the encrypt function but with negative shift so that it will decrypt.
    return encrypt( ciphertext, -shift)

# This function check whether file exists or not. And Return boolean as per the result.
def is_file(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False

# This function write strings to a file called results.txt, with each item taking up a single line.
def write_messages(messages):
    with open("results.txt", "w") as f:
        for message in messages:
            f.write(message + "\n")

# This function  process the lines in the file one by one, returning a list of encrypted/decrypted messages.
def process_file(filename, mode, shift):
    messages = []
    with open(filename, "r") as f:
        for line in f:
            message = line.strip().upper()
            if mode == 'e':
                messages.append(encrypt(message, shift))
            else:
                messages.append(decrypt(message, shift))
    return messages


def message_or_file():
   mode, message, filename, shift =enter_message()
   return mode, message, filename, shift
 
#  This function wraps all the helper function and executes to perform encryption/decryption.
def main():
    # Calling welcome function()
    welcome()
    checker = True

    # Loops through the program untill user chooses to quit.
    while checker==True:
        mode, message, filename, shift = message_or_file()
    
    # If filename exists calls process_file() function and perform the task for file
        if filename:
            messages = process_file(filename, mode, shift)
            write_messages(messages)
            choice = input("Would you like to encrypt or decrypt another message? (y/n)").lower()

            if(choice)=="n":
                checker = False
                print("\nThanks for using the program, goodbye!")   
        else:
            if mode == 'e':
                print("Encrypted Message:", encrypt(message, shift))
            if mode =="d":
                print("Decrypted Message:", decrypt(message, shift))

            choice = input("Would you like to encrypt or decrypt another message? (y/n)").lower()
            if(choice)=="n":
                checker = False
                print("\nThanks for using the program, goodbye!")
main()
    







