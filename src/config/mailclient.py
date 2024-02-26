"""Provides imap4 mail client"""
import imaplib
import os
import logging
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class ImapMailClient:
    """Class to handle IMAP4 mail client configuration"""
    username: str
    password: str
    server_name: str  #https://www.systoolsgroup.com/imap/
    server: imaplib.IMAP4_SSL

    def __init__(self):
        load_dotenv()
        self.username = os.getenv("SECURE_USER")
        self.password = os.getenv("SECURE_KEY")
        self.server_name = os.getenv("IMAP_SERVER")
        logging.info("Mail configuration:")
        logging.info("              username=%s", self.username)
        logging.info("              server_name=%s", self.server_name)
        self.server = imaplib.IMAP4_SSL(self.server_name)
        logging.debug("Mail client successfully created")

    def authenticate(self):
        """Authenticates provided user on imap mail server"""
        self.server.login(self.username, self.password)
        logging.debug("User: %s successfully logged in", self.username)

    def logout(self):
        """Logs out provided user from imap mail server"""
        self.server.logout()
        logging.debug("User: %s successfully logged out", self.username)
    