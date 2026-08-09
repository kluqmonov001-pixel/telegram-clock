from telethon import TelegramClient, functions
from telethon.sessions import StringSession
from datetime import datetime
from zoneinfo import ZoneInfo
import os

api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
session = os.environ['SESSION_STRING']

client = TelegramClient(
    StringSession(session),
    api_id,
    api_hash
)

async def main():
    await client.connect()

    current_time = datetime.now(ZoneInfo("Asia/Tashkent")).strftime("%H:%M")

    await client(functions.account.UpdateProfileRequest(
        about=f"🕒 {current_time}"
    ))

    await client.disconnect()

with client:
    client.loop.run_until_complete(main())
