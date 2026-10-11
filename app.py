from flask import Flask, request, redirect, session
import os, json

app = Flask(__name__)
app.secret_key = "umar-secret-final-v7-2026"
app.config['SESSION_PERMANENT'] = False

# --- AJIYE USERS ---
FILE = "users_db.json"
def load_users():
    if os.path.exists(FILE):
        try:
            with open(FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"admin": {"password": "1234", "email": "admin@local.com"}}

def save_users(data):
    try:
        with open(FILE, 'w') as f:
            json.dump(data, f)
    except:
        pass

users = load_users()

# --- DARUSSA 100 ---
LESSON_DATA = {
1: ("Phishing - Damfarar Link", "Phishing shine yadda barawo ke turo maka sako kamar daga banki ne, ya ce ka danna link. Link din na karya ne, da zarar ka saka password, ya dauke shi.", "Matakai:\n1. Ya turo SMS/Email kamar na gaskiya\n2. Link yayi kama da na banki (misali: firstbank-nigeria-secure.com)\n3. Idan ka saka bayanai, ya tura zuwa server dinsa", "Yan damfara a Telegram, WhatsApp, Email", "Satar kudi a account, satar Facebook/WhatsApp", "1. Kada ka taba danna link daga SMS\n2. Koyaushe duba adireshin website da kyau\n3. Kunna 2FA a duk account dinka\n4. Kira banki kai tsaye"),
2: ("Strong Password - Makullin Karfi", "Password mai rauni ana karya shi cikin dakika 2 da software. Password mai karfi yana dauke da harafi babba, karami, lamba, da alama.", "Hacker na amfani da Brute Force Tool kamar Hydra wanda ke gwada kalmomi miliyan a minti daya", "Kowa zai iya, yaro karami ma", "Shiga duk account dinka da satar kudi", "1. Yi password mai tsayi 12+\n2. Misali: Zaria@2026!Secure\n3. Kada ka sake amfani da password daya a waje 2\n4. Yi amfani da Google Password Manager"),
}
extra_names = ["Malware","Ransomware","SQL Injection","XSS Attack","DDoS Attack","Man in Middle","Keylogger","Spyware","Trojan Horse","Rootkit","Zero Day","Fake Apps","SIM Swapping","WhatsApp Hacking","Facebook Hacking","Email Spoofing","OTP Bypass","Session Hijacking","Cookie Theft","Data Breach","Dark Web","Cryptojacking","Botnet","Adware","Pharming","Vishing Call","Smishing SMS","Baiting","Pretexting","Password Spray","Credential Stuffing","Dictionary Attack","Rainbow Table","WiFi Hacking","Bluetooth Hack","QR Code Scam","USB Drop Attack","Shoulder Surfing","Sniffing","Port Scanning","Vulnerability Scan","Reverse Engineering","Digital Forensics","Steganography","Cryptography","Two Factor Auth","Biometrics","Firewall","Antivirus","VPN","Proxy Server","Tor Browser","Secure Email","HTTPS","SSL Certificate","Backup Strategy","Patch Update","OSINT","Online Safety","Banking Safety","ATM Skimming","Carding","Identity Theft","Cyberbullying","Kids Online Safety","Fake News","Deepfake Video","AI Scam","IoT Hacking","CCTV Hacking","Phone Security","Android Security","App Permission","Cloud Security","Google Dorking","Metadata Leak","Fileless Malware","Insider Threat","Supply Chain Attack","Business Email Compromise","RAT Remote Access","Kali Linux Basics","Bug Bounty","Penetration Testing","Account Recovery","What If You Are Hacked","Ethical Hacking Career","Final Protection Tips"]

for i, name in enumerate(extra_names, start=3):
    if i>100: break
    LESSON_DATA[i] = (name, f"{name} wani babban barazana ne a duniyar internet a yanzu. Yana nufin hanyar da hacker ke amfani da ita don shiga tsarin ka ba tare da izini ba. Dole ka san yadda yake aiki don ka kare kanka.", f"Yadda {name} yake aiki:\n1. Bincike akan wanda za a kai hari (Reconnaissance)\n2. Shiri kayan aiki na musamman\n3. Aika tarko ta hanyar link, file, ko WiFi\n4. Da zarar ka danna, ya shiga tsarinka\n5. Ya dauki abin da yake so a boye", f"Yan damfara, Hackers, kungiyoyin masu satar bayani ne ke yin {name}. Suna aiki a Telegram, Dark Web.", f"Hadari: Satar kudi, satar hotuna da bidiyo, lalata waya, toshe waya sai an biya kudi, cin mutunci a social media.", f"Hanyar Kariya daga {name}:\n1. Koyaushe sabunta wayarka da apps\n2. Yi amfani da Strong Password da 2FA\n3. Kada ka danna link da baka sani ba\n4. Saka Antivirus mai kyau (kamar Bitdefender)\n5. Yi amfani da VPN idan kana WiFi na waje")

