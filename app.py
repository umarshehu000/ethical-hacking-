from flask import Flask, render_template_string, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = "umar-final-v6-100"
app.config['SESSION_PERMANENT'] = False

users = {"admin":"1234"}

# === DARUSSA 100 CIKAKKE ===
DATA = {
1: ("Phishing", "Phishing yaudara ce inda barawo ya yi kamar banki ko Facebook don sace password.", "1. Ya turo link na karya\n2. Link yayi kama da na gaskiya\n3. Idan ka saka password ya dauke shi", "Yan damfara da hackers", "Satar kudi da account", "Kada ka danna link da baka sani ba, duba adireshi, kunna 2FA"),
2: ("Strong Password", "Password mai karfi shi ne makullin gidan ka. Idan mai rauni ne, za a bude shi cikin dakika 2.", "Brute Force - software da ke gwada kalmomi miliyan", "Kowa zai iya karya shi", "Satar duk account", "Yi amfani da 12 harafi: Babba+karami+lamba+alama"),
3: ("Malware", "Malware guba ce da ke lalata waya/computer.", "Yana shigowa ta app na karya da ka sauke", "Hackers", "Lalata waya, sata hotuna", "Kada ka sauke daga wajen Play Store, saka Antivirus"),
}

EXTRA = ["Ransomware","SQL Injection","XSS Attack","DDoS","Man in Middle","Keylogger","Brute Force","Spyware","Trojan","Rootkit","Zero Day","Fake Apps","SIM Swapping","WhatsApp Hack","Facebook Hack","Email Spoofing","OTP Bypass","Session Hijack","Cookie Theft","Data Breach","Dark Web","Cryptojacking","Botnet","Adware","Pharming","Vishing","Smishing","Baiting","Pretexting","Password Spray","Credential Stuff","Dictionary Attack","Rainbow Table","WiFi Hacking","Bluetooth Hack","QR Scam","USB Drop","Shoulder Surf","Sniffing","Port Scanning","Vuln Scanning","Reverse Engineering","Forensics","Steganography","Cryptography","2FA","Biometrics","Firewall","Antivirus","VPN","Proxy","Tor Browser","Secure Email","HTTPS","SSL Certificate","Backup","Patch Management","OSINT","Social Safety","Banking Safety","ATM Skimming","Carding","Identity Theft","Cyberbullying","Kids Safety","Fake News","Deepfake","AI Scam","IoT Hacking","CCTV Hack","Phone Security","Android Hack","App Permission","Cloud Security","Google Dorking","Metadata Leak","Fileless Malware","Insider Threat","Supply Chain Attack","Business Email","RAT","Kali Linux","Bug Bounty","Pen Testing","Account Recovery","What If Hacked","Ethical Career","Final Tips"]

for i, name in enumerate(EXTRA, start=4):
    if i>100: break
    DATA[i] = (name, f"{name} wani muhimmin bangare ne na cyber security da ya kamata ka sani don kare kanka.", f"1. Bincike\n2. Shiri kayan aiki na {name}\n3. Sanya tarko\n4. Daukar bayani", f"Hackers da yan damfara ne ke yin {name}", f"Hadari: Satar kudi da bayanan sirri", f"Sabunta waya\nStrong Password + 2FA\nKada ka danna link\nAntivirus + VPN")

LESSONS = {}
for k,v in DATA.items():
    LESSONS[k] = {"title":v[0], "menene":v[1], "yadda":v[2], "waye":v[3], "matsala":v[4], "kare":v[5]}

@app.route("/", methods=["GET","POST"])
def login():
    if request.method=="POST":
        u=request.form["username"]
        if u in users and request.form["password"]==users[u]:
            session["user"]=u
            session.permanent=False
            return redirect("/home")
    return """
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{background:#050a14;color:white;font-family:Arial;text-align:center;padding:20px}.box{max-width:400px;margin:30px auto;background:#101a2e;padding:25px;border-radius:15px;border:1px solid #00ff88} input{width:90%;padding:12px;margin:8px;border-radius:8px;border:none} button{width:95%;padding:12px;background:#00ff88;border:none;border-radius:8px;font-weight:bold}</style>
<div style="color:#00ff88"><h1>ETHICAL HACKING</h1></div>
<div class="box"><h2>Login</h2><form method="post"><input name="username" placeholder="Username" required><br><input type="password" name="password" placeholder="Password" required><br><button>SHIGA</button></form><p>admin / 1234 | <a href="/register" style="color:#00ff88">Register</a></p></div>
"""

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        u=request.form["username"]; p=request.form["password"]
        if u not in users:
            users[u]=p
            return redirect("/")
    return """
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{background:#050a14;color:white;font-family:Arial;text-align:center;padding:20px}.box{max-width:400px;margin:30px auto;background:#101a2e;padding:25px;border-radius:15px;border:1px solid #00ff88} input{width:90%;padding:12px;margin:8px;border-radius:8px;border:none} button{width:95%;padding:12px;background:#00ff88;border:none;border-radius:8px;font-weight:bold}</style>
<div style="color:#00ff88"><h1>ETHICAL HACKING</h1></div>
<div class="box"><h2>Register</h2><form method="post"><input name="username" placeholder="Username" required><br><input type="password" name="password" placeholder="Password" required><br><button>REGISTER</button></form><p><a href="/" style="color:#00ff88">Login</a></p></div>
"""

