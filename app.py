from flask import Flask, render_template_string, request, redirect, session
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "ethical-hacking-2026-umar-final"
app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = 0

users = {"admin":"1234"}
LOG_FILE = "users_log.txt"

def save_user(u,p):
    try:
        open(LOG_FILE,"a",encoding="utf-8").write(f"{datetime.now()} - {u}:{p}\n")
    except: pass

if not os.path.exists(LOG_FILE): open(LOG_FILE,"w").close()

# DARUSSA 100 - FULL DETAIL
LESSONS = {
    1: {"title":"1. Phishing", "menene": """Phishing wata dabara ce ta yaudara inda barawo ya yi kamar amintacce (kamar banki, Facebook, MTN) don sace bayanan ka.""", "yadda": """1. Ya turo maka email/SMS da link na karya
2. Link yayi kama da na gaskiya (faceb00k.com)
3. Idan ka shiga ka saka password, ya dauke shi
4. Ya shiga account dinka""", "waye": """Yan damfara na yanar gizo (Yahoo boys), hackers matasa.""", "matsala": """Satar kudin banki, satar Facebook/WhatsApp, blackmail.""", "kare": """Kada ka danna link da baka sani ba
Duba adireshi da kyau
Kunna 2FA
Banki BAYA tambayar OTP a waya"""},
    2: {"title":"2. Strong Password", "menene": """Password mai karfi shi ne makullin gidan ka. Idan mai rauni ne, hacker zai bude shi cikin dakika 2.""", "yadda": """Brute Force - software da ke gwada kalmomi miliyan a dakika.
Dictionary Attack - yana gwada sunaye da aka saba.""", "waye": """Kowa zai iya karya shi - daga yaro mai laptop har zuwa babban hacker.""", "matsala": """Satar duk account dinka da password daya.""", "kare": """Yi amfani da 12 harafi: Zaria@2026!Ng
Kada ka maimaita password
Yi amfani da Password Manager"""},
    3: {"title":"3. Malware", "menene": """Malware guba ce da ke lalata waya/computer. Virus ne da ke shigowa ta app na karya.""", "yadda": """Yana shigowa ta app da ka sauke daga wajen Play Store, ko file da ka bude.
Sai ya boye a waya yana satar bayani.""", "waye": """Hackers da ke kirkirar virus don kudi.""", "matsala": """Wayarka zata yi kasa, sata hotuna, lalata file, satar kudi.""", "kare": """Kada ka sauke daga wajen Play Store
Saka Antivirus
Kada ka bude file da baka sani ba"""},
}

# Sauran 4-100 - zan kara muku a auto, amma wannan tsarin zai yi aiki
# Don cikakken 100, kwafa wannan tsarin har 100
for i in range(4,101):
    LESSONS[i] = {
        "title": f"{i}. Darasi {i}",
        "menene": f"Darasi na {i} game da Ethical Hacking - wani muhimmin bangare ne na cyber security da ya kamata ka sani.",
        "yadda": f"1. Hacker ya fara bincike\n2. Ya shirya kayan aiki na darasi {i}\n3. Ya sanya tarko\n4. Idan ka fada, sai ya dauki bayani",
        "waye": f"Hackers da yan damfara ne ke yin wannan.",
        "matsala": f"Hadari ya hada da satar kudi da bayani.",
        "kare": f"Kare kai: Sabunta waya, Strong Password + 2FA, Kada ka danna link, Antivirus + VPN"
    }

@app.route("/", methods=["GET","POST"])
def login():
    msg=""
    if request.method=="POST":
        u=request.form["username"]; p=request.form["password"]
        if u in users and users[u]==p:
            session["user"]=u
            session.permanent=False
            return redirect("/home")
        msg="Suna ko Password ba daidai ba!"
    return render_template_string("""
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{background:#050a14;color:white;font-family:Arial;margin:0}.box{max-width:500px;margin:20px auto;background:#101a2e;padding:25px;border-radius:15px;border:1px solid #00ff88} input{width:95%;padding:13px;margin:8px 0;border-radius:8px;border:none} button{width:98%;padding:13px;background:#00ff88;color:black;border:none;border-radius:8px;font-weight:bold} a{color:#00ff88}.header{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88}</style>
<div class="header"><h1 style="color:#00ff88">🎓 ETHICAL HACKING</h1></div>
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
<style>body{background:#050a14;color:white;font-family:Arial;margin:0}.box{max-width:500px;margin:20px auto;background:#101a2e;padding:25px;border-radius:15px;border:1px solid #00ff88} input{width:95%;padding:13px;margin:8px 0;border-radius:8px;border:none} button{width:98%;padding:13px;background:#00ff88;color:black;border:none;border-radius:8px;font-weight:bold} a{color:#00ff88}.header{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88}</style>
<div class="header"><h1 style="color:#00ff88">🎓 ETHICAL HACKING</h1></div>
<div class="box"><h2>Register</h2><p style="color:orange">{{msg}}</p><form method="post"><input name="username" placeholder="Username" required><input type="password" name="password" placeholder="Password" required><button>REGISTER</button></form><p>Kana da account? <a href="/">Login</a></p></div>
""", msg=msg)

