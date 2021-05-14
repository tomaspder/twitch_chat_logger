import socket
import logging
from twitter_auth import api

#Auth with Twitch
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'nakedddd' #your twitch name
token = 'your token'
channel = '#thegrefg' #channel name here

#socket settings to enable Twitch connection
sock = socket.socket()

sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

#setting for the log storage

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

#function to send a Twitter direct message
def send_dm(username, msg):
    user = api.get_user(username)
    recipient_id = user.id_str
    text = msg
    direct_message = api.send_direct_message(recipient_id, text)



while True:
    resp = sock.recv(2048).decode('utf-8')
    if 'repeira' in resp: #replace keyword to store only specific user message
        logging.info(resp)
        content = (resp[resp.find('#thegrefg :')+10:])
        user = "pereiraagus_" #Twitter username to send the message 
        msg = content
        send_dm(user, msg)

	#Status responses from Twitch to keep the connection if it's being used
    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))

    elif len(resp) > 0:
        #logging.info(demojize(resp))
        pass