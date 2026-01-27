# TorrentSync

![Python](https://img.shields.io/badge/python-3.8+-blue?logo=python)
![Watchdog](https://img.shields.io/badge/watchdog-monitored-green)
![Paramiko](https://img.shields.io/badge/paramiko-SFTP-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A lightweight Python tool that monitors a Windows download folder (such as a torrent directory) and automatically uploads completed files to a Linux server via SFTP.

It uses:

- **Watchdog** — detects new files in real time  
- **Paramiko** — handles SFTP file transfer 

---

## Features

-  Monitors any folder for new files   
-  Automatically uploads files to a Linux server  
-  Runs continuously in the background  
-  Lightweight and easy to customize  

---

## Setup, Configuration & Usage

Install dependencies:

```bash
pip install watchdog paramiko
```
**Create your config file:**
- Copy data.example.json to data.json
- Edit data.json and set your values:
```
{
  "ip": "192.168.1.100",
  "username": "your_ssh_username",
  "password": "your_ssh_password",
  "watch_path": "R:/Torrent/Completed",
  "remote_dir": "/DATA/Media/TV"
}
```


---
## Run the script
```bash
python main.py
```
The script will monitor the folder and print messages like:
```console
Monitoring
Found: vid.mp4
Now Uploading ..
upload complete
```
---
## If you want to contribute fell free to add this improvements.

- Log events to a file instead of printing to console.

- Use SSH keys instead of passwords for secure authentication.

- Move or delete files locally after upload.

- Send notifications (Telegram/Discord) after upload.
