from flask import Flask, render_template_string, request, redirect, session
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "umar-secret-2026-v2"
users = {"admin":"1234"}
LOG_FILE = "users_log.txt"

def save_user(u,p):
    try:
        open(LOG_FILE,"a",encoding="utf-8").write(f"{datetime.now()} - {u}:{p}\n")
    except: pass

if not os.path.exists(LOG_FILE):
    open(LOG_FILE,"w").close()

LESSONS = {
1: {"title":"1. Phishing","menene":"Phishing yaudara ce da ake yi kamar daga banki ko Facebook don sace bayanan ka.","yadda":"1. Aiko link na karya\n2. Kamar facebook.com amma faceb00k.com\n3. Idan ka saka password sai ya sace","waye":"Yan damfara, yahoo boys","matsala":"Satar kudi da account","kare":"Kada ka danna link da baka sani ba, kunna 2FA"},
2: {"title":"2. Strong Password","menene":"Password mai karfi shine makullin ka.","yadda":"Hacker na amfani da brute force","waye":"Kowa","matsala":"Duk account zai tafi","kare":"Yi amfani da Zaria@2026!Ng"},
3: {"title":"3. Malware","menene":"Virus da ke lalata waya.","yadda":"Ta app na karya","waye":"Hackers","matsala":"Lalata waya","kare":"Kada ka sauke app daga waje"},
}
extra = ["Ransomware","SQL Injection","XSS","DDoS","MITM","Keylogger","Brute Force","Spyware","Trojan","Rootkit","Zero-Day","Fake Apps","SIM Swapping","WhatsApp Hack","Facebook Hack","Email Spoofing","OTP Bypass","Session Hijacking","Cookie Theft","Data Breach","Dark Web","Cryptojacking","Botnet","Adware","Pharming","Vishing","Smishing","Baiting","Pretexting","Password Spraying","Credential Stuffing","Dictionary Attack","Rainbow Table","WiFi Hacking","Bluetooth Hacking","NFC Hacking","QR Code Scam","USB Drop","Shoulder Surfing","Eavesdropping","Port Scanning","Vuln Scanning","Reverse Engineering","Forensics","Steganography","Cryptography","2FA","Biometrics","Firewall","Antivirus","VPN","Proxy","Tor","Secure Email","HTTPS","SSL","Backup","Patch Management","OSINT","Social Media Safety","Banking Safety","ATM Skimming","Carding","Identity Theft","Cyberbullying","Kids Safety","Fake News","Deepfake","AI Scam","IoT Hacking","CCTV Hacking","Smartphone Security","Android Hacking","App Permission","Cloud Security","Google Dorking","Metadata Leak","Fileless Malware","Insider Threat","Supply Chain Attack","BEC","RAT","Kali Linux","Bug Bounty","Pen Testing","Recovery","What To Do If Hacked"]
for idx, name in enumerate(extra, start=4):
    if idx>100: break
    LESSONS[idx] = {"title":f"{idx}. {name}","menene":f"{name} muhimmin darasi ne na cyber security.","yadda":f"1. Hacker ya bincike\n2. Ya shirya tarko na {name}\n3. Ya aiko","waye":f"Hackers na {name}","matsala":f"Satar kudi da bayani ta {name}","kare":f"Sabunta waya, strong password, 2FA, kada ka danna link"}

@app.route("/", methods=["GET","POST"])
def login():
    msg=""
    if request.method=="POST":
        u=request.form["username"]; p=request.form["password"]
        if u in users and users[u]==p:
            session["user"]=u
            return redirect("/home")
        msg="Suna ko Password ba daidai ba!"
    return render_template_string("""
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{background:#050a14;color:white;font-family:Arial;margin:0}.box{max-width:500px;margin:40px auto;background:#101a2e;padding:25px;border-radius:15px;border:1px solid #00ff88} input{width:95%;padding:13px;margin:8px 0;border-radius:8px;border:none} button{width:98%;padding:13px;background:#00ff88;color:black;border:none;border-radius:8px;font-weight:bold} a{color:#00ff88}.header{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88}</style>
<div class="header"><h1 style="color:#00ff88">🎓 ETHICAL HACKING</h1><p>Umar - Zaria</p></div>
<div class="box"><h2>Login</h2><p style="color:orange">{{msg}}</p><form method="post"><input name="username" placeholder="Username" required><input type="password" name="password" placeholder="Password" required><button>SHIGA</button></form><p>Baka da account? <a href="/register">Register</a></p></div>
""", msg=msg)

@app.route("/register", methods=["GET","POST"])
def register():
    msg=""
    if request.method=="POST":
        u=request.form["username"]; p=request.form["password"]
        if u in users:
            msg="Wannan sunan yana nan!"
        else:
            users[u]=p
            save_user(u,p)
            return redirect("/")
    return render_template_string("""
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{background:#050a14;color:white;font-family:Arial;margin:0}.box{max-width:500px;margin:40px auto;background:#101a2e;padding:25px;border-radius:15px;border:1px solid #00ff88} input{width:95%;padding:13px;margin:8px 0;border-radius:8px;border:none} button{width:98%;padding:13px;background:#00ff88;color:black;border:none;border-radius:8px;font-weight:bold} a{color:#00ff88}.header{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88}</style>
<div class="header"><h1 style="color:#00ff88">🎓 ETHICAL HACKING</h1></div>
<div class="box"><h2>Register</h2><p style="color:orange">{{msg}}</p><form method="post"><input name="username" placeholder="Sabon Username" required><input type="password" name="password" placeholder="Sabon Password" required><button>REGISTER</button></form><p>Kana da account? <a href="/">Login</a></p></div>
""", msg=msg)

@app.route("/home")
def home():
    if "user" not in session: return redirect("/")
    admin_link = '<a href="/admin" style="color:#ffcc00;margin-left:10px">ADMIN</a>' if session["user"]=="admin" else ""
    html = f"""
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{{background:#050a14;color:white;font-family:Arial;margin:0}}.header{{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88;position:sticky;top:0}}.card{{background:#101a2e;margin:12px;padding:18px;border-radius:12px;border-left:4px solid #00ff88;display:inline-block;width:42%;vertical-align:top}} @media(max-width:600px){{.card{{width:85%}}}} button{{padding:10px 15px;background:#00ff88;border:none;border-radius:8px;font-weight:bold}} a{{color:#00ff88;text-decoration:none}}</style>
<div class="header"><a href="/logout" style="float:right;color:#ff4444">Logout</a>{admin_link}<h1 style="color:#00ff88">🎓 DARUSSA 100</h1><p>Barka da zuwa {session["user"]} 👨‍💻</p></div><div style="max-width:900px;margin:auto;text-align:center">
"""
    for i in range(1,101):
        html += f'<div class="card"><h3>{LESSONS[i]["title"]}</h3><a href="/lesson/{i}"><button>Karanta →</button></a></div>'
    html += "</div>"
    return render_template_string(html)

@app.route("/lesson/<int:id>")
def lesson_page(id):
    if "user" not in session: return redirect("/")
    l=LESSONS.get(id)
    if not l: return redirect("/home")
    nid = id+1 if id < 100 else 1
    pid = id-1 if id >