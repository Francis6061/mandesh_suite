import hashlib
from colorama import Fore, Style
import itertools

class MandeshCrack:
    def __init__(self):
        self.algorithms = {
            "md5": hashlib.md5,
            "sha1": hashlib.sha1,
            "sha256": hashlib.sha256
        }

    def generate_wordlist(self, keywords, min_len, max_len, output_file):
        print(f"{Fore.CYAN}[*] Generating custom wordlist...{Style.RESET_ALL}")
        count = 0
        with open(output_file, "w") as f:
            for length in range(int(min_len), int(max_len) + 1):
                for combination in itertools.product(keywords, repeat=length):
                    word = "".join(combination)
                    f.write(word + "\n")
                    count += 1
        print(f"{Fore.GREEN}[+] Created {count} combinations in {output_file}{Style.RESET_ALL}")

    def crack_hash(self, target_hash, wordlist_path, algo):
        print(f"{Fore.YELLOW}[!] Attempting to crack hash...{Style.RESET_ALL}")
        try:
            with open(wordlist_path, "r") as f:
                for line in f:
                    word = line.strip()
                    hashed_word = self.algorithms[algo](word.encode()).hexdigest()
                    if hashed_word == target_hash:
                        print(f"{Fore.GREEN}[***] MATCH FOUND: {word}{Style.RESET_ALL}")
                        return word
            print(f"{Fore.RED}[-] Password not in wordlist.{Style.RESET_ALL}")
        except FileNotFoundError:
            print(f"{Fore.RED}[-] Wordlist file not found.{Style.RESET_ALL}")

if __name__ == "__main__":
    cracker = MandeshCrack()
    print(f"\n{Fore.RED}--- Mandesh Cracker Engine ---{Style.RESET_ALL}")
    print("[1] Generate Wordlist\n[2] Crack Hash")
    choice = input("\nSelect >> ")

    if choice == "1":
        chars = input("Enter keywords/chars (e.g. abc12): ")
        low = input("Min length: ")
        high = input("Max length: ")
        cracker.generate_wordlist(list(chars), low, high, "mandesh_list.txt")
    elif choice == "2":
        h = input("Enter hash: ")
        w = input("Wordlist path: ")
        a = input("Type (md5, sha1, sha256): ").lower()
        cracker.crack_hash(h, w, a)
