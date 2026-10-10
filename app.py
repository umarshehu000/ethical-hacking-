from flask import Flask, render_template_string, request, redirect, session
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "ethical-2026-v5-final"
app.config['SESSION_PERMANENT'] = False

users = {"admin":"1234"}

LESSONS = {}
# Darussa 3 na farko da rubutu mai yawa
LESSONS[1] = {"title":"Phishing", "menene":"Phishing yaudara ce inda barawo ya yi kamar banki ko Facebook don sace password dinka.", "yadda":"1. Ya turo link na karya\n2. Link yayi kama da na gaskiya\n3. Idan ka saka password, ya dauke shi\n4. Ya shiga account dinka", "waye":"Yan damfara (Yahoo boys) da hackers.", "matsala":"Satar kudi, satar Facebook, blackmail.", "kare":"Kada ka danna link da baka sani ba\nDuba adireshi\nKunna 2FA"}
LESSONS[2] = {"title":"Strong Password", "menene":"Password mai karfi shi ne makullin gidan ka. Idan mai rauni ne, hacker zai bude shi cikin dakika 2.", "yadda":"Brute Force - gwada kalmomi miliyan a dakika.", "waye":"Kowa zai iya karya shi.", "matsala":"Satar duk account dinka.", "kare":"Yi amfani da 12 harafi: Zaria@2026!Ng"}
LESSONS[3] = {"title":"Malware", "menene":"Malware guba ce da ke lalata waya.", "yadda":"Yana shigowa ta app na karya.", "waye":"Hackers.", "matsala":"Lalata waya, sata hotuna.", "kare":"Kada ka sauke daga wajen Play Store"}

# Sauran 4-100
topics = ["Ransomware","SQL Injection","XSS","DDoS","MITM","Keylogger","Brute Force","Spyware","Trojan","Rootkit","Zero-Day","Fake Apps","SIM Swap","WhatsApp Hack","Facebook Hack","Email Spoof","OTP Bypass","Session Hijack","Cookie Theft","Data Breach","Dark Web","Cryptojacking","Botnet","Adware","Pharming","Vishing","Smishing","Baiting","Pretexting","Password Spray","Credential Stuff","Dictionary Attack","Rainbow Table","WiFi Hack","Bluetooth Hack","QR Scam","USB Drop","Shoulder Surf","Sniffing","Port Scan","Vuln Scan","Reverse Eng","Forensics","Steganography","Cryptography","2FA","Biometrics","Firewall","Antivirus","VPN","Proxy","Tor","Secure Email","HTTPS","SSL","Backup","Patch","OSINT","Social Safety","Banking Safety","ATM Skim","Carding","Identity Theft","Cyberbullying","Kids Safety","Fake News","Deepfake","AI Scam","IoT Hack","CCTV Hack","Phone Security","Android Hack","App Permission","Cloud Sec","Google Dork","Metadata","Fileless","Insider Threat","Supply Chain","BEC","RAT","Kali Linux","Bug Bounty","Pen Test","Recovery","Hacked?","Career","Ethics","Final Tips"]

for i, name in enumerate(topics, start=4):
    if i>100: break
    LESSONS[i] = {"title":name, "menene":f"{name} muhimmin bangare ne na cyber security da ya kamata ka sani.", "yadda":f"1. Bincike\n2. Shiri kayan aiki na {name}\n3. Sanya tarko\n4. Daukar bayani", "waye":f"Hackers da yan damfara ne ke yin {name}.", "matsala":f"Hadari: Satar kudi da bayani.", "kare":f"Sabunta waya\nStrong Password + 2FA\nAntivirus + VPN"}

@app.route("/", methods=["GET","POST"])
def login():
    msg=""
    if request.method=="POST":
        u=request.form["username"]; p=request.form["password"]
        if u in users and users[u]==p:
            session["user"]=u
            session.permanent=False
            return redirect("/home")
        msg="Ba daidai ba!"
    return render_template_string("""
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{background:#050a14;color:white;font-family:Arial;margin:0}.box{max-width:500px;margin:20px auto;background:#101a2e;padding:25px;border-radius:15px;border:1px solid #00ff88} input{width:95%;padding:13px;margin:8px 0;border-radius:8px;border:none} button{width:98%;padding:13px;background:#00ff88;color:black;border:none;border-radius:8px;font-weight:bold} a{color:#00ff88}.header{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88}</style>
<div class="header"><h1 style="color:#00ff88">ETHICAL HACKING</h1></div>
<div class="box"><h2>Login</h2><p style="color:orange">{{msg}}</p><form method="post"><input name="username" placeholder="Username" required><input type="password" name="password" placeholder="Password" required><button>SHIGA</button></form><p>admin / 1234 - <a href="/register">Register</a></p></div>
""", msg=msg)

