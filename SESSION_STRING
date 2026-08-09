from telethon.sync import TelegramClient

api_id = int(input("API ID: "))
api_hash = input("API HASH: ")

with TelegramClient("session", api_id, api_hash) as client:
    print("\nSESSION STRING:")
    print(client.session.save())
