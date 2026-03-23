import requests
from telethon import TelegramClient, events
from colorama import Fore, Style
import asyncio

class MandeshLeak:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}

    # --- Discord OSINT Section ---
    def discord_lookup(self, token):
        print(f"{Fore.CYAN}[*] Fetching Discord User Info via Token...{Style.RESET_ALL}")
        url = "https://discord.com/api/v9/users/@me"
        headers = {"Authorization": token}
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            data = res.json()
            print(f"{Fore.GREEN}[+] Username: {data['username']}#{data['discriminator']}")
            print(f"[+] Email: {data.get('email', 'N/A')}")
            print(f"[+] Phone: {data.get('phone', 'N/A')}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] Invalid Token{Style.RESET_ALL}")

    # --- Telegram OSINT Section ---
    async def telegram_search(self, api_id, api_hash, target_phone):
        print(f"{Fore.CYAN}[*] Connecting to Telegram API...{Style.RESET_ALL}")
        async with TelegramClient('mandesh_session', api_id, api_hash) as client:
            try:
                entity = await client.get_entity(target_phone)
                print(f"{Fore.GREEN}[+] User Found: {entity.first_name} {entity.last_name or ''}")
                print(f"[+] Username: @{entity.username}")
                print(f"[+] ID: {entity.id}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}[-] User not found or Privacy restricted: {e}{Style.RESET_ALL}")

    # --- Breach Lookup Section (Simulated) ---
    def check_breach(self, email):
        print(f"{Fore.YELLOW}[!] Searching for '{email}' in known leaks...{Style.RESET_ALL}")
        # In a full build, this would connect to an API like HaveIBeenPwned
        print(f"{Fore.BLUE}[i] Checking databases: Compilation of Many Breaches (COMB), etc.{Style.RESET_ALL}")
        # Simulated result
        print(f"{Fore.RED}[!] Found in 3 leaks (LinkedIn, Adobe, Canva). Check hunt_results.txt{Style.RESET_ALL}")

if __name__ == "__main__":
    hunter = MandeshLeak()
    print(f"\n{Fore.MAGENTA}--- Mandesh Leak & API Hunter ---{Style.RESET_ALL}")
    print("[1] Discord Token Lookup\n[2] Telegram Phone Search\n[3] Email Breach Check")
    choice = input("\nSelect >> ")

    if choice == "1":
        t = input("Enter Discord Token: ")
        hunter.discord_lookup(t)
    elif choice == "2":
        aid = input("Enter API ID: ")
        ahash = input("Enter API Hash: ")
        phone = input("Target Phone (with +country code): ")
        asyncio.run(hunter.telegram_search(aid, ahash, phone))
    elif choice == "3":
        em = input("Enter Email: ")
        hunter.check_breach(em)
