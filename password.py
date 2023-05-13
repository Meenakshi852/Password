import string
import random

def generate_password(length):
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    password = "".join(s[0:length])
    return password

if __name__=="__main__":
    while True:
        try:
            length=int(input("Enter password length: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid length. Please enter a positive integer.")

    password = generate_password(length)
    print("Your Password is:", password)

    # Evaluate password strength
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    is_strong = len(password) >= 8 and has_lowercase and has_uppercase and has_digit and has_special
    if is_strong:
        print("This is a strong password.")
    else:
        print("This password could be stronger.")
