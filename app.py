from flask import Flask, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
app = Flask(__name__)
app.secret_key = 'umar_ethical_2026_secret'
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, contact TEXT UNIQUE, password TEXT)')
    conn.commit()
    conn.close()
init_db()
LESSONS = []
topics = ["Ethical Hacking","Phishing","Password Security","Social Engineering","Malware","WiFi Security","Kali Linux","Footprinting","SQL Injection","XSS","Nmap","Cryptography","VPN","Firewall","Cyber Law NG","Dark Web","Ransomware","Spyware","DoS Attack","MITM"]
for i in range(1, 101):
    t = topics[(i-1) % len(topics)]
    LESSONS.append({"id": i, "title": f"Lesson {i}: {t}", "p1": f"SHAPI 1 - {t}: Gabatarwa akan {t}. Wannan darasi yana koya maka asalin {t} da yadda yake aiki.", "p2": f"SHAPI 2 - Kariya daga {t}: 1) Kada ka danna link da baka sani ba. 2) Yi amfani da strong password. 3) Sabunta phone/laptop. Offline lesson."})
def page(html):
    return f"<html><head><meta name='viewport' content='width=device-width, initial-scale=1.0'><style>body{{background:#050508;color:#fff;font-family:Arial;padding:20px;max-width:900px;margin:auto}}.nav{{display:flex;justify-content:space-between;background:#111;padding:15px;border-radius:15px;border:1px solid #333}}.card{{background:#15151f;padding:20px;border-radius:15px;margin-top:15px;border:1px solid #222}}input{{width:100%;padding:14px;margin:8px 0;border-radius:10px;border:1px solid #333;background:#0a0a0f;color:#fff;box-sizing:border-box}}button{{width:100%;padding:14px;background:#6c5cff;color:#fff;border:none;border-radius:10px;font-weight:bold}}a{{color:#6c5cff;text-decoration:none}}.btn{{padding:8px 18px;background:#6c5cff;color:#fff;border-radius:20px}}.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}}</style></head><body>{html}</body></html>"
@app.route('/')
def home():
    if 'user' not in session: return redirect('/login')
    cards = "".join([f"<div class='card'><b>{l['title']}</b><br><br><a class='btn' href='/lesson/{l['id']}/1'>Bude →</a></div>" for l in LESSONS])
    return page(f"<div class='nav'><div>👨‍💻 ETHICALHACKING.NG<br><small style='color:#888'>Barka {session['user']['name']}</small></div><a href='/logout' style='color:#ff5c9c'>Logout</a></div><h2>📚 Darussa 100 - Offline</h2><p style='color:#888'>Kowanne darasi shafi 2</p><div class='grid'>{cards}</div>")
@app.route('/register', methods=['GET','POST'])
def register():
    msg=""
    if request.method == 'POST':
        name=request.form['name']; contact=request.form['contact'].strip(); pwd=generate_password_hash(request.form['password'])
        try:
            conn=sqlite3.connect('database.db'); c=conn.cursor(); c.execute("INSERT INTO users (name,contact,password) VALUES (?,?,?)",(name,contact,pwd)); conn.commit(); conn.close(); return redirect('/login')
        except: msg="<p style='color:#ff5c9c'>Email/Phone an riga an yi amfani dashi!</p>"
    return page(f"<div class='card' style='max-width:400px;margin:50px auto'><h2>📝 Register</h2>{msg}<form method='POST'><input name='name' placeholder='Sunanka' required><input name='contact' placeholder='Email ko Phone' required><input name='password' type='password' placeholder='Password' required><button>Register</button></form><p><a href='/login'>Login</a></p></div>")
@app.route('/login', methods=['GET','POST'])
def login():
    msg=""
    if request.method == 'POST':
        contact=request.form['contact']; pwd=request.form['password']
        conn=sqlite3.connect('database.db'); c=conn.cursor(); c.execute("SELECT * FROM users WHERE contact=?",(contact,)); u=c.fetchone(); conn.close()
        if u and check_password_hash(u[3], pwd): session['user']={'name':u[1],'contact':u[2]}; return redirect('/')
        else: msg="<p style='color:#ff5c9c'>Ba daidai bane!</p>"
    return page(f"<div class='card' style='max-width:400px;margin:50px auto'><h2>🔐 Login</h2>{msg}<form method='POST'><input name='contact' placeholder='Email ko Phone' required><input name='password' type='password' placeholder='Password' required><button>Shiga</button></form><p><a href='/forgot'>Manta password?</a> | <a href='/register'>Register</a></p></div>")
@app.route('/forgot', methods=['GET','POST'])
def forgot():
    msg=""
    if request.method == 'POST':
        contact=request.form['contact']; new=generate_password_hash(request.form['new_password'])
        conn=sqlite3.connect('database.db'); c=conn.cursor(); c.execute("UPDATE users SET password=? WHERE contact=?",(new,contact))
        if c.rowcount==0: msg="<p style='color:#ff5c9c'>Ba a samu ba!</p>"
        else: conn.commit(); conn.close(); return redirect('/login')
        conn.close()
    return page(f"<div class='card' style='max-width:400px;margin:50px auto'><h2>🔑 Manta Password?</h2>{msg}<form method='POST'><input name='contact' placeholder='Email ko Phone' required><input name='new_password' type='password' placeholder='Sabon Password' required><button>Sake Saita</button></form><p><a href='/login'>Login</a></p></div>")
@app.route('/lesson/<int:lid>/<int:pg>')
def lesson(lid, pg):
    if 'user' not in session: return redirect('/login')
    l = next((x for x in LESSONS if x['id']==lid), None)
    txt = l['p1'] if pg==1 else l['p2']
    nxt = f"<a class='btn' href='/lesson/{lid}/2'>Shafi 2 →</a>" if pg==1 else f"<a class='btn' href='/'>Gida</a>"
    return page(f"<div class='nav'><a href='/'>← Gida</a><div>{l['title']}</div><div>Shafi {pg}/2</div></div><div class='card'><h2>{l['title']} - Shafi {pg}</h2><p style='line-height:1.8;color:#ccc'>{txt}</p><div style='margin-top:20px'>{nxt}</div></div>")
@app.route('/logout')
def logout():
    session.clear(); return redirect('/login')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
