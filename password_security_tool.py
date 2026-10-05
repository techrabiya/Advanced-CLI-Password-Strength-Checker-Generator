import random
import string

def check_password_strength(password):
    length = len(password) >= 8
    digit = any(char.isdigit() for char in password)
    upper = any(char.isupper() for char in password)
    special = any(char in string.punctuation for char in password)
    
    score = sum([length, digit, upper, special])
    
    print("-" * 50)
    print(f"Password Evaluated : {password}")
    if score == 4:
        print("Strength Rating    : 🛡️ STRONG (Elite Security)")
    elif score >= 2:
        print("Strength Rating    : ⚠️ MODERATE (Needs Improvement)")
    else:
        print("Strength Rating    : ❌ WEAK (Vulnerable)")
    print("-" * 50)

def generate_secure_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    secure_pwd = "".join(random.choice(chars) for _ in range(12))
    print(f"Generated Secure PWD: {secure_pwd}")
    print("=" * 50)

if __name__ == "__main__":
    print("=" * 50)
    print(" 🔐 RABIA'S PASSWORD SECURITY TOOL 🔐")
    print("=" * 50)
    user_pwd = input("Enter a password to test strength: ")
    check_password_strength(user_pwd)
    print("\nGenerating a recommended secure password for you:")
    generate_secure_password()
