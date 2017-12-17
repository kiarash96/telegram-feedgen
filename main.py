import re

import config

from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest


def add_channel(client, username):
    channel = client.get_entity(username)
    try:
        client.invoke(JoinChannelRequest(channel))
    except ValueError:
        print("Wrong username {}!".format(username))


def handle_update(update):
    pass


def main():
    client = TelegramClient(config.session_name, config.api_id, config.api_hash, update_workers=1)
    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(config.phone)
        client.sign_in(phone=config.phone, code=input("Enter code: "))

    client.add_update_handler(handle_update)

    while True:
        command = input(">> ")
        if command == "exit":
            break
        else:
            result = re.match(r"^join\s+@?(\w+)", command)
            if result:
                username = result.group(1)
                add_channel(client, username)

    client.disconnect()


if __name__ == "__main__":
    main()
