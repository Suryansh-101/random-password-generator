from password_generator import generate_password

def get_user_input():
    try:
        length = int(input("Enter password length: "))
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
        return length, use_upper, use_digits, use_special
    except ValueError:
        print("Please enter a valid number.")
        return None

if __name__ == "__main__":
    print("Random Password Generator")
    user_input = get_user_input()
    if user_input:
        length, use_upper, use_digits, use_special = user_input
        password = generate_password(length, use_upper, use_digits, use_special)
        if password:
            print("Generated Password:", password)
