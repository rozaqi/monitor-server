
#!/bin/bash
    
# prepare any message you want
login_ip="$(echo $SSH_CONNECTION | cut -d " " -f 1)"
login_date="$(date +"%e %b %Y, %a %r")"
login_name="$(whoami)"

# For new line I use $'
' here
message="New login to server"$'
'"$login_name"$'
'"$login_ip"$'
'"$login_date"

#send it to telegram
telegram-send "$message"

