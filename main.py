import requests
import time
from itertools import cycle

def send_message(webhook_url, message, avatar_url=None, username=None, proxy=None):
    payload = {'content': message}
    if avatar_url:
        payload['avatar_url'] = avatar_url
    if username:
        payload['username'] = username

    try:
        response = requests.post(webhook_url, json=payload, proxies=proxy)
        if response.status_code == 204:
            print("Message sent successfully to", webhook_url)
        else:
            print("Failed to send message to", webhook_url, "- Status code:", response.status_code)
    except Exception as e:
        print("An error occurred while sending message to", webhook_url, ":", str(e))

def main():
    try:
        with open('webhooks.txt', 'r') as file:
            webhook_urls = file.read().splitlines()
    except FileNotFoundError:
        print("webhooks.txt not found.")
        return

    try:
        with open('proxies.txt', 'r') as file:
            proxies_list = file.read().splitlines()
    except FileNotFoundError:
        print("proxies.txt not found.")
        return

    send_from_file = input("Do you want to send the text from message.txt? (y/n): ").strip().lower()
    if send_from_file == 'y':
        try:
            with open('message.txt', 'r') as file:
                message = file.read()
        except FileNotFoundError:
            print("msg.txt not found.")
            return
    else:
        message = input("Enter the message you want to send: ")

    custom_avatar_url = "image url"
    custom_username = "name"

    proxies_cycle = cycle(proxies_list)

    for webhook_url in webhook_urls:
        proxy = {'http': next(proxies_cycle)}
        send_message(webhook_url, message, custom_avatar_url, custom_username, proxy)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
