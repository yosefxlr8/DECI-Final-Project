import random
import string 

import categories_descrp

class Password:
    ALPHA_LOW = string.ascii_lowercase
    ALPHA_HIGH = string.ascii_uppercase
    DIGITS = string.digits
    SPECIALS = string.punctuation

    CATEGORIES = categories_descrp.CATEGORIES

    def __init__(self, password, strength=None):
        self.password = password
        self.strength = strength
    
    def categorise(self):
        password = self.password
        if Password.isvalid(password):
            if len(password) < 12:
                self.strength = Password.CATEGORIES[1]
                return

            high =  digits = puncs = 0
            for char in password:
                if char.isdecimal():
                    digits = 1
                elif char in Password.SPECIALS:
                    puncs = 1
                elif char.isupper():
                    high = 1
             
            score = sum((high, digits, puncs))
            if  score == 0:
                self.strength = Password.CATEGORIES[2]
            elif score == 1:
                self.strength = Password.CATEGORIES[3]
            elif 1<score<=4 :
                self.strength = Password.CATEGORIES[4]
        else:
            self.strength = 0
        
        return

    @staticmethod
    def isvalid(password):
        valid = True
        if ' ' in password:
            valid = False
        if not password[0].isalpha():
            valid = False
        elif not password[0].isascii():
            valid = False
        return valid

    class PasswordGenerator:
        def __init__(self, length=14, caps=True, nums=True, special_chars=True):
            self.length = length 
            self.caps = caps
            self.nums = nums
            self.special_chars = special_chars

        def gen_password(self):
            characters = Password.ALPHA_LOW
            characters += Password.ALPHA_HIGH*self.caps 
            characters += Password.DIGITS*self.nums
            characters += Password.SPECIALS*self.special_chars

            password = [random.choice(characters[:52])]
            for _ in range(self.length - 1):
                character = random.choice(characters)
                password.append(character)
            return ''.join(password)
    
