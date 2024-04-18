from requests import post
from time import time, sleep
from uuid import uuid4


def req(name, dude):
    headers = {
        'Host': 'ngl.link',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not- A.Brand";v="24"',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://ngl.link',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://ngl.link/{name}',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data = {
        'username': f'{name}',
        'question': f'{dude}',
        'deviceId': str(uuid4()),
        'gameSlug': '',
        'referrer': ''
    }
    return post(
        'https://ngl.link/api/submit',
        headers=headers,
        data=data
    )

def tq(n, user, msg):
    i = 0
    while i < n:
        try:
            r = req(user, msg[i % len(msg)])
            if r.ok:
                print(f'[{str(int(time()))[-4:]}] Message sent!')
                i += 1
            else:
                print(f'[{str(int(time()))[-4:]}] Error...')
                sleep(5)
        except: 
            print(f'[{str(int(time()))[-4:]}] Error...')
            sleep(5)
        sleep(1)
    return

user = input('Victim username > ') 
msg = input('Message > ').split(' ')
for i in range(3):
    try:
        amount = input('Amount > ')
        amount = int(amount)
    except:
        print(f'{amount} is not a valid integer. Try again. ({3-i} attempts left)')
    finally:
        break
else:
    print('Argument error. Press enter to exit.')
    input()
    quit()

print('\n\n\nStarting...\n')

tq(amount, user, msg)

print('Process finished, press enter to exit.')
input()
  