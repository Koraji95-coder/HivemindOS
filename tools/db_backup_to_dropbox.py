"""
db_backup_to_dropbox.py
-----------------------
Uploads your encrypted SQLite database to Dropbox 'App' folder.

Usage:
    python tools/db_backup_to_dropbox.py
"""

import os
import dropbox

DB_PATH = "data/hivemind_memory.db"
DROPBOX_TOKEN = os.environ.get("DROPBOX_ACCESS_TOKEN")
DROPBOX_DEST = "/hivemind_memory.db"  # uploads to app folder

def upload_db():
    if not DROPBOX_TOKEN:
        print("DropBox access token missing from env.")
        return
    if not os.path.exists(DB_PATH):
        print("DB file not found:", DB_PATH)
        return
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)
    with open(DB_PATH, "rb") as f:
        dbx.files_upload(f.read(), DROPBOX_DEST, mode=dropbox.files.WriteMode.overwrite)
    print("Backup uploaded to Dropbox!")

if __name__ == "__main__":
    upload_db()