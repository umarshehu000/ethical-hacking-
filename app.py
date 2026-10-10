from flask import Flask, render_template_string, request, redirect, session
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "ethical-hacking-2026-umar-final-v4"
app.config['SESSION_PERMANENT'] = False

users = {"admin":"1234"}
LOG_FILE = "users_log.txt"

def save_user(u,p):
    try:
        open(LOG_FILE,"a",encoding="utf-8").write(f"{datetime.now()} - {u}:{p}\n")
    except: pass

if not os.path.exists(LOG_FILE):
    open(LOG_FILE,"w").close()

LESSONS = {
    1: {"title":"Phishing", "icon":"🎣", "menene":"Phishing wata dabara ce ta yaudara inda barawo ya yi kamar amintacce (banki, Facebook) don sace bayanan ka.", "yadda":"1. Ya turo link na karya\n2. Link yayi kama da na gaskiya\n3. Idan ka saka password, ya dauke shi\n4. Ya shiga account dinka", "waye":"Yan damfara (Yahoo boys), hackers matasa.", "matsala":"Satar kudi, satar Facebook/WhatsApp, blackmail.", "kare":"Kada ka danna link da baka sani ba\nDuba adireshi\nKunna 2FA"},
    2: {"title":"Strong Password", "icon":"🔑", "menene":"Password mai karfi shi ne makullin gidan ka. Idan mai rauni ne, hacker zai bude shi cikin dakika 2.", "yadda":"Brute Force - software da ke gwada kalmomi miliyan.\nDictionary Attack - gwada sunaye da aka saba.", "waye":"Kowa zai iya karya shi.", "matsala":"Satar duk account dinka.", "kare":"Yi amfani da 12 harafi: Zaria@2026!Ng\nKada ka maimaita password"},
    3: {"title":"Malware", "icon":"🦠", "menene":"Malware guba ce da ke lalata waya/computer.", "yadda":"Yana shigowa ta app na karya ko file da ka sauke.", "waye":"Hackers da ke kirkirar virus.", "matsala":"Wayarka zata yi kasa, sata hotuna.", "kare":"Kada ka sauke daga wajen Play Store\nSaka Antivirus"},
}

# Auto 4-100
names = ["Ransomware","SQL Injection","XSS","DDoS","MITM","Keylogger","Brute Force","Spyware","Trojan","Rootkit","Zero-Day","Fake Apps","SIM Swap","WhatsApp Hack","Facebook Hack","Email Spoof","OTP Bypass","Session Hijack","Cookie Theft","Data Breach","Dark Web","Cryptojacking","Botnet","Adware","Pharming","Vishing","Smishing","Baiting","Pretexting","Password Spray","Credential Stuff","Dictionary Attack","Rainbow Table","WiFi Hack","Bluetooth Hack","QR Scam","USB Drop","Shoulder Surf","Sniffing","Port Scan","Vuln Scan","Reverse Eng","Forensics","Steganography","Cryptography","2FA","Biometrics","Firewall","Antivirus","VPN","Proxy","Tor","Secure Email","HTTPS","SSL","Backup","Patch","OSINT","Social Safety","Banking Safety","ATM Skim","Carding","Identity Theft","Cyberbullying","Kids Safety","Fake News","Deepfake","AI Scam","IoT Hack","CCTV Hack","Phone Security","Android Hack","App Permission","Cloud Sec","Google Dork","Metadata","Fileless","Insider Threat","Supply Chain","BEC","RAT","Kali Linux","Bug Bounty","Pen Test","Recovery","Hacked?","Career","Ethics"]

icons = ["💀","💉","👾","🌐","🕵️","⌨️","🔨","👁️","🐴","🌱","0️⃣","📱","📲","💬","📘","📧","🔢","🍪","🗃️","💾","🌑","⛏️","🤖","📢","🚜","📞","💬","🎣","🎭","💦","🧴","📚","🌈","📶","🔵","📡","🔳","🔌","👀","👃","🔍","🔎","⚙️","🔬","🖼️","🔐","👆","🧱","🛡️","🔒","🌐","🧅","✉️","🔒","📜","💾","🩹","🔍","🛡️","🏦","🏧","💳","🪪","😢","👶","📰","🎭","🤖","🏠","📹","📱","🤖","🔑","☁️","🔍","📄","👻","👤","📦","📧","🐀","🐧","🐛","🧪","🆘","💼","🎓"]

for idx, (nm, ic) in enumerate(zip(names, icons), start=4):
    if idx>100: break
    LESSONS[idx] = {
        "title": nm,
        "icon": ic,
        "menene": f"{nm} wani muhimmin bangare ne na cyber security. Barazana ce ko kariya da ya kamata ka sani.",
        "yadda": f"1. Hacker ya fara bincike\n2. Ya shirya kayan aiki na {nm}\n3. Ya sanya tarko\n4. Ya dauki bayanan ka",
        "waye": f"Hackers da yan damfara