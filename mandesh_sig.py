import json
import os
from colorama import Fore, Style

class SignatureManager:
    def __init__(self):
        self.config_path = os.path.expanduser("~/mandeshHakingTools/signatures.json")
        self.default_sigs = {
            "jpg": "ffd8ff",
            "png": "89504e47",
            "pdf": "25504446",
            "zip": "504b0304"
        }
        self.load_signatures()

    def load_signatures(self):
        if not os.path.exists(self.config_path):
            with open(self.config_path, "w") as f:
                json.dump(self.default_sigs, f)
        with open(self.config_path, "r") as f:
            self.sigs = json.load(f)

    def add_signature(self, ext, hex_str):
        # Validation: Hex strings should be even-length
        if len(hex_str) % 2 != 0:
            print(f"{Fore.RED}[-] Invalid Hex string!{Style.RESET_ALL}")
            return
        
        self.sigs[ext.lower()] = hex_str.lower()
        with open(self.config_path, "w") as f:
            json.dump(self.sigs, f)
        print(f"{Fore.GREEN}[+] Added {ext} signature: {hex_str}{Style.RESET_ALL}")

    def list_signatures(self):
        print(f"\n{Fore.CYAN}--- Current Forensic Signatures ---{Style.RESET_ALL}")
        for ext, hex_val in self.sigs.items():
            print(f"  {Fore.YELLOW}{ext.upper()}:{Style.RESET_ALL} {hex_val}")

if __name__ == "__main__":
    manager = SignatureManager()
    print(f"\n{Fore.MAGENTA}[1] List Signatures\n[2] Add New Signature{Style.RESET_ALL}")
    choice = input("\nSelect >> ")

    if choice == "1":
        manager.list_signatures()
    elif choice == "2":
        e = input("File Extension (e.g., mp3): ")
        h = input("Hex Header (e.g., 494433): ")
        manager.add_signature(e, h)
