import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0

def init(app):
    global entries, next_id
    try:

        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
        max_id = 0
        for e in entries:
            if 'id' in e and int(e['id']) >= max_id:
                max_id = int(e['id']) + 1
        next_id = max_id
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %H:%M %p")
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(next_id)}
    next_id += 1
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(idnum):
    global entries, GUESTBOOK_ENTRIES_FILE
    for e in entries:
        if e['id'] == idnum:
            entries.remove(e)
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, 'w')
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")