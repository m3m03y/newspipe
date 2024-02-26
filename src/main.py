"""Main module"""
import logging
from config.mailclient import ImapMailClient
from config.log import LogConf

LogConf()

client = ImapMailClient()
client.authenticate()
client.logout()
