import requests #dependency

url = "https://discord.com/api/webhooks/967857205477007400/UVZEW3zQKIePnbmkLE_EgCK4R6k3XkiVFoesxSZ_yi_JOZTB1uznTlA-Bp4V9FnqB4vl" #webhook url

data = {"content": "Using webhook to automate the messages", 
        "username": "pk", 
        "embeds": []}

embed = {"description": "Test run 2",
         "title": "Hello world"}
         
data["embeds"].append(embed)

result = requests.post(url, json=data, headers={"Content-Type": "application/json"})

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))

