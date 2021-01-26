from config import username, api_id, api_hash

from telethon import TelegramClient


def print_to_telegram(msg):
    client = TelegramClient(username, api_id, api_hash)

    async def main():
        me = await client.get_me()
        await client.send_message('me', msg)

    with client:
        client.loop.run_until_complete(main())

