import os
from datetime import datetime
from colorama import Fore, Style

def save_result(tool_name, data, extension="txt"):
    # Ensure the directory exists
    base_dir = os.path.expanduser("~/mandeshHakingTools/Results")
    os.makedirs(base_dir, exist_ok=True)
    
    # Generate filename: TOOLNAME-sec-min-dd-mm-yyyy.ext
    timestamp = datetime.now().strftime("%S-%M-%d-%m-%Y")
    file_name = f"{tool_name}-{timestamp}.{extension}"
    full_path = os.path.join(base_dir, file_name)
    
    save_choice = input(f"\n{Fore.YELLOW}[?] Save results to {file_name}? (y/n): {Style.RESET_ALL}").lower()
    
    if save_choice == 'y':
        with open(full_path, "w") as f:
            f.write(data)
        print(f"{Fore.GREEN}[+] Results saved to: {full_path}{Style.RESET_ALL}")
    else:
        print(f"{Fore.BLUE}[i] Results not saved.{Style.RESET_ALL}")
