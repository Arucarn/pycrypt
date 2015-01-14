f#! /usr/bin/env python3

from random import randint


class Caesar(object):
    
    def shift(self, offset):
        
        """Shifts the alphabet using a random number.
           Returns the value of the shift."""
        
        self.alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', ' ', '.', ',', '!', '?', '', '\'',
            '-', '*', '\n'
            ]

        self.new_alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', ' ', '.', ',', '!', '?', '', '\'',
            '-', '*', '\n'
            ]

        for i in range(int(offset)):
            
            # Takes first index and appends it to the end.
            
            self.new_alphabet.append(self.new_alphabet.pop(0))
        #print(self.alphabet)
        #print(self.new_alphabet)    
        return offset
    
    def encrypt(self, text):
        
        """The function takes an input then
           then returns the encrypted output and key."""
        
        #text = text.lower()

        key = self.shift(randint(0, 26))
        encrypted_text = []
        
        for c in text:
            
            # Takes letter input then appends the output to a list.
            
            encrypted_text.append(self.new_alphabet[self.alphabet.index(c)])
        
        return "".join(encrypted_text), key # Returns the encrypted text and the key.
    
    def decrypt(self, cypher, key):
        
        """This function takes the encrypted text and key then returns
           the original text."""

        decrypted_text = []
        self.shift(key) # Shift alphabet using value from key.
        
        for i in range(len(cypher)):
            
            
            # Takes encrypted letter and returns original letter.
            decrypted_text.append(self.alphabet[self.new_alphabet.index(
                cypher[i])])
            
        return "".join(decrypted_text)
        
    
class Ncaesar(object):
    
    """This encryption method is like the Caesar Cypher however it does a
       different alphabet shift for each letter. This results in a more
       secure encryption method, however the key is longer."""

    def shift(self, offset):
        
        self.alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', ' ', '.', ',', '!', '?', '', '\'',
            '-', '*', '\n'
            ]

        self.new_alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', ' ', '.', ',', '!', '?', '', '\'',
            '-', '*', '\n'
            ]

        for i in range(int(offset)):
            
            self.new_alphabet.append(self.new_alphabet.pop(0))
            
        return offset
    
    def encrypt(self, text):
        
<<<<<<< HEAD
        """Does exactly the same as the Ceaser method but uses a
           different key for each letter."""
        #text = text.lower()
=======
        """Does exactly the same as the Caeser encrypt method but 
           uses a different key for each letter."""

>>>>>>> refs/remotes/origin/master
        key = []
        encrypted_text = []
        
        for c in text:
            
            # Shifts alphabet for each letter and generates key + text

            key.append(self.shift(randint(0, 26)))
            encrypted_text.append(self.new_alphabet[self.alphabet.index(c)])
        
        return "".join(encrypted_text), key
    
    def decrypt(self, cypher, key):
        
        # Decrypted each letter in text.
        decrypted_text = []
        
        for i in range(len(key)):
            
            self.shift(key[i])
            decrypted_text.append(self.alphabet[self.new_alphabet.index(
                cypher[i])])
            
        return "".join(decrypted_text)
        
        
        
        
        
        
        
