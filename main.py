import requests
import time
import random
import threading
import json

with open("config.json", "r") as f:
    config = json.load(f)

channel_id = config["channel_id"]
message = config["message"]
delay = config["delay"]
threads = config.get("threads", len(tokens))

with open("tokens.txt", "r") as f:
    tokens = [token.strip() for token in f.readlines()]

def send_message(token):
    while True:
        try:
            headers = {
                "Authorization": token,
                "Content-Type": "application/json"
            }
            data = {
                "content": message
            }
            url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

            response = requests.post(url, headers=headers, json=data)

            if response.status_code != 200:
                print(f"Error sending message: {response.status_code} {response.reason}")
            else:
                print(f"Message sent: {message}")

        except Exception as e:
            print(f"Error sending message: {e}")

        time.sleep(delay)

threads = []
for i in range(threads):
    token = tokens[i % len(tokens)]
    thread = threading.Thread(target=send_message, args=(token,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
