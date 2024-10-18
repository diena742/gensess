import json
from pyrogram import Client as PyroClient
from telethon import TelegramClient as TeleClient
from telethon.sessions import StringSession
import os

# Membuat folder 'sessi' jika belum ada
if not os.path.exists("sessi"):
    os.makedirs("sessi")

# Membaca konfigurasi dari file session.json
def load_config():
    with open("session.json", "r") as file:
        config = json.load(file)
    return config

def save_session_to_file(session_string, filename):
    with open(f"sessi/{filename}.session", "w") as file:
        file.write(session_string)
    print(f"Session string saved to 'sessi/{filename}.session'")

def generate_pyrogram_session(is_bot=False):
    config = load_config()
    api_id = config['api_id']
    api_hash = config['api_hash']
    
    if is_bot:
        bot_token = input("Enter your bot token: ")
        with PyroClient("pyrogram_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token) as app:
            session_string = app.export_session_string()
            print("Pyrogram BOT String Session generated.")
            filename = input("Enter a filename to save the session: ")
            save_session_to_file(session_string, filename)
    else:
        with PyroClient("pyrogram_user", api_id=api_id, api_hash=api_hash) as app:
            session_string = app.export_session_string()
            print("Pyrogram USER String Session generated.")
            filename = input("Enter a filename to save the session: ")
            save_session_to_file(session_string, filename)

def generate_telethon_session(is_bot=False):
    config = load_config()
    api_id = config['api_id']
    api_hash = config['api_hash']
    
    if is_bot:
        bot_token = input("Enter your bot token: ")
        client = TeleClient(StringSession(), api_id, api_hash)
        client.start(bot_token=bot_token)
        session_string = client.session.save()
        print("Telethon BOT String Session generated.")
        filename = input("Enter a filename to save the session: ")
        save_session_to_file(session_string, filename)
    else:
        client = TeleClient(StringSession(), api_id, api_hash)
        client.start()
        session_string = client.session.save()
        print("Telethon USER String Session generated.")
        filename = input("Enter a filename to save the session: ")
        save_session_to_file(session_string, filename)

def main():
    print("Select the type of session you want to generate:")
    print("1. Pyrogram (USER)")
    print("2. Telethon (USER)")
    print("3. Pyrogram (BOT)")
    print("4. Telethon (BOT)")
    
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        generate_pyrogram_session(is_bot=False)
    elif choice == 2:
        generate_telethon_session(is_bot=False)
    elif choice == 3:
        generate_pyrogram_session(is_bot=True)
    elif choice == 4:
        generate_telethon_session(is_bot=True)
    else:
        print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
    