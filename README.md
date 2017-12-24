# Telegram Rss Generator

This simple tools allows you to export posts from Telegram channels to rss format. It may be used in conjunction with a simple http server to allow for subscribing to the feeds.

## Setup and usage
Currently Telegram bots API does not allow bots to join channels, therefore you need a valid phone number with an associated Telegram account in order to use it with this script.
* First follow the steps described on https://core.telegram.org/api/obtaining_api_id to obtain an api_id and api_hash. Put these values and also your phone number into the `config.py` file.
* Run the interactive session using `TelegramRss` command
