import random
import string

def generate_strong_password(length):
    """Generate a strong password with letters, digits, and special characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_random_password(length):
    """Generate a random password with letters and digits."""
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get password length from user
while True:
    try:
        password_length = int(input("Enter the desired password length: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

# Generate passwords
strong_password = generate_strong_password(password_length)
random_password = generate_random_password(password_length)

print("Strong Password:", strong_password)
print("Random Password:", random_password)
