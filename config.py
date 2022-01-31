import os
from dotenv import load_dotenv
load_dotenv()


class Settings():
    EVERNOTE_CONSUMER_KEY = os.getenv('EVERNOTE_CONSUMER_KEY', '')
    EVERNOTE_CONSUMER_SECRET = os.getenv('EVERNOTE_CONSUMER_SECRET', '')
    EVERNOTE_PERSONAL_TOKEN = os.getenv('EVERNOTE_PERSONAL_TOKEN', '')

    JOURNAL_TEMPLATE_NOTE_GUID = os.getenv('JOURNAL_TEMPLATE_NOTE_GUID', '')
    JOURNAL_NOTEBOOK_GUID = os.getenv('JOURNAL_NOTEBOOK_GUID', '')

    INBOX_NOTEBOOK_GUID = os.getenv('INBOX_NOTEBOOK_GUID', '')
    SANDBOX = os.getenv('SANDBOX', False)
