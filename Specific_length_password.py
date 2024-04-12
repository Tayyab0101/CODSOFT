print("Welcome to password generator.")
import string
import random

length_of_pass = int(input("Enter desired password length: "))

# Define characters
alphs = string.ascii_letters
numbs = string.digits
spec = "!@#$%^&*()[]{}|<>/?"

# Determine counts for each character type
count_alpha = random.randint(1, length_of_pass - 2)  # Ensure at least 1 char for each type
count_num = random.randint(1, length_of_pass - count_alpha - 1)  # Remaining length for numbers
count_spec = length_of_pass - count_alpha - count_num  # Remaining length for special characters

# Generate password parts
password = ''.join(random.choice(alphs) for _ in range(count_alpha))
password += ''.join(random.choice(numbs) for _ in range(count_num))
password += ''.join(random.choice(spec) for _ in range(count_spec))

# Shuffle the password
pass_list = list(password)
random.shuffle(pass_list)

final_password = ''.join(pass_list)
print(final_password)
