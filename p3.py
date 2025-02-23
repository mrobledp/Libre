import secrets

# Generate a secure random token of hexadecimal format
hex_token = secrets.token_hex(16)  # Generates a 32-character hex token
print(f"Hex Token: {hex_token}")

# Generate a secure random URL-safe token
url_token = secrets.token_urlsafe(16)  # Generates a URL-safe token
print(f"URL-safe Token: {url_token}")

# Generate a random integer below a given number
random_number = secrets.randbelow(100)
print(f"Random Number below 100: {random_number}")

# Securely choose a random element from a sequence
choices = ['apple', 'banana', 'cherry']
secure_choice = secrets.choice(choices)
print(f"Securely chosen fruit: {secure_choice}")
