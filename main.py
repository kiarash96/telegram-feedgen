#!/usr/bin/env python3

import re

from telethon import TelegramClient
import telethon.tl.functions as functions
import telethon.tl.types as types

from feedgen.feed import FeedGenerator

import config


feeds = {}


def add_channel(client, username):
    result = client.invoke(functions.contacts.ResolveUsernameRequest(username))
    if not isinstance(result.peer, types.PeerChannel):
        print("Wrong username " + username)
        return

    channel = result.chats[0]

    if channel.id in feeds:
        print("Already joined channel " + username)
        return

    full_channel = client.invoke(functions.channels.GetFullChannelRequest(channel)).full_chat

    fg = FeedGenerator()
    fg.title(channel.title)
    fg.link(href='https://t.me/' + username, rel='via')
    fg.description(full_channel.about)
    feeds[channel.id] = fg

    client.invoke(functions.channels.JoinChannelRequest(channel))


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
