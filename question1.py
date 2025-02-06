import re

def check_password_strength(password):
    # Minimum length
    if len(password) < 8:
        return False
    
    # Uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        return False
    
    # Lowercase letter
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        return False
    
    # For digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        return False
    
    # For special character
    special_characters = "!@#$%^&*()_+-=[]{};:'\",.<>?\\/\\"
    has_special = False
    for char in password:
        if char in special_characters:
            has_special = True
            break
    if not has_special:
        return False
    
    return True

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    
    if check_password_strength(password):
        print("Strong password")
    else:
        print("Weak password!, Please provide a password that has at least 8 characters, uppercase & lowercase letters, a digit, and a special character.")
