import sys
import time
from itertools import product
import string
import hashlib

def read_file(path):
    """
    This function is for reading file
    """
    hashes = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Process each line here
                hashes.append(line.strip())
        return hashes
    except FileNotFoundError:
        print("File not found. please provide the correct path for hash file")
        return None
def find_password(hash_arr):
    """
    This function takes arrays of hashes and find corresponding passwords
    """
    start = time.time()
    counter = 0
    lowercase_letters = list(string.ascii_lowercase)
    # Password containing 1 to 6 characters.
    for i in range(1, 7):
        # This is for creating different combinations of lowercase letters
        for letter in product(lowercase_letters, repeat=i):
            password = ''.join(letter)
            hash_value = hashlib.sha1(password.encode('utf-8')).hexdigest()
            # This counter is for stopping the program if all 6 passwords were found
            if counter == 6:
                break
            if hash_value in hash_arr:
                end = time.time()
                print(hash_value, "\t", password, "\t", round(end - start, 2))
                counter += 1
if __name__ == "__main__":
    # Hash file path should be provided as command line argument.
    hash_values = []
    if len(sys.argv) > 1:
        FILE_PATH = sys.argv[1]
        hash_values = read_file(FILE_PATH)
        print("******* Parsing hash values to find out passwords ******\n")
        print("hash_value", "\t","\t","\t","\t","\t", "password","\t", "time(second): ")
        find_password(hash_values)
    else:
        print("Please provide the hash file path.")
