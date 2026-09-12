"""
AIKReporter - Telegram Client
Connect to Telegram and manage session
"""

from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError


class TGClient:
    """Telegram connection manager"""

    def __init__(self, api_id, api_hash, phone, session_name='aik_session'):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone = phone
        self.session_name = session_name
        self.client = TelegramClient(session_name, api_id, api_hash)

    def connect(self):
        """Connect and login"""
        self.client.connect()

        if not self.client.is_user_authorized():
            print("[*] Sending verification code...")
            self.client.send_code_request(self.phone)

            code = input("[?] Enter verification code: ")

            try:
                self.client.sign_in(self.phone, code)
            except SessionPasswordNeededError:
                password = input("[?] Enter 2FA password: ")
                self.client.sign_in(password=password)

        print("[+] Logged in successfully!\n")
        return self.client

    def disconnect(self):
        """Disconnect"""
        self.client.disconnect()

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()