# --- STYLE GUDA DAYA ---
def page_style():
    return """
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#050a14;color:#e0e0e0;font-family:Arial, sans-serif;margin:0}
.box{max-width:400px;margin:25px auto;background:#101a2e;padding:22px;border-radius:14px;border:1px solid #1a2a4a}
input{width:100%;padding:12px;margin:8px 0;border-radius:8px;border:1px solid #222;background:#0a1220;color:white;box-sizing:border-box}
.btn{width:100%;padding:12px;background:#00ff88;color:#000;border:none;border-radius:8px;font-weight:bold;cursor:pointer;margin-top:8px}
.btn2{background:transparent;color:#00ff88;border:1px solid #00ff88}
.header{background:#001122;padding:12px;text-align:center;border-bottom:2px solid #00ff88;position:sticky;top:0;z-index:10}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:9px;padding:10px;max-width:800px;margin:auto}
.card{background:#101a2e;border-radius:10px;padding:10px;text-align:center;border-top:3px solid #00ff88}
.showpass{position:relative}
.eye{position:absolute;right:10px;top:50%;transform:translateY(-50%);cursor:pointer;color:#00ff88;font-size:12px;background:#001122;padding:4px 8px;border-radius:4px}
a{color:#00ff88;text-decoration:none}
.card2{background:#101a2e;margin:12px;padding:15px;border-radius:10px;border-left:4px solid #00ff88}
</style>
"""

def show_pass_js():
    return """
<script>
function toggle(id, el){
 var x=document.getElementById(id);
 if(x.type==='password'){x.type='text'; el.innerText='BOYE';}
 else{x.type='password'; el.innerText='NUNA';}
}
</script>
"""

# --- LOGIN ---
@app.route("/", methods=["GET","POST"])
def login():
    global users
    users = load_users()
    msg=""
    if request.method=="POST":
        u=request.form.get("username","").strip()
        p=request.form.get("password","")
        if u in users and users[u]["password"]==p:
            session["user"]=u
            session.permanent=False
            return redirect("/home")
        else:
            msg="Username ko Password ba daidai ba!"
    return page_style()+show_pass_js()+f"""
<body><div style="text-align:center;padding:20px;color:#00ff88"><h1>ETHICAL HACKING</h1><small>Zaria Security Academy</small></div>
<div class="box"><h3 style="text-align:center">LOGIN</h3>
<p style="color:#ff6666;text-align:center">{msg}</p>
<form method="post">
<input name="username" placeholder="Username" required>
<div class="showpass"><input id="p1" name="password" type="password" placeholder="Password" required><span class="eye" onclick="toggle('p1',this)">NUNA</span></div>
<button class="btn">SHIGA</button>
</form>
<p style="text-align:center;margin-top:12px"><a href="/forgot">Manta Password?</a> | <a href="/register">Yi Register</a></p>
<p style="text-align:center;font-size:11px;color:#888">admin / 1234 - shine admin</p>
</div></body>
"""

@app.route("/register", methods=["GET","POST"])
def register():
    global users
    users = load_users()
    msg=""
    if request.method=="POST":
        u=request.form.get("username","").strip()
        p=request.form.get("password","")
        e=request.form.get("email","").strip()
        if not u or not p:
            msg="Cika duka!"
        elif u in users:
            msg="Username ya riga ya wanzu!"
        else:
            users[u]={"password":p, "email":e}
            save_users(users)
            return redirect("/")
    return page_style()+show_pass_js()+f"""
<body><div style="text-align:center;padding:20px;color:#00ff88"><h1>REGISTER</h1></div>
<div class="box"><p style="color:#ff6666;text-align:center">{msg}</p>
<form method="post">
<input name="username" placeholder="Saka Username" required>
<input name="email" placeholder="Email (optional)">
<div class="showpass"><input id="p2" name="password" type="password" placeholder="Password" required><span class="eye" onclick="toggle('p2',this)">NUNA</span></div>
<button class="btn">YI REGISTER</button>
</form><p style="text-align:center"><a href="/">Koma Login</a></p></div></body>
"""

@app.route("/forgot", methods=["GET","POST"])
def forgot():
    users = load_users()
    msg="Saka username naka, zamu nuna maka password dinka (saboda demo)."
    res=""
    if request.method=="POST":
        u=request.form.get("username","").strip()
        if u in users:
            res=f"Password dinka shine: <b style='color:#00ff88'>{users[u]['password']}</b>"
        else:
            res="Ba a samu username din ba."
    return page_style()+f"""
<body><div class="box"><h3>Forgot Password</h3><p style="font-size:13px">{msg}</p>
<form method="post"><input name="username" placeholder="Username" required><button class="btn">NEMO PASSWORD</button></form>
<p style="text-align:center;color:#00ff88">{res}</p><p style="text-align:center"><a href="/">Koma Login</a></p></div></body>
"""

