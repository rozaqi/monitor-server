# monitor-server
Telegram Bot for server monitoring

step by step
git clone https://github.com/rozaqiw/monitor-server/
cd monitor-server

in telegram-send.sh change group_id and bot token
nano telegram-send.sh

add permission
chmod +x telegram-send.sh

test message
./telegram-send.sh "Test message"

move script telegram-send.sh to /usr/bin/telegram-send
sudo mv telegram-send.sh /usr/bin/telegram-send

move login-notify.sh to /etc/profile.d/ folder
sudo mv login-notify.sh /etc/profile.d/login-notify.sh

re-login ssh and check your bot telegram
