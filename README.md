# monitor-server
Telegram Bot for server monitoring

A. Send notification on SSH login 
1. git clone https://github.com/rozaqiw/monitor-server/   
2. cd monitor-server

in telegram-send.sh change group_id and bot token                  
3. nano telegram-send.sh

add permission    
4. chmod +x telegram-send.sh

test message    
5. ./telegram-send.sh "Test message"

move script telegram-send.sh to /usr/bin/telegram-send           
6. sudo mv telegram-send.sh /usr/bin/telegram-send

move login-notify.sh to /etc/profile.d/ folder          
7. sudo mv login-notify.sh /etc/profile.d/login-notify.sh

re-login ssh and check your bot telegram

B. Monitoring Server 
1. python3 utama.py

# Telegram Bot-Api


API Token - Get Api Token from [@botfather](https://telegram.me/botfather)

### Video Tutorial

https://www.youtube.com/watch?v=qIuGJEAAIHY

## Features Of [@github_rbot]

- [x] Start (`/start`)

- [x] Help (`/help`)

# List Command Monitoring Server Linux

  - [x] List file,directory (`ls`)

  - [x] Current directory (`pwd`)

  - [x] Display the total amount of physical memory and system swap and buffers used by the kernel (`free`)

  - [x] it is used to find out how long the system is active (running). (`uptime`)

  - [x] Test Internet connection (`koneksi`)

  - [x] Display the list of all the users logged in and out (`last`)

  - [x] Prints the name of the user associated with the current effective user ID (`whoami`)