@app.route("/home")
def home():
    if "user" not in session:
        return redirect("/")
    grid=""
    for i in range(1,101):
        t=LESSON_DATA.get(i, (f"Darasi {i}",))[0]
        grid+=f'<div class="card"><div style="color:#00ff88;font-weight:bold">{i}</div><div style="font-size:12px;margin:6px 0;min-height:30px">{t}</div><a href="/lesson/{i}" style="background:#00ff88;color:#000;padding:5px 10px;border-radius:6px;font-size:11px;font-weight:bold;display:block">KARANTA</a></div>'
    admin_link=""
    if session["user"]=="admin":
        admin_link='<a href="/admin" style="color:#ffcc00;margin-left:10px">ADMIN PANEL</a>'
    return page_style()+f"""
<body><div class="header"><a href="/logout" style="float:right;color:#ff4444">Logout</a><h3 style="color:#00ff88;margin:0">DARUSSA 100</h3><small>Barka {session["user"]} {admin_link}</small></div>
<div class="grid">{grid}</div></body>
"""

@app.route("/lesson/<int:id>")
def lesson(id):
    if "user" not in session:
        return redirect("/")
    if id not in LESSON_DATA:
        return redirect("/home")
    t,m,y,w,ma,k = LESSON_DATA[id]
    nid = id+1 if id<100 else 1
    pid = id-1 if id>1 else 100
    return page_style()+f"""
<body><div class="header"><a href="/home" style="float:left">Home</a><a href="/logout" style="float:right;color:#ff4444">Logout</a><h3 style="color:#00ff88;margin:0">{id}. {t}</h3></div>
<div style="max-width:700px;margin:auto;padding:10px">
<div class="card2" style="border-left-color:#4488ff"><h3 style="color:#4488ff">1. Menene Wannan?</h3><p style="white-space:pre-line;line-height:1.6">{m}</p></div>
<div class="card2" style="border-left-color:#ffcc00"><h3 style="color:#ffcc00">2. Yadda Ake Yi</h3><p style="white-space:pre-line;line-height:1.6">{y}</p></div>
<div class="card2"><h3>3. Waye Ke Yi?</h3><p style="white-space:pre-line;line-height:1.6">{w}</p></div>
<div class="card2" style="border-left-color:#ff4444"><h3 style="color:#ff4444">4. Matsalar Da Yake Jawo</h3><p style="white-space:pre-line;line-height:1.6">{ma}</p></div>
<div class="card2" style="border-left-color:#00ff88"><h3 style="color:#00ff88">5. Yadda Za Ka Kare Kai</h3><p style="white-space:pre-line;line-height:1.6">{k}</p></div>
<div style="text-align:center;margin:15px"><a href="/lesson/{pid}" style="padding:10px 16px;border:1px solid #00ff88;border-radius:8px;margin:5px;display:inline-block">BAYA</a><a href="/lesson/{nid}" style="padding:10px 16px;background:#00ff88;color:#000;border-radius:8px;margin:5px;display:inline-block;font-weight:bold">GABA</a><br><br><a href="/home" style="padding:8px 14px;border:1px solid #555;border-radius:8px">KOMAWa GRID</a></div>
</div></body>
"""

@app.route("/admin")
def admin_panel():
    if "user" not in session or session["user"]!="admin":
        return redirect("/")
    users = load_users()
    rows=""
    for u, info in users.items():
        rows+=f"<tr><td style='border:1px solid #333;padding:8px'>{u}</td><td style='border:1px solid #333;padding:8px'>{info.get('password')}</td><td style='border:1px solid #333;padding:8px'>{info.get('email','')}</td></tr>"
    return page_style()+f"""
<body><div class="header"><a href="/home" style="float:left">Home</a><h3 style="color:#ffcc00">ADMIN PANEL - SIRRI</h3></div>
<div style="max-width:700px;margin:auto;padding:15px">
<div class="card2"><h3 style="color:#ffcc00">Duk Passwords da aka Ajiye</h3><p style="font-size:12px;color:#888">Wannan wuri ne a Render Dashboard kai kadai admin kake iya gani. Wannan file yana cikin users_db.json</p>
<table style="width:100%;border-collapse:collapse;margin-top:10px"><tr style="background:#001122"><th style="border:1px solid #333;padding:8px">Username</th><th style="border:1px solid #333;padding:8px">Password</th><th style="border:1px solid #333;padding:8px">Email</th></tr>{rows}</table>
<br><p style="font-size:11px;color:#888">Render dashboard: Ana ajiye su a file users_db.json. Ko da user ya manta, zaka iya dubo anan.</p>
</div></div></body>
"""

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))