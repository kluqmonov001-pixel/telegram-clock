from telethon import TelegramClient, functions
from datetime import datetime
import os

api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
session = os.environ['SESSION_STRING']

client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start()
    current_time = datetime.utcnow().strftime('%H:%M UTC')
    await client(functions.account.UpdateProfileRequest(
        about=f'🕒 {current_time}'
    ))

with client:
    client.loop.run_until_complete(main())