@app.route("/home")
def home():
    if "user" not in session: return redirect("/")
    html = """
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{background:#050a14;color:white;font-family:Arial;margin:0}.header{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88;position:sticky;top:0}.card{background:#101a2e;margin:12px;padding:18px;border-radius:12px;border-left:4px solid #00ff88} button{padding:10px 15px;background:#00ff88;border:none;border-radius:8px;font-weight:bold}</style>
<div class="header"><a href="/logout" style="float:right;color:#ff4444">Logout</a><h1 style="color:#00ff88">🎓 DARUSSA 100</h1><p>Barka da zuwa """ + session["user"] + """ </p></div><div style="max-width:700px;margin:auto">"""
    for i in range(1,101):
        t = LESSONS[i]["title"]
        html += f'<div class="card"><h3>{t}</h3><a href="/lesson/{i}"><button>Karanta Cikakke →</button></a></div>'
    html += "</div>"
    return render_template_string(html)

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
.header{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88;position:sticky;top:0;z-index:10}
.card{background:#101a2e;margin:15px;padding:22px;border-radius:15px;border-left:6px solid #00ff88;box-shadow:0 4px 15px rgba(0,255,136,0.1)}
.card.red{border-left-color:#ff4444}.card.blue{border-left-color:#4488ff}
.card.yellow{border-left-color:#ffcc00}.card.green{border-left-color:#00ff88}
h2{color:#00ff88;font-size:18px} p{line-height:1.8;font-size:16px}
.btn{display:inline-block;padding:13px 22px;background:#00ff88;color:black;border-radius:10px;text-decoration:none;font-weight:bold;margin:5px}
.btn2{background:#101a2e;color:#00ff88;border:1px solid #00ff88}
.progress{height:8px;background:#222;border-radius:10px;margin:10px 0}
.progress-bar{height:100%;background:#00ff88;border-radius:10px;width:{{ (id/100)*100 }}%}
</style>
<div class="header">
<a href="/home" style="float:left;color:#00ff88">← Home</a>
<a href="/logout" style="float:right;color:#ff4444">Logout</a>
<h1 style="color:#00ff88;margin:0;font-size:18px">🎓 {{l.title}}</h1>
<div class="progress"><div class="progress-bar"></div></div>
<small>Darasi {{id}} / 100</small>
</div>
<div style="max-width:750px;margin:auto;padding-bottom:40px">
<div class="card blue"><h2>📖 1. Menene Wannan Abun?</h2><p>{{l.menene}}</p></div>
<div class="card yellow"><h2>⚙️ 2. Yadda Ake Yinshi</h2><p style="white-space:pre-line">{{l.yadda}}</p></div>
<div class="card"><h2>👤 3. Waye Ke Yi?</h2><p>{{l.waye}}</p></div>
<div class="card red"><h2>☠️ 4. Matsala / Hadari</h2><p>{{l.matsala}}</p></div>
<div class="card green"><h2>🛡️ 5. Yadda Za Ka Kare Kai</h2><p style="white-space:pre-line;font-weight:bold">{{l.kare}}</p></div>
<div style="text-align:center;margin:25px">
<a href="/lesson/{{pid}}" class="btn btn2">← Baya</a>
<a href="/lesson/{{nid}}" class="btn">Gaba →</a><br><br>
<a href="/home" class="btn btn2" style="width:85%">🏠 Komawa Jerin Darussa</a>
</div></div>
""", l=l, id=id, nid=nid, pid=pid)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))