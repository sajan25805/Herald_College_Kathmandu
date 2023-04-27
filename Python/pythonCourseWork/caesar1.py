import os

def welcome():
    print("Welcome to the Caesar Cipher \n This program encrypts and decrypts text with the Caesar Cipher.\n")

def enter_message():
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode == 'e' or mode == 'd':
            break
        else:
            print("Invalid mode\n")
    
    while True:
        source = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if source == 'c':
            message = input("What message would you like to " + ("decrypt: " if mode == 'd' else "encrypt: ")).upper()
            while True:
                try:
                    shift = int(input("What is the shift number: "))
                    break
                except:
                    print("Invalid Shift")
            return mode, message, shift
        else:
            print("Invalid source\n")

def encrypt(message, shift):
    ciphertext = ''
    for char in message:
        if char.isalpha():
            char = chr((ord(char) - 65 + shift) % 26 + 65)
        ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            char = chr((ord(char) - 65 - shift) % 26 + 65)
        plaintext += char
    return plaintext

def is_file(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False


def write_messages(messages):
    with open("results.txt", "w") as f:
        for message in messages:
            f.write(message + "\n")

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
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode == 'e' or mode == 'd':
            break
        else:
            print("Invalid mode\n")

    source = None
    message = None
    filename = None
    shift= 0

    while not (message or filename):
        source = input("Would you like to read from a file (f) or the console (c)? ").lower()

        if source == 'f':
            while not filename:
                print("File Name:",filename)
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

        elif source == 'c':
            mode, message, shift = enter_message()  
        else:
            print("Invalid source\n")
    print("Mode",mode,"Message",message,"File Name:",filename,"Shift" ,shift)
    return mode, message, filename, shift

def main():
    welcome()
    checker = True
    while checker==True:
        mode, message, filename, shift = message_or_file()
        print("Shifts",shift)
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
            else:
                print("Decrypted Message:", decrypt(message, shift))   
main()

