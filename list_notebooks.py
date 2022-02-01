#!/usr/bin/env python
# -*- coding: utf-8 - *-
from evernote.api.client import EvernoteClient

from config import Settings


if __name__ == '__main__':
    config = Settings()
    client = EvernoteClient(
        token=config.EVERNOTE_PERSONAL_TOKEN,
        sandbox=config.SANDBOX
    )
    note_store = client.get_note_store()

    notebooks = note_store.listNotebooks()
    for notebook in notebooks:
        print('%s - %s' % (notebook.guid, notebook.name))
