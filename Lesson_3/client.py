from socket import *
from sys import argv
import json
import time


addr, port = argv[1], argv[2]

action_tosend = {
    "authenticate": {"action": "authenticate", "time": f"{str(int(time.time()))}", "user": {"account_name": "Bobik_Rubika", "password": "TheblastFormThepast"}},
    "presence": {"action": "presence", "time": str(int(time.time())), "type": "status", "user": {"account_name": "Bobik_Rubika", "password": "TheblastFormThepast"}},
    "quit": {"action": "quit"}
}

action_on_response = {
    "authenticate_200": action_tosend["presence"],
    "authenticate_409": action_tosend["presence"],
    "authenticate_402": action_tosend["quit"],
    "presence_200": action_tosend["quit"],
}

case = list(action_tosend.keys())[0]
msg = action_tosend[case]

authed = False


s = socket(AF_INET, SOCK_STREAM)

s.connect((addr, int(port)))


s.send(json.dumps(msg).encode('utf-8'))
while True:

    if case != 'quit':
        data = json.loads(s.recv(1000000).decode('utf-8'))
    else:
        s.close()
        break

    print('Сообщение от сервера: ', data,
          ', длиной ', len(data), ' байт')

    for action in list(action_on_response.keys()):
        if action.find(case) != -1 and action.find(data['response']) != -1:
            msg = action_on_response[f'{case}_{data["response"]}']
            case = msg['action']            
            s.send(json.dumps(msg).encode('utf-8'))
            print(f'Сообщение {msg} отправлено на сервер.')
