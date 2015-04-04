import pycrypt

crypto = pycrypt.Caesar()
q= "no"

while q== "no":
    a= input("Would you like to encrypt(e) or decrypt(d)? ")

    if a=="e":
        b= input("Please enter text: ")
        key = input("Please enter key: ")
        c= crypto.encrypt(b, key)
        print("Your encrypted text:", c)
    elif a=="d":
        b= input("Please enter encrypted text: ")
        d= input("Please enter key: ")
        c= crypto.decrypt(b, d)
        print("Your decrypted text:", c)

    q= input("Would you like to quit? ")
