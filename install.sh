#!/bin/bash

# MandeshHakinTools Automated Installer
echo -e "\e[32m[+] Updating system repositories...\e[0m"
sudo apt update -y

echo -e "\e[32m[+] Installing system-level dependencies...\e[0m"
sudo apt install nmap tcpdump sleuthkit libtsk-dev python3-pip python3-venv -y

# 1. Create the environment if it doesn't exist
if [ ! -d "haking_env" ]; then
    echo -e "\e[34m[*] Creating Python Virtual Environment (haking_env)...\e[0m"
    python3 -m venv haking_env
else
    echo -e "\e[34m[*] Virtual environment already exists. Skipping creation.\e[0m"
fi

# 2. Activate and Install
echo -e "\e[32m[+] Activating environment and installing requirements...\e[0m"
source haking_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 3. Final Permissions
chmod +x main.py
echo -e "\e[32m[+] Setup Complete!\e[0m"
echo -e "\e[33m[!] Use 'source haking_env/bin/activate' before running main.py\e[0m"
