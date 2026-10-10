from flask import Flask, render_template_string, request, redirect, session
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "ethical-hacking-2026-umar-final-v3"
app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = 0

users = {"admin":"1234"}
LOG_FILE = "users_log.txt"

def save_user(u,p):
    try:
        open(LOG_FILE,"a",encoding="utf-8").write(f"{datetime.now()} - {u}:{p}\n")
    except: pass

if not os.path.exists(LOG_FILE):
    open(LOG_FILE,"w").close()

# === DARUSSA 100 - FULL DETAIL ===
LESSONS = {
    1: {"title":"1. Phishing", "menene":"Phishing wata dabara ce ta yaudara inda barawo ya yi kamar amintacce (kamar banki, Facebook, MTN) don sace bayanan ka. Yana aiko maka da sakon karya cewa 'Account dinka zai kulle, danna nan'.", "yadda":"1. Ya turo maka email/SMS da link na karya\n2. Link yayi kama da na gaskiya (faceb00k.com)\n3. Idan ka shiga ka saka password, nan take ya dauke shi\n4. Ya shiga account dinka ya sace komai", "waye":"Yan damfara na yanar gizo (Yahoo boys), hackers matasa, kungiyoyin sata a kasashen waje. Sun fi amfani da Gmail da WhatsApp.", "matsala":"☠️ Satar kudin banki, satar Facebook/WhatsApp, cin mutuncin ka, bashi da sunanka, blackmail da hotunanka.", "kare":"✅ Kada ka taba danna link daga mutumin da baka sani ba\n✅ Koyaushe duba adireshi: facebook.com ba faceb00k.com ba\n✅ Kunna 2FA a ko'ina\n✅ Banki BAYA tambayar OTP a waya"},
    2: {"title":"2. Strong Password", "menene":"Password mai karfi shi ne makullin gidan ka na yanar gizo. Idan mai rauni ne kamar '12345', hacker zai bude shi cikin dakika 2 da software.", "yadda":"Hacker yana amfani da 'Brute Force' - software da ke gwada kalmomi miliyan a dakika. Dictionary Attack yana gwada sunaye da aka saba amfani da su.", "waye":"Kowa zai iya karya shi - daga yaro mai laptop har zuwa babban hacker. Akwai website a Dark Web da suke siyar da password.", "matsala":"Satar duk account dinka da password daya. Idan Facebook da Banki iri daya ne, duk sun tafi.", "kare":"✅ Yi amfani da 12 harafi: Babba+karami+lamba+alama. Mis: Zaria@2026!Ng\n✅ Kada ka maimaita password\n✅ Yi amfani da Password Manager"},
    3: {"title":"3. Malware", "menene":"Malware guba ce da ke lalata waya/computer. Virus ne da ke shigowa ta app na karya ko file da ka sauke.", "yadda":"Yana shigowa ta app da ka sauke daga wajen Play Store, ko file da ka bude. Sai ya boye a waya yana satar bayani a bayan fage.", "waye":"Hackers da ke kirkirar virus don kudi, ko don leken asiri.", "matsala":"Wayarka zata yi kasa, sata hotuna, lalata file, satar kudi da password.", "kare":"✅ Kada ka sauke app daga wajen Play Store\n✅ Saka Antivirus mai kyau\n✅ Kada ka bude file da baka sani ba"},
}

# Sauran darussa 4-100 - auto generated
extra = ["Ransomware","SQL Injection","XSS","DDoS","MITM","Keylogger","Brute Force","Spyware","Trojan","Rootkit","Zero-Day","Fake Apps","SIM Swapping","WhatsApp Hack","Facebook Hack","Email Spoofing","OTP Bypass","Session Hijacking","Cookie Theft","Data Breach","Dark Web","Cryptojacking","Botnet","Adware","Pharming","Vishing","Smishing","Baiting","Pretexting","Password Spraying","Credential Stuffing","Dictionary Attack","Rainbow Table","WiFi Hacking","Bluetooth Hacking","NFC Hacking","QR Code Scam","USB Drop","Shoulder Surfing","Eavesdropping","Port Scanning","Vuln Scanning","Reverse Engineering","Forensics","Steganography","Cryptography","2FA","Biometrics","Firewall","Antivirus","VPN","Proxy","Tor","Secure Email","HTTPS","SSL","Backup","Patch Management","OSINT","Social Media Safety","Banking Safety","ATM Skimming","Carding","Identity Theft","Cyberbullying","Kids Safety","Fake News","Deepfake","AI Scam","IoT Hacking","CCTV Hacking","Smartphone Security","Android Hacking","App Permission","Cloud Security","Google Dorking","Metadata Leak","Fileless Malware","Insider Threat","Supply Chain Attack","BEC","RAT