@app.route("/register", methods=["GET","POST"])
def register():
    msg=""
    if request.method=="POST":
        u=request.form["username"]; p=request.form["password"]
        if u in users:
            msg="Sunan yana nan!"
        else:
            users[u]=p
            return redirect("/")
    return render_template_string("""
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{background:#050a14;color:white;font-family:Arial;margin:0}.box{max-width:500px;margin:20px auto;background:#101a2e;padding:25px;border-radius:15px;border:1px solid #00ff88} input{width:95%;padding:13px;margin:8px 0;border-radius:8px;border:none} button{width:98%;padding:13px;background:#00ff88;color:black;border:none;border-radius:8px;font-weight:bold} a{color:#00ff88}.header{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88}</style>
<div class="header"><h1 style="color:#00ff88">ETHICAL HACKING</h1></div>
<div class="box"><h2>Register</h2><p style="color:orange">{{msg}}</p><form method="post"><input name="username" placeholder="Username" required><input type="password" name="password" placeholder="Password" required><button>REGISTER</button></form><p><a href="/">Login</a></p></div>
""", msg=msg)

@app.route("/home")
def home():
    if "user" not in session: return redirect("/")
    return render_template_string("""
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#050a14;color:white;font-family:Arial;margin:0}
.header{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88;position:sticky;top:0;z-index:10}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;padding:12px;max-width:900px;margin:auto}
.card{background:#101a2e;border:1px solid #222;border-radius:12px;padding:12px;text-align:center;border-top:3px solid #00ff88}
.card:hover{border-color:#00ff88}
.num{font-size:22px;font-weight:bold;color:#00ff88}
.title{font-size:13px;margin:8px 0;min-height:32px}
.btn{display:block;padding:8px;background:#00ff88;color:black;border-radius:8px;text-decoration:none;font-weight:bold;font-size:12px}
</style>
<div class="header"><a href="/logout" style="float:right;color:#ff4444">Logout</a><h1 style="color:#00ff88;margin:0">DARUSSA 100</h1><p>Barka {{user}} - Grid Horizontal</p></div>
<div class="grid">
{% for i in range(1,101) %}
<div class="card"><div class="num">{{i}}</div><div class="title">{{lessons[i].title}}</div><a href="/lesson/{{i}}" class="btn">Karanta</a></div>
{% endfor %}
</div>
""", user=session["user"], lessons=LESSONS)

@app.route("/lesson/<int:id>")
def lesson_page(id):
    if "user" not in session: return redirect("/")
    l=LESSONS.get(id)
    if not l: return redirect("/home")
    nid = id+1 if id < 100 else 1
    pid = id-1 if id > 1 else 100
    return render_template_string("""
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#050a14;color:#e0e0e0;font-family:Arial;margin:0}
.header{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88;position:sticky;top:0}
.card{background:#101a2e;margin:12px;padding:18px;border-radius:12px;border-left:5px solid #00ff88}
.card.red{border-left-color:#ff4444}.card.blue{border-left-color:#4488ff}.card.yellow{border-left-color:#ffcc00}.card.green{border-left-color:#00ff88}
h2{color:#00ff88;font-size:17px} p{line-height:1.7;white-space:pre-line}
.btn{padding:10px 18px;background:#00ff88;color:black;border-radius:8px;text-decoration:none;font-weight:bold;margin:5px;display:inline-block}
.btn2{background:#101a2e;color:#00ff88;border:1px solid #00ff88}
</style>
<div class="header"><a href="/home" style="float:left;color:#00ff88">Home</a><a href="/logout" style="float:right;color:#ff4444">Logout</a><h1 style="color:#00ff88;font-size:16px">{{l.title}}</h1><small>Darasi {{id}}/100</small></div>
<div style="max-width:700px;margin:auto;padding-bottom:30px">
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
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))