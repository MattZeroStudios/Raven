import os


class AP:
    def __init__(self):
        pass


# scans area with certain interface to find areas
def scan(interface, *band):
    pass


# Sends distributed or focused Deauthentication frames to capture the handshake
def deauthenticate(interface, targetap, *client):
    pass


# Check if handshake file has handshake and if yes, it will clean up the file.
def check_handshake():
    pass


# If local resources are used it will crack the handshake on Raven or it will forward it as a Job to Odin.
def crack(platform):
    pass
