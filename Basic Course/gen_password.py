import random
import string

def generate_password():

    characters = string.ascii_letters + string.digits + string.punctuation

    password = []

    while(len(password) < 16):
        character = random.choice(characters)
        password.append(character)

    password = ''.join(password)
    return password

def run():
    password = generate_password()
    print(f'Your new password is {password}')
if __name__ == '__main__':
    run()