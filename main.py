import requests
import time
import random
import os

class Colors:
    red = "\x1b[1;31m"
    green = "\x1b[1;32m"
    white = "\x1b[1;37m"
    
valid = 0
invalid = 0

art = f"""
                   {Colors.white}/|_
                  /   |_
                 /     /
                /      >
               (      >
              /      /
             /     /
            /      /
         __/      \_____
        /{Colors.red}'{Colors.white}             |
         /     /-\     /
        /      /  \--/
       /     /
      /      /  {Colors.red}region call reaper by {Colors.white}speezy
     (      >
    /      >
   /     _|
  /  __/
 /_/
"""

def callreaper():
    global valid
    global invalid
    region = ["brazil", "hongkong", "inda", "japan", "rotterdam", "russia", "singapore", "southafrica", "sydney", "us-central", "us-east", "us-south", "us-west"]
    token = input(f"{Colors.white}" + "[" + f"{Colors.red}" + "ϟ" + f"{Colors.white}" + "]" + f"{Colors.red}" + " Token: " + f"{Colors.white}")
    r = requests.get("https://discord.com/api/v9/users/@me/library", headers={"authorization": token, "content-type": "application/json"})
    if r.status_code == 200:
        print(f"{Colors.white}" + "[" + f"{Colors.green}" + "+" + f"{Colors.white}" + "]" + f"{Colors.green}" + " Valid Token" + f"{Colors.white}")
    else:
        print(f"{Colors.white}" + "[" + f"{Colors.red}" + "!" + f"{Colors.white}" + "]" + f"{Colors.red}" + " Invalid Token" + f"{Colors.white}")
    groupid = input(f"{Colors.white}" + "[" + f"{Colors.red}" + "ϟ" + f"{Colors.white}" + "]" + f"{Colors.red}" + " Guild ID: " + f"{Colors.white}")
    while True:
        headers = {
            "authority": "discord.com",
            "method": "PATCH",
            "path": f"/api/v9/channels/{groupid}/call",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "fr-FR, fr;q=0.9",
            "authorization": token,
            "content-length": "21",
            "content-type": "application/json",
            "cookie": f"__dcfduid={os.urandom(34).hex()}; __sdcfduid={os.urandom(98).hex()}; __cf_bm={os.urandom(191).hex()}; locale=fr",
            "origin": "https://discord.com",
            "referer": f"https://discord.com/channels/@me/{groupid}",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "fr",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwMDg5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
        }
        r = requests.patch(f"https://discord.com/api/v9/channels/{groupid}/call", headers=headers, json={"region": random.choice(region)})
        if r.status_code == 204:
            valid += 1
            print(f"{Colors.white}" + "[" + f"{Colors.green}" + "+" + f"{Colors.white}" + "]" + f"{Colors.green}" + f" Changed Region {Colors.white}({Colors.green}{valid}{Colors.white})")
        else:
            invalid += 1
            print(f"{Colors.white}" + "[" + f"{Colors.red}" + "-" + f"{Colors.white}" + "]" + f"{Colors.red}" + f" Failed {r.json()} {Colors.white}({Colors.red}{invalid}{Colors.white})")

def main():
    print(art)
    time.sleep(0.5)
    callreaper()
    
if __name__ == "__main__":
    os.system("cls")
    os.system(f'mode con: cols=90 lines=30')
    os.system("title Discord Region Call Raper")
    main()