import os
import psutil
import shutil
import platform
from datetime import datetime
from colorama import Fore, Style

class MandeshSys:
    def view_system(self):
        print(f"{Fore.CYAN}--- System Information ---{Style.RESET_ALL}")
        print(f"OS: {platform.system()} {platform.release()}")
        print(f"Node: {platform.node()}")
        print(f"CPU Usage: {psutil.cpu_percent()}%")
        print(f"RAM Usage: {psutil.virtual_memory().percent}%")
        
        # Chromebook battery check (Linux path)
        bat = psutil.sensors_battery()
        if bat:
            print(f"Battery: {bat.percent}% {'(Charging)' if bat.power_plugged else ''}")

    def create_backup(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"mandesh_backup_{timestamp}.zip"
        print(f"{Fore.YELLOW}[!] Creating backup of project files...{Style.RESET_ALL}")
        # Archive the current directory
        shutil.make_archive(f"../{backup_name.replace('.zip', '')}", 'zip', os.getcwd())
        print(f"{Fore.GREEN}[+] Backup saved to: {os.path.abspath('../' + backup_name)}{Style.RESET_ALL}")

    def clear_logs(self):
        # Cleans up the results files created by other tools
        logs = ["credentials.txt", "hunt_results.txt", "scan_results.json", "mandesh_list.txt"]
        for log in logs:
            if os.path.exists(log):
                os.remove(log)
                print(f"{Fore.RED}[-] Deleted: {log}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Environment Cleaned.{Style.RESET_ALL}")

if __name__ == "__main__":
    sys_tool = MandeshSys()
    print(f"\n{Fore.BLUE}[1] View System Stats\n[2] Create Project Backup\n[3] Clear Tool Logs{Style.RESET_ALL}")
    choice = input("\nSelect >> ")

    if choice == "1": sys_tool.view_system()
    elif choice == "2": sys_tool.create_backup()
    elif choice == "3": sys_tool.clear_logs()
