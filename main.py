import json
import logging
import os
import sys
import time

import paramiko
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

def on_created(event):
    if event.is_directory:
        return
    filepath = event.src_path
    print(f"Found: {filepath}")
    
    print("Now Uploading")
    
    #Uplaod now

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname = data["ip"],username = data["username"],password = data["password"],port=22)
    sftp_client = ssh.open_sftp() 
    sftp_client.put(filepath, f'{data["remote_dir"]}/{os.path.basename(filepath)}')
    sftp_client.close()
    ssh.close()
    print("upload complete")

if __name__ == "__main__":
    event_handler = FileSystemEventHandler()
    # Calling the function
    event_handler.on_created = on_created
    #Path
    watch_path = data["watch_path"]
    observer = Observer()
    observer.schedule(event_handler, watch_path, recursive=True)
    observer.start()
    try:
        print("Monitoring")
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        print("Done")
        observer.join()

