#!/usr/bin/env python3

import hashlib
import argparse

def hash_word(word, algorithm):
    word = word.encode()
    if algorithm == 'md5':
        return hashlib.md5(word).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(word).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(word).hexdigest()
    else:
        raise ValueError("Unsupported algorithm")

def crack_hash(target_hash, wordlist_path, algorithm):
    with open(wordlist_path, 'r', errors='ignore') as f:
        for word in f:
            word = word.strip()
            if hash_word(word, algorithm) == target_hash:
                return word
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algorithm", default="md5", choices=["md5", "sha1", "sha256"], help="Hash algorithm")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist")
    parser.add_argument("-f", "--file", required=True, help="File with hashes to crack")
    args = parser.parse_args()

    with open(args.file, 'r') as hash_file:
        for line in hash_file:
            target_hash = line.strip().lower()
            result = crack_hash(target_hash, args.wordlist, args.algorithm)
            if result:
                print(f"[+] {target_hash} : {result}")
            else:
                print(f"[-] {target_hash} : NOT FOUND")