@app.route("/home")
def home():
    if "user" not in session: return redirect("/")
    html = """
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#050a14;color:white;font-family:Arial;margin:0}
.header{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88;position:sticky;top:0}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;padding:12px;max-width:800px;margin:auto}
.card{background:#101a2e;border-radius:12px;padding:12px;text-align:center;border-top:3px solid #00ff88;border:1px solid #222}
.card:hover{border-color:#00ff88}
.num{color:#00ff88;font-weight:bold;font-size:18px}
.title{font-size:13px;margin:6px 0;min-height:32px}
.btn{display:block;background:#00ff88;color:black;padding:7px;border-radius:7px;text-decoration:none;font-weight:bold;font-size:12px;margin-top:6px}
</style>
<div class="header"><a href="/logout" style="float:right;color:#ff4444">Logout</a><h2 style="color:#00ff88;margin:0">DARUSSA 100 - HORIZONTAL</h2><small>Barka """ + session["user"] + """</small></div><div class="grid">
"""
    for i in range(1,101):
        t = LESSONS[i]["title"]
        html += f'<div class="card"><div class="num">{i}</div><div class="title">{t}</div><a href="/lesson/{i}" class="btn">Karanta</a></div>'
    html += '</div>'
    return render_template_string(html)

@app.route("/lesson/<int:id>")
def lesson_page(id):
    if "user" not in session: return redirect("/")
    l=LESSONS.get(id)
    if not l: return redirect("/home")
    nid = id+1 if id<100 else 1
    pid = id-1 if id>1 else 100
    return render_template_string("""
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#050a14;color:#e0e0e0;font-family:Arial;margin:0}
.header{background:#001122;padding:12px;text-align:center;border-bottom:2px solid #00ff88;position:sticky;top:0}
.card{background:#101a2e;margin:12px;padding:16px;border-radius:10px;border-left:5px solid #00ff88}
.card.red{border-left-color:#ff4444}.card.blue{border-left-color:#4488ff}.card.yellow{border-left-color:#ffcc00}.card.green{border-left-color:#00ff88}
h2{color:#00ff88;font-size:16px} p{line-height:1.6;white-space:pre-line;font-size:14px}
.btn{padding:10px 16px;background:#00ff88;color:black;border-radius:8px;text-decoration:none;font-weight:bold;margin:5px;display:inline-block}
.btn2{background:#101a2e;color:#00ff88;border:1px solid #00ff88}
</style>
<div class="header"><a href="/home" style="float:left;color:#00ff88">Home</a><a href="/logout" style="float:right;color:#ff4444">Logout</a><h3 style="color:#00ff88;margin:0">{{id}}. {{l.title}}</h3></div>
<div style="max-width:700px;margin:auto;padding-bottom:20px">
<div class="card blue"><h2>1. Menene Wannan?</h2><p>{{l.menene}}</p></div>
<div class="card yellow"><h2>2. Yadda Ake Yinshi</h2><p>{{l.yadda}}</p></div>
<div class="card"><h2>3. Waye Ke Yi?</h2><p>{{l.waye}}</p></div>
<div class="card red"><h2>4. Matsala</h2><p>{{l.matsala}}</p></div>
<div class="card green"><h2>5. Yadda Za Ka Kare Kai</h2><p>{{l.kare}}</p></div>
<div style="text-align:center"><a href="/lesson/{{pid}}" class="btn btn2">Baya</a><a href="/lesson/{{nid}}" class="btn">Gaba</a><br><br><a href="/home" class="btn btn2">Komawa Grid</a></div>
</div>
""", l=l, id=id, nid=nid, pid=pid)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",10000)))