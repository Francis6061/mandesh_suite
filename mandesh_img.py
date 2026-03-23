import os
from PIL import Image
import hexdump
from colorama import Fore, Style

class MandeshImg:
    def img_to_ascii(self, img_path):
        print(f"{Fore.CYAN}[*] Converting image to ASCII...{Style.RESET_ALL}")
        try:
            img = Image.open(img_path).convert('L')
            width, height = img.size
            aspect_ratio = height/width
            new_width = 80
            new_height = int(aspect_ratio * new_width * 0.5)
            img = img.resize((new_width, new_height))
            
            chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
            pixels = img.getdata()
            new_pixels = [chars[pixel//25] for pixel in pixels]
            
            ascii_img = "".join(new_pixels)
            # Split the string into lines
            for i in range(0, len(ascii_img), new_width):
                print(ascii_img[i:i+new_width])
                
        except Exception as e:
            print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

    def read_hex(self, file_path):
        print(f"{Fore.CYAN}[*] Reading Hex of {file_path}...{Style.RESET_ALL}")
        try:
            with open(file_path, 'rb') as f:
                # Read first 1kb to avoid flooding the screen
                data = f.read(1024)
                print(hexdump.hexdump(data))
                print(f"{Fore.YELLOW}[!] Only showing first 1KB of data.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

    def hide_file_in_img(self, img_path, file_to_hide, output_path):
        print(f"{Fore.CYAN}[*] Hiding file in image (Steganography)...{Style.RESET_ALL}")
        try:
            # Open the image
            with open(img_path, 'rb') as img_f:
                img_data = img_f.read()
            
            # Open the file to hide
            with open(file_to_hide, 'rb') as hide_f:
                hide_data = hide_f.read()
            
            # Simple steganography by appending the data
            with open(output_path, 'wb') as out_f:
                out_f.write(img_data)
                out_f.write(hide_data)
            
            print(f"{Fore.GREEN}[+] Data hidden successfully. Output: {output_path}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[!] Data is hidden at the end of the image file.{Style.RESET_ALL}")

        except Exception as e:
            print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    tool = MandeshImg()
    print(f"\n{Fore.MAGENTA}--- Mandesh Image Mechanic ---{Style.RESET_ALL}")
    print("[1] Image to ASCII\n[2] Read Image Hex (1KB Sample)\n[3] Hide File in Image")
    choice = input("\nSelect >> ")

    if choice == "1":
        img = input("Path to image: ")
        tool.img_to_ascii(img)
    elif choice == "2":
        img = input("Path to file/image: ")
        tool.read_hex(img)
    elif choice == "3":
        img = input("Path to cover image: ")
        f_to_h = input("Path to file to hide: ")
        out = input("Output image name: ")
        tool.hide_file_in_img(img, f_to_h, out)
