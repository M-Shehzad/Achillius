import requests #dependency
from datetime import datetime
import pytz

# url = "https://discord.com/api/webhooks/967857205477007400/UVZEW3zQKIePnbmkLE_EgCK4R6k3XkiVFoesxSZ_yi_JOZTB1uznTlA-Bp4V9FnqB4vl" #webhook url

# data = {"content": "Using webhook to automate the messages", 
#         "username": "pk", 
#         "embeds": []}

# embed = {"description": "Test run 2",
#          "title": "Hello world"}
         
# data["embeds"].append(embed)

# result = requests.post(url, json=data, headers={"Content-Type": "application/json"})

# try:
#     result.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     print(err)
# else:
#     print("Payload delivered successfully, code {}.".format(result.status_code))

class TacWebhook:
    def __init__(self) -> None:
        self.url = #webhook here
        self.username = "Recruitment Bot"
        self.title = "Application Form"
        self.color = 980461
        self.timestamp = str(datetime.now(pytz.timezone('Asia/Kolkata')))

    def addEmbeds(self, Name, Number, Email, Department, CV, LinkedIn, Message):
        self.data = {"content": "",
                "username": self.username,
                "embeds": [
                    {
                        "title": self.title,
                        "color": self.color,
                        "timestamp": self.timestamp,
                        "fields": [
                            {
                                "name": "Name",
                                "value": Name,
                                "inline": False
                            },
                            {
                                "name": "Number",
                                "value": Number,
                                "inline": False
                            },
                            {
                                "name": "Email",
                                "value": Email,
                                "inline": False
                            },
                            {
                                "name": "Interested department:",
                                "value": Department,
                                "inline": False
                            },
                            {
                                "name": "CV URL:",
                                "value": CV if CV else 'nil',
                                "inline": False
                            },
                            {
                                "name": "Linkedin URL:",
                                "value": LinkedIn if LinkedIn else 'nil',
                                "inline": False
                            },
                            {
                                "name": "Message",
                                "value": Message,
                                "inline": False
                            },
                        ]
                    }
                ]}

    def submitWebhook(self):
        return requests.post(self.url, json=self.data, headers={
                               "Content-Type": "application/json"})