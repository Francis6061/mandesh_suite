import os
import pytsk3
from colorama import Fore, Style
from mandesh_utils import save_result

class MandeshForensic:
    def __init__(self):
        self.log_data = []
        self.sig_file = os.path.expanduser("~/mandeshHakingTools/signatures.json")
        
        # 1. Load from the JSON file
        try:
            with open(self.sig_file, "r") as f:
                hex_dict = json.load(f)
            # 2. Convert hex strings to actual bytes for the scanner
            self.signatures = {k: bytes.fromhex(v) for k, v in hex_dict.items()}
            print(f"{Fore.GREEN}[+] Loaded {len(self.signatures)} custom signatures.{Style.RESET_ALL}")
        except Exception as e:
            # Fallback if the JSON is missing or broken
            print(f"{Fore.RED}[!] Could not load signatures.json, using defaults.{Style.RESET_ALL}")
            self.signatures = {
                "jpg": b"\xff\xd8\xff",
                "png": b"\x89\x50\x4e\x47",
                "pdf": b"\x25\x50\x44\x46"
            }

    def log(self, text):
        print(text)
        self.log_data.append(text)

    def carve_by_signature(self, device_path, output_dir):
        if os.getuid() != 0:
            self.log(f"{Fore.RED}[!] Error: Run with sudo for raw disk access.{Style.RESET_ALL}")
            return

        self.log(f"{Fore.CYAN}[*] Deep Carving: {device_path}{Style.RESET_ALL}")
        os.makedirs(output_dir, exist_ok=True)

        try:
            with open(device_path, "rb") as disk:
                file_count = 0
                # Read disk in 512-byte sectors
                chunk_size = 512 
                while True:
                    chunk = disk.read(chunk_size)
                    if not chunk: break
                    
                    # Check chunk against our hex signatures
                    for ext, sig in self.signatures.items():
                        if chunk.startswith(sig):
                            file_count += 1
                            file_name = f"carved_file_{file_count}.{ext}"
                            self.log(f"{Fore.GREEN}[+] Signature Found! Carving {file_name}...{Style.RESET_ALL}")
                            
                            # Grab 1MB of data following the signature (simple carving)
                            # In a full tool, we'd look for the "Footer" signature
                            with open(f"{output_dir}/{file_name}", "wb") as f:
                                f.write(chunk + disk.read(1024 * 1024)) 
                
                self.log(f"{Fore.YELLOW}[!] Found {file_count} files via signature analysis.{Style.RESET_ALL}")

        except Exception as e:
            self.log(f"{Fore.RED}[-] Error during carving: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    forensic = MandeshForensic()
    device = input("Enter device path (e.g. /dev/sdb): ")
    out = f"Carved_Results_{device.split('/')[-1]}"
    forensic.carve_by_signature(device, out)
    
    report = "\n".join(forensic.log_data)
    save_result("CARVER", report)


"""import os
import pytsk3
from colorama import Fore, Style
from mandesh_utils import save_result

class MandeshForensic:
    def __init__(self):
        self.log_data = []

    def log(self, text):
        print(text)
        self.log_data.append(text)

    def recover_files(self, device_path, output_dir):
        if os.getuid() != 0:
            self.log(f"{Fore.RED}[!] Error: Data carving requires sudo.{Style.RESET_ALL}")
            return

        print(f"{Fore.CYAN}[*] Opening device: {device_path}{Style.RESET_ALL}")
        try:
            img = pytsk3.Img_Info(device_path)
            fs = pytsk3.FS_Info(img)
            root = fs.open_dir(path="/")
            
            os.makedirs(output_dir, exist_ok=True)
            self.log(f"[+] Scanning File System... Limit: 64GB Check Passed.")

            for fs_object in root:
                if fs_object.info.meta:
                    # Check if file is deleted (unallocated)
                    status = "DELETED" if fs_object.info.meta.flags & pytsk3.TSK_FS_META_FLAG_UNALLOC else "ACTIVE"
                    name = fs_object.info.name.name.decode('utf-8')
                    
                    self.log(f"  [{status}] Found: {name}")
                    
                    # Extracting the file for analysis
                    if status == "DELETED" or status == "ACTIVE":
                        file_data = fs_object.read_random(0, fs_object.info.meta.size)
                        with open(f"{output_dir}/{name}", "wb") as f:
                            f.write(file_data)
            
            self.log(f"{Fore.GREEN}[+] Recovery complete. Files stored in: {output_dir}{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED}[-] Forensic Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    forensic = MandeshForensic()
    print(f"\n{Fore.BLUE}--- Mandesh Forensic Data Carver ---{Style.RESET_ALL}")
    dev = input("Enter device path (e.g., /dev/sdb): ")
    out = f"Extracted_{dev.split('/')[-1]}"
    forensic.recover_files(dev, out)
    
    report = "\n".join(forensic.log_data)
    save_result("CARVER", report)
"""
