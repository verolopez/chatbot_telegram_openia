import requests
import time
from dotenv import env_values
config = env_values(".env")

def get_updates(token, offset=None):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    params = {"offset": offset} if offset else {}
    response = requests.get(url,params =params)
    return response.json()

def print_new_messages(token):
    offset = None
    while True:
        updates = get_updates(token,offset)
        if "result" in updates:
            for update in updates["result"]:
                message = update["result"]
                id = message["from"]["id"]
                username = message['from']["first_name"]
                text = message.get("text")
                print(f"Username: {username}({id})")
                print(f"Message: {text}")
                offset = update["update_id"]+1 

        time.sleep(1)
TOKEN = config["TELEGRAM_TOKEN"]
print_new_messages(TOKEN)