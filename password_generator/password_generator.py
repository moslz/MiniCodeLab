import random
import string

def read_common_words(filename):
    with open(filename, 'r') as file:
        common_words = file.read().splitlines()
        return common_words

def common_word_password(num_common_words):
    password = ""

    if num_common_words > 0:
        common_words = read_common_words('common_words.csv')
        while num_common_words > 0:
            word = random.choice(common_words)
            modified_word = word.capitalize()
            password += modified_word
            num_common_words -= 1
    return password

def character_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range (length))
    return password 

def main():
    
    print("------------------")
    print("Password Generator")
    print("------------------")
    password_type = input("Choose password type ('Words' or 'Characters'): ").lower()

    if password_type == 'words':
        num_common_words = int(input("Enter the number of common words (within 3 to 9): "))
        while num_common_words < 3 and num_common_words >= 10:
            print("Number of common words must be within 3 to 9.")
            num_common_words = int(input("Enter the number of common words: "))
    
        password = common_word_password(num_common_words)
        print("Generated Password: ", password)

    elif password_type == 'characters':
        length = int(input("Enter desired password length (minimum 8): "))
        while length < 8:
            print("Password length must be at least 8 characters.")
            length = int(input("Enter desired password length (minimum 8): "))
        
        password = character_password(length) 
        print("Generated Password: ", password)

    else:
        print("Invalid password type choice.")
    
if __name__ == "__main__":
    main()
