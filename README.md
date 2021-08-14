# monitor-server
Telegram Bot for server monitoring

step by step  
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
