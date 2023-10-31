import random
import string

def generate_password(numbers=True,special_characters=True,minimum_length=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
        
        
    password = ""
    me_criteria = False
    has_number = False
    has_special = False
    
    while not me_criteria or len(password)<minimum_length:
        new_char = random.choice(characters)
        password += new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
            
        me_criteria = True
        if numbers:
            me_criteria = has_number
        if special_characters:
            me_criteria = me_criteria and has_special
            
    return password        
    
minimum_length = int(input("Enter the minimum length: "))
has_number = input("Do you have numbers(y/n)?").lower()=="y"
has_special = input("Do you have characters(y/n)?").lower()=="y"
password = generate_password(has_number, has_special,minimum_length)

print("The generate password is :", password)
