#!/usr/bin/env python3

import pycrypt

enc_method = int(input("For Caesar enter 1. For Ncaesar enter 2.\n> "))
option = int(input("Enter 1 for Encryption, 2 for Decryption.\n> "))

def main(enc_method, option):

    if enc_method == 1:

        crypto = pycrypt.Caesar()

    elif enc_method == 2:

        crypto = pycrypt.Ncaesar()

    else:

        print("Please select an encryption method.")        

    if option == 1:
        
        text = input("Text to encrypt.\n> ")
               
        if enc_method == 1:
            key = input("Key.\n> ")
            output = crypto.encrypt(text, key)
        elif enc_method == 2:
            output = crypto.encrypt(text)
     
        
        print("Encrypted text:\n%s" % output[0])
        print("Key: \n%s" % output[1])

    elif option == 2:
        text = input("Text to decrypt\n> ")
        if enc_method == 1:
            key = int(input("Key\n> "))
        elif enc_method == 2:
            print("When input of key is type 'done'.")
            key = []
            while True: 
                #inpt = None
                inpt = input("Key\n> ")
                if inpt == 'done':
                    break
                else:
                    key.append(inpt)
        else:
            print("I'm too lazy to tell you why this quit. Work it out.")
        output = crypto.decrypt(text, key)
        print("Original text:\n%s" % output)
    else:
        print("Please select an option.")

if __name__ == '__main__':
    main(enc_method, option)
