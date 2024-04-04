import random
import string

def gen_pass(length):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("Get your desired Password!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length should be atleast one figure.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    password = gen_pass(length)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
