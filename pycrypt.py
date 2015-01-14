#! /usr/bin/env python3

from random import randint


class Ceaser(object):
    
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
            
        return offset
    
    def encrypt(self, text):
        
        """The function takes an input then
           then returns the encrypted output and
           key."""
        
        key = self.shift(randint(0, 26))
        encrypted_text = []
        
        for c in text:
            
            # Takes letter input then appends the output to a list.
            
            encrypted_text.append(self.new_alphabet[self.alphabet.index(c)])
        
        return "".join(encrypted_text), key # Returns the encrypted text and the key.
    
    def decrypt(self, cypher, key):
        
        decrypted_text = []
        
        for i in range(len(key)):
            
            self.shift(key[i])
            decrypted_text.append(self.alphabet[self.new_alphabet.index(
                cypher[i])])
            
        return "".join(decrypted_text)
        
    
class Nceaser(object):
    
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
        
        key = []
        encrypted_text = []
        
        for c in text:
            
            key.append(self.shift(randint(0, 26)))
            encrypted_text.append(self.new_alphabet[self.alphabet.index(c)])
        
        return "".join(encrypted_text), key
    
    def decrypt(self, cypher, key):
        
        decrypted_text = []
        
        for i in range(len(key)):
            
            self.shift(key[i])
            decrypted_text.append(self.alphabet[self.new_alphabet.index(
                cypher[i])])
            
        return "".join(decrypted_text)
        
        
        
        
        
        
        
