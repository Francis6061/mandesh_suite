import os
import sys
from colorama import Fore, Style

# Import custom modules with safety check
try:
    import mandesh_phish
    import mandesh_hunt
    import mandesh_audit
    import mandesh_payload
    import mandesh_bomber
    import mandesh_crack
    import mandesh_webscan
    import mandesh_leak
    import mandesh_sys
except ImportError as e:
    print(f"{Fore.RED}[!] Missing module: {e}. Check your folder!{Style.RESET_ALL}")

class MandeshGUI:
    def __init__(self):
        self.version = "1.0.0"
        self.author = "Mandesh"

    def banner(self):
        os.system('clear')
        print(f"""{Fore.RED}
  __  __                         _            _   _    _       _   _       
 |  \/  |                       | |          | | | |  | |     | | (_)      
 | \  / | __ _ _ __   __| | ___| ___| |__ | |__| | __ _| | ___ _ _ __  
 | |\/| |/ _` | '_ \ / _` |/ _ \/ __| '_ \|  __  |/ _` | |/ / | | '_ \ 
 | |  | | (_| | | | | (_| |  __/\__ \ | | | |  | | (_| |  <| | | | | |
 |_|  |_|\__,_|_| |_|\__,_|\___||___/_| |_|_|  |_|\__,_|_|\_\_|_|_| |_|
        {Fore.YELLOW}>> Advanced Penetration Testing Suite v{self.version}{Style.RESET_ALL}
        """)

    def authenticate(self):
        # Secure login gate
        user = input("Username: ")
        pw = input("Password: ")
        if user == "admin" and pw == "mandesh":
            return True
        print(f"{Fore.RED}Access Denied.{Style.RESET_ALL}")
        return False

    def menu(self):
        while True:
            self.banner()
            print(f"{Fore.CYAN}[01] Phishing Engine      [06] Security Cracker")
            print(f"[02] Identity Hunter      [07] Web Vulnerability Scan")
            print(f"[03] Network Auditor      [08] Leak & API Hunter")
            print(f"[04] Payload Generator    [09] System Utilities")
            print(f"[05] Bomber/Spammer       [10] Image Mechanic (New)")
            print(f"[11] Forensic Auditor(New)[00] Exit System{Style.RESET_ALL}")
            
            choice = input(f"\n{Fore.WHITE}mandesh@hacker ~# {Style.RESET_ALL}")

            # Execution Logic
            if choice == "01": os.system("python3 mandesh_phish.py")
            elif choice == "02": os.system("python3 mandesh_hunt.py")
            elif choice == "03": os.system("python3 mandesh_audit.py")
            elif choice == "04": os.system("python3 mandesh_payload.py")
            elif choice == "05": os.system("python3 mandesh_bomber.py")
            elif choice == "06": os.system("python3 mandesh_crack.py")
            elif choice == "07": os.system("python3 mandesh_webscan.py")
            elif choice == "08": os.system("python3 mandesh_leak.py")
            elif choice == "09": os.system("python3 mandesh_sys.py")
            elif choice == "10": os.system("python3 mandesh_img.py")
            elif choice == "11": os.system("python3 mandesh_forensic.py")
            elif choice == "00": 
                print(f"{Fore.YELLOW}Shutting down suite...{Style.RESET_ALL}")
                break
            else: 
                print(f"{Fore.RED}Invalid option!{Style.RESET_ALL}")
                os.system("sleep 1")

if __name__ == "__main__":
    app = MandeshGUI()
    if app.authenticate():
        app.menu()
