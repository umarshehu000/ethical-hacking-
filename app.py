from flask import Flask, request, redirect, session
import os, json

app = Flask(__name__)
app.secret_key = "umar-v8-dark-light"
app.config['SESSION_PERMANENT'] = False

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

LESSON_DATA = {
1: ("Phishing - Damfarar Link", "Phishing shine yadda barawo ke turo maka sako kamar daga banki ne, ya ce ka danna link. Link din na karya ne.", "1. Ya turo SMS/Email kamar na gaskiya\n2. Link yayi kama da na banki\n3. Idan ka saka bayani ya dauke shi", "Yan damfara a Telegram/WhatsApp", "Satar kudi da Facebook", "Kada ka danna link, duba URL, kunna 2FA"),
2: ("Strong Password", "Password mai rauni ana karya shi cikin dakika 2.", "Brute Force Tool ke gwada kalmomi miliyan", "Kowa", "Satar account", "Yi 12 harafi, babba+karami+lamba+alama"),
}
extra = ["Malware","Ransomware","SQL Injection","XSS","DDoS","Man in Middle","Keylogger","Spyware","Trojan","Rootkit","Zero Day","Fake Apps","SIM Swap","WhatsApp Hack","Facebook Hack","Email Spoof","OTP Bypass","Session Hijack","Cookie Theft","Data Breach","Dark Web","Cryptojack","Botnet","Adware","Pharming","Vishing","Smishing","Baiting","Pretexting","Password Spray","Credential Stuff","Dictionary Attack","Rainbow Table","WiFi Hack","Bluetooth Hack","QR Scam","USB Drop","Shoulder Surf","Sniffing","Port Scan","Vuln Scan","Reverse Eng","Forensics","Steganography","Cryptography","2FA","Biometrics","Firewall","Antivirus","VPN","Proxy","Tor","Secure Email","HTTPS","SSL","Backup","Patch","OSINT","Online Safety","Banking Safety","ATM Skim","Carding","ID Theft","Cyberbully","Kids Safety","Fake News","Deepfake","AI Scam","IoT Hack","CCTV Hack","Phone Sec","Android Sec","App Perm","Cloud Sec","Google Dork","Metadata","Fileless Mal","Insider Threat","Supply Chain","BEC","RAT","Kali Linux","Bug Bounty","Pen Test","Account Recovery","If Hacked","Career","Final Tips"]
for i, n in enumerate(extra, start=3):
    if i>100: break
    LESSON_DATA[i]=(n, f"{n} babban barazana ne a internet. Dole ka sani don kare kanka.", f"1. Bincike\n2. Shiri kayan aiki\n3. Aika tarko\n4. Daukar bayani", "Hackers ne ke yi", "Satar kudi da bayani", "Sabunta waya, Strong Password + 2FA, Antivirus, VPN")

def base_style():
    return """
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root{--bg:#050a14;--card:#101a2e;--text:#e0e0e0;--head:#001122;--green:#00ff88}
.light{--bg:#f2f4f8;--card:#ffffff;--text:#111;--head:#ffffff;--green:#008f4c}
body{background:var(--bg);color:var(--text);font-family:Arial;margin:0;transition:0.3s}
.box{max-width:420px;margin:20px auto;background:var(--card);padding:20px;border-radius:14px;border:1px solid #333}
input{width:100%;padding:12px;margin:7px 0;border-radius:8px;border:1px solid #444;background:var(--bg);color:var(--text);box-sizing:border-box}
.btn{width:100%;padding:12px;background:var(--green);color:#fff;border:none;border-radius:8px;font-weight:bold;cursor:pointer;margin-top:8px}
.btn2{background:transparent;color:var(--green);border:1px solid var(--green)}
.header{background:var(--head);padding:12px;text-align:center;border-bottom:2px solid var(--green);position:sticky;top:0;z-index:10}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:9px;padding:10px;max-width:800px;margin:auto}
.card{background:var(--card);border-radius:10px;padding:10px;text-align:center;border-top:3px solid var(--green);box-shadow:0 2px 5px rgba(0,0,0,0.2)}
.card2{background:var(--card);margin:12px;padding:15px;border-radius:10px;border-left:4px solid var(--green)}
.showpass{position:relative}.eye{position:absolute;right:10px;top:50%;transform:translateY(-50%);cursor:pointer;color:var(--green);font-size:11px;background:var(--head);padding:4px 8px;border-radius:4px}
a{color:var(--green);text-decoration:none}
</style>
<script>
// THEME
function loadTheme(){let t=localStorage.getItem('theme'); if(t==='light'){document.body.classList.add('light')}}
function toggleTheme(){document.body.classList.toggle('light'); localStorage.setItem('theme', document.body.classList.contains('light')?'light':'dark')}
function togglePass(id,el){var x=document.getElementById(id); if(x.type==='password'){x.type='text';el.innerText='BOYE'}else{x.type='password';el.innerText='NUNA'}}
window.onload=loadTheme
</script>
"""

