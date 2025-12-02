import logging
import os
import sys
import time

import paramiko
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

def on_created(event):
    #When ever he detect a file he will upload
    filepath = event.src_path
    print(f"Found: {filepath}")

    print("Now Uploading ..")

    #Uplaod now

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname = 'put your ip',username = 'put your username',password = 'the password for username',port=22)
    sftp_client = ssh.open_sftp() 
    sftp_client.put(filepath, f"/To/Your/server/dir/{os.path.basename(filepath)}")
    sftp_client.close()
    ssh.close()
    print("upload complete")

if __name__ == "__main__":
    event_handler = FileSystemEventHandler()
    # Calling the function
    event_handler.on_created = on_created
    #Path
    path = "Your completed torrent file"
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        print("Monitoring")
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        print("Done")
        observer.join()

