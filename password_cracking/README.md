
# Password Cracking

The `password_cracking.py` script is a simple Python script that attempts to crack hashed passwords. It takes a file containing hashed passwords as input and tries to find the corresponding passwords by generating various combinations of lowercase letters.

## Requirements

- Python 3.11.3 or later
- `hashlib` module
- `string` module

## Usage

1. Create a text file with the hashed passwords you want to crack. Each hashed password should be on a separate line.
2. Save the text file with a ".txt" extension. For example, "passwords.txt".
3. Place the `password_cracking.py` script in the same directory as the password file.
4. Open a command prompt or terminal and navigate to the directory where the script is located.
5. Run the script using the following command: `python password_cracking.py passwords.txt`
   - Replace "passwords.txt" with the actual file name of your password file.

## Output

The script will start processing the hashed passwords and attempt to find the corresponding passwords. For each successful match, it will display the hash value, the password, and the time taken to find the password.

Example output:
```
hash_value                           password     time(second):
5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8    password    0.12
6dcd4cecd79895048e02c186b3486a3127b11182    secret      0.35
```

## Notes

- The script uses a brute-force approach by generating combinations of lowercase letters to form passwords.
- It only considers passwords containing 1 to 6 characters in length.
- The script utilizes the SHA-1 hashing algorithm (`hashlib.sha1`) to hash the generated passwords and compare them with the provided hashed passwords.

## Disclaimer

This script is intended for educational and informational purposes only. Please ensure that you have the necessary permissions and legal rights before attempting to crack passwords. Unauthorized access or use of passwords is illegal and unethical.