@app.route("/", methods=["GET","POST"])
def login():
    global users; users=load_users(); msg=""
    if request.method=="POST":
        u=request.form.get("username","").strip(); p=request.form.get("password","")
        if u in users and users[u]["password"]==p:
            session["user"]=u; return redirect("/home")
        else: msg="Password ko Username ba daidai ba!"
    return base_style()+f"""
<body><div style="text-align:center;padding:18px;color:var(--green)"><h1>ETHICAL HACKING</h1></div>
<div class="box"><h3 style="text-align:center">LOGIN</h3><p style="color:#ff5555;text-align:center">{msg}</p>
<form method="post"><input name="username" placeholder="Username" required>
<div class="showpass"><input id="p1" name="password" type="password" placeholder="Password" required><span class="eye" onclick="togglePass('p1',this)">NUNA</span></div>
<button class="btn">SHIGA</button></form>
<p style="text-align:center"><a href="/forgot">Manta Password?</a> | <a href="/register">Register</a> | <a href="#" onclick="toggleTheme()">🌗 Dark/Light</a></p>
<p style="font-size:11px;text-align:center">admin / 1234 shine admin</p></div></body>
"""

@app.route("/register", methods=["GET","POST"])
def register():
    global users; users=load_users(); msg=""
    if request.method=="POST":
        u=request.form.get("username","").strip(); p=request.form.get("password",""); e=request.form.get("email","").strip()
        if u in users: msg="Username ya riga ya wanzu!"
        else: users[u]={"password":p,"email":e}; save_users(users); return redirect("/")
    return base_style()+f"""
<body><div class="box"><h3>REGISTER</h3><p style="color:#ff5555">{msg}</p>
<form method="post"><input name="username" placeholder="Username" required><input name="email" placeholder="Email (optional)">
<div class="showpass"><input id="p2" name="password" type="password" placeholder="Password" required><span class="eye" onclick="togglePass('p2',this)">NUNA</span></div>
<button class="btn">REGISTER</button></form><p><a href="/">Login</a> | <a href="#" onclick="toggleTheme()">🌗 Theme</a></p></div></body>
"""

@app.route("/forgot", methods=["GET","POST"])
def forgot():
    users=load_users(); res=""
    if request.method=="POST":
        u=request.form.get("username","").strip()
        if u in users: res=f"Password dinka: <b style='color:var(--green)'>{users[u]['password']}</b>"
        else: res="Ba a samu ba"
    return base_style()+f"""<body><div class="box"><h3>Forgot Password</h3><form method="post"><input name="username" placeholder="Username" required><button class="btn">NEMO</button></form><p style="text-align:center">{res}</p><a href="/">Login</a></div></body>"""

@app.route("/home")
def home():
    if "user" not in session: return redirect("/")
    grid="";
    for i in range(1,101):
        t=LESSON_DATA[i][0]
        grid+=f'<div class="card"><div style="color:var(--green);font-weight:bold">{i}</div><div style="font-size:12px;margin:6px 0;min-height:32px">{t}</div><a href="/lesson/{i}" style="background:var(--green);color:#fff;padding:6px 10px;border-radius:6px;font-size:11px;font-weight:bold;display:block">KARANTA</a></div>'
    admin_link='<a href="/admin" style="color:#ffcc00">ADMIN PANEL</a>' if session["user"]=="admin" else ""
    return base_style()+f"""<body><div class="header"><div style="float:right"><a href="/settings">⚙️ Setting</a> | <a href="/logout" style="color:#ff5555">Logout</a></div><h3 style="color:var(--green);margin:0">DARUSSA 100</h3><small>Barka {session["user"]} {admin_link}</small></div><div class="grid">{grid}</div></body>"""

