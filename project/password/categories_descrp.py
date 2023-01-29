CATEGORIES = [
'''
Completely unvalid due to:
    -starting the password with a number (a digit)
    -including unicode characters (ex: emojis) 
    -not including ascii lower or uppercase characters -> [a-zA-Z]
    -including whitespace characters
To have a strong password you need to follow the following rules:
    -length = 12 to 14 
    -have at least one capital letter or one digit or one special character (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)''',

'''Weak password (doesn't meet the minimum requirements):
    -due to the small length: less than 12 characters
To have a strong password you need to follow the following rules:
    -length = 12 to 14 
    -have at least one capital letter or one digit or one special character (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)''',

'''Medium strength password (doesn't meet the minimum requirements):
    -a size of 12-14 but the absence of any digits, caps or special characters
To have a strong password you need to follow the following rules:
    -length = 12 to 14 
    -have at least one capital letter or one digit or one special character (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)''',

'''Strong password (meets the minimum requirements):
    -meeting the right length and meeting one of the other rules:
        ex: 'jc87c0rstnlq3e' is a strong password as it meets 2 requirements; length and digits
    To have the strongest password (unbreakable) you need to follow all the rules''',

'''5-Unbreakable password (it's breakable with brute force theoretically but would be much harder)
    -A password that meets all the rules'''
    ]