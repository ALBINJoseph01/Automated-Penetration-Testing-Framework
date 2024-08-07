# modules/password_cracker.py
import hashlib

def hash_password(password, algorithm='sha256'):
    if algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    # Add more algorithms as needed
    else:
        raise ValueError(f"Unsupported hashing algorithm: {algorithm}")

def crack_password(hash_to_crack, wordlist_path, algorithm='sha256'):
    try:
        with open(wordlist_path, 'rb') as wordlist:  # Open in binary mode
            for word in wordlist:
                try:
                    word = word.decode('utf-8', errors='ignore').strip()  # Decode with error handling
                    hashed_word = hash_password(word, algorithm)
                    if hashed_word == hash_to_crack:
                        return f"Password found: {word}"
                except UnicodeDecodeError:
                    continue  # Skip the word if it can't be decoded
    except FileNotFoundError:
        return f"Wordlist file not found: {wordlist_path}"
    return "Password not found in wordlist."

def run(hash_to_crack, wordlist_path, algorithm='sha256'):
    result = crack_password(hash_to_crack, wordlist_path, algorithm)
    return result