@app.route("/lesson/<int:id>")
def lesson(id):
    if "user" not in session: return redirect("/")
    t,m,y,w,ma,k=LESSON_DATA[id]; nid=id+1 if id<100 else 1; pid=id-1 if id>1 else 100
    return base_style()+f"""<body><div class="header"><a href="/home" style="float:left">Home</a><a href="/settings" style="float:right">⚙️</a><h3 style="color:var(--green);margin:0">{id}. {t}</h3></div>
<div style="max-width:700px;margin:auto;padding:10px"><div class="card2" style="border-left-color:#4488ff"><h3 style="color:#4488ff">1. Menene?</h3><p style="white-space:pre-line">{m}</p></div>
<div class="card2" style="border-left-color:#ffcc00"><h3 style="color:#ffcc00">2. Yadda Ake Yi</h3><p style="white-space:pre-line">{y}</p></div>
<div class="card2"><h3>3. Waye Ke Yi?</h3><p>{w}</p></div><div class="card2" style="border-left-color:#ff4444"><h3 style="color:#ff4444">4. Matsala</h3><p>{ma}</p></div><div class="card2"><h3 style="color:var(--green)">5. Kariya</h3><p style="white-space:pre-line">{k}</p></div>
<div style="text-align:center"><a href="/lesson/{pid}" style="padding:10px 15px;border:1px solid var(--green);border-radius:8px;margin:5px;display:inline-block">BAYA</a><a href="/lesson/{nid}" style="padding:10px 15px;background:var(--green);color:#fff;border-radius:8px;margin:5px;display:inline-block">GABA</a></div></div></body>"""

@app.route("/settings", methods=["GET","POST"])
def settings():
    if "user" not in session: return redirect("/")
    global users; users=load_users(); msg=""
    if request.method=="POST":
        old=request.form.get("old",""); new=request.form.get("new","")
        u=session["user"]
        if users[u]["password"]==old:
            users[u]["password"]=new; save_users(users); msg="Password an canza! ✔️"
        else: msg="Tsohon password ba daidai ba!"
    return base_style()+f"""<body><div class="header"><a href="/home">Home</a><h3 style="color:var(--green);margin:0">⚙️ SETTINGS</h3></div>
<div style="max-width:500px;margin:auto;padding:15px">
<div class="card2"><h3>🌗 Canza Haske</h3><p>Idan kana son Light ko Dark mode</p><button class="btn" onclick="toggleTheme()">Canza zuwa Light/Dark</button></div>
<div class="card2"><h3>🔑 Canza Password</h3><p style="color:#ff5555">{msg}</p>
<form method="post"><input name="old" type="password" placeholder="Tsohon Password" required><input name="new" type="password" placeholder="Sabon Password" required><button class="btn">Canza Password</button></form></div>
<div class="card2"><h3>ℹ️ Bayani akan ADMIN</h3>
<p style="line-height:1.6;font-size:13px;white-space:pre-line">
Kai admin ne saboda ka shiga da:
Username: admin
Password: 1234

Abubuwan da admin kadai zai iya yi:
1. Shiga ADMIN PANEL - yana sama a Home idan ka shiga da admin
2. Gani duk passwords na mutane da suka yi register
3. Gani emails dinsu
4. Wannan file yana ajiye a Render a matsayin users_db.json

Idan wani ya manta password, kai zaka shiga Admin Panel ka fada masa.

Kada ka bayar da password din admin ga kowa!

Idan kana son canza password din admin:
- Shiga Settings nan
- Saka Tsohon: 1234
- Saka Sabon da kake so
- Danna Canza
</p></div>
<a href="/home" style="display:block;text-align:center;padding:10px;border:1px solid var(--green);border-radius:8px;margin-top:10px">Koma Home</a>
</div></body>"""

@app.route("/admin")
def admin_panel():
    if "user" not in session or session["user"]!="admin": return redirect("/")
    users=load_users(); rows=""
    for u,info in users.items():
        rows+=f"<tr><td style='border:1px solid #444;padding:8px'>{u}</td><td style='border:1px solid #444;padding:8px'>{info.get('password')}</td><td style='border:1px solid #444;padding:8px'>{info.get('email','')}</td></tr>"
    return base_style()+f"""<body><div class="header"><a href="/home">Home</a> | <a href="/settings">Settings</a><h3 style="color:#ffcc00">ADMIN PANEL - SIRRI</h3></div>
<div style="max-width:700px;margin:auto;padding:15px"><div class="card2"><h3 style="color:#ffcc00">Duk Users da Passwords</h3>
<table style="width:100%;border-collapse:collapse"><tr style="background:var(--head)"><th style="border:1px solid #444;padding:8px">User</th><th style="border:1px solid #444;padding:8px">Password</th><th style="border:1px solid #444;padding:8px">Email</th></tr>{rows}</table>
<p style="font-size:11px;margin-top:10px">Wannan shine wurin da ake adana password a Render (users_db.json). Kai kadai zaka gani.</p></div></div></body>"""

@app.route("/logout")
def logout():
    session.clear(); return redirect("/")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))