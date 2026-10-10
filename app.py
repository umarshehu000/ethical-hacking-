LESSONS = {
 1: {
   "title":"1. Phishing",
   "menene":"Phishing wata dabara ce ta yaudara inda barawo ya yi kamar amintacce (kamar banki, Facebook) don sace bayanan ka. Yana aiko maka da sakon karya cewa 'Account dinka zai kulle'.",
   "yadda":"1. Ya turo maka email/SMS da link na karya\n2. Link din yayi kama da na gaskiya (faceb00k.com)\n3. Idan ka shiga ka saka password, nan take ya dauke shi\n4. Ya shiga account dinka",
   "waye":"Yan damfara na yanar gizo, hackers matasa, kungiyoyin sata a kasashen waje. Sun fi amfani da Gmail da WhatsApp.",
   "matsala":"☠️ Satar kudin banki, satar Facebook/WhatsApp, cin mutuncin ka, bashi da sunanka, blackmail da hotunanka.",
   "kare":"✅ Kada ka taba danna link daga mutumin da baka sani ba\n✅ Koyaushe duba adireshi: facebook.com ba faceb00k.com ba\n✅ Kunna 2FA a ko'ina\n✅ Banki BAYA tambayar OTP a waya"
 },
 2: {
   "title":"2. Strong Password",
   "menene":"Password mai karfi shi ne makullin gidan ka na yanar gizo. Idan mai rauni ne, hacker zai bude shi cikin dakika 2 da software.",
   "yadda":"Hacker yana amfani da 'Brute Force' - software da ke gwada kalmomi miliyan. Idan password dinka '12345' ne ko 'zaria', zai kama nan da nan.",
   "waye":"Kowa zai iya karya shi - daga yaro mai laptop har zuwa babban hacker. Akwai website da suke siyar da password da aka sace.",
   "matsala":"Satar duk account dinka da password daya. Idan Facebook da Banki iri daya ne, duk sun tafi.",
   "kare":"✅ Yi amfani da 12 harafi: Babba + karami + lamba + alama. Mis: Zaria@2026!Ng\n✅ Kada ka maimaita password\n✅ Yi amfani da Password Manager"
 }
 # Ka ci gaba da sauran 98 kamar wannan tsarin...
}

# --- SABON DESIGN NA LESSON PAGE ---
@app.route("/lesson/<int:id>")
def lesson(id):
    if "user" not in session: return redirect("/")
    l=LESSONS.get(id)
    if not l: return redirect("/home")
    nid = id+1 if id < len(LESSONS) else 1
    pid = id-1 if id > 1 else len(LESSONS)
    
    return render_template_string("""
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#050a14;color:#e0e0e0;font-family:Arial;margin:0}
.header{background:#001122;padding:15px;text-align:center;border-bottom:2px solid #00ff88;position:sticky;top:0}
.card{background:#101a2e;margin:15px;padding:20px;border-radius:15px;border-left:5px solid #00ff88;box-shadow:0 4px 15px rgba(0,255,136,0.1)}
.card.red{border-left-color:#ff4444}
.card.blue{border-left-color:#4488ff}
.card.yellow{border-left-color:#ffcc00}
.card.green{border-left-color:#00ff88}
h2{color:#00ff88;margin-top:5px}
.btn{display:inline-block;padding:12px 20px;background:#00ff88;color:black;border-radius:10px;text-decoration:none;font-weight:bold;margin:5px}
.btn2{background:#101a2e;color:#00ff88;border:1px solid #00ff88}
.progress{height:8px;background:#222;border-radius:10px;margin:10px 0}
.progress-bar{height:100%;background:#00ff88;border-radius:10px;width:{{ (id/100)*100 }}%}
</style>
<div class="header">
<a href="/home" style="float:left;color:#00ff88">← Home</a>
<a href="/logout" style="float:right;color:#ff4444">Logout</a>
<h1 style="color:#00ff88;margin:0">🎓 {{l.title}}</h1>
<div class="progress"><div class="progress-bar"></div></div>
<small>Darasi {{id}} daga 100</small>
</div>

<div style="max-width:700px;margin:auto;padding-bottom:30px">

<div class="card blue">
<h2>📖 1. Menene Wannan Abun?</h2>
<p style="line-height:1.7;font-size:16px">{{l.menene}}</p>
</div>

<div class="card yellow">
<h2>⚙️ 2. Yadda Ake Yinshi</h2>
<p style="line-height:1.7;white-space:pre-line;font-size:16px">{{l.yadda}}</p>
</div>

<div class="card">
<h2>👤 3. Waye Ke Yi?</h2>
<p style="line-height:1.7;font-size:16px">{{l.waye}}</p>
</div>

<div class="card red">
<h2>☠️ 4. Matsala / Hadari</h2>
<p style="line-height:1.7;font-size:16px">{{l.matsala}}</p>
</div>

<div class="card green">
<h2>🛡️ 5. Yadda Za Ka Kare Kai</h2>
<p style="line-height:1.7;white-space:pre-line;font-size:16px;font-weight:bold">{{l.kare}}</p>
</div>

<div style="text-align:center;margin:25px">
<a href="/lesson/{{pid}}" class="btn btn2">← Baya</a>
<a href="/lesson/{{nid}}" class="btn">Gaba →</a>
<br><br>
<a href="/home" class="btn btn2" style="width:80%">🏠 Komawa Jerin Darussa</a>
</div>

</div>
""", l=l, id=id, nid=nid, pid=pid)