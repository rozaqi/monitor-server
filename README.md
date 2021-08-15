# Telegram Bot for server monitoring


### Installation

A. Send notification on SSH login 
1. Clone the repo
   ```sh
   git clone https://github.com/rozaqiw/monitor-server/
   ```
2. Change Directory
   ```sh
   cd monitor-server
   ```
3. in telegram-send.sh change group_id and bot token     
   ```sh
   nano telegram-send.sh
   ```
4. Add permission    
   ```sh
   chmod +x telegram-send.sh
   ```
5. test message    
   ```sh
   ./telegram-send.sh "Test message"
   ```
6. move script telegram-send.sh to /usr/bin/telegram-send           
   ```sh
   sudo mv telegram-send.sh /usr/bin/telegram-send
   ```
7. move login-notify.sh to /etc/profile.d/ folder
   ```sh
   sudo mv login-notify.sh /etc/profile.d/login-notify.sh
   ```
re-login ssh and check your bot telegram

B. Monitoring Server 
1. Running python utama 
   ```sh
   python3 utama.py
   ```

# Telegram Bot-Api


API Token - Get Api Token from [@botfather](https://telegram.me/botfather)

## Features

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
