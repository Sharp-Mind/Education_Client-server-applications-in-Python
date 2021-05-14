from socket import *
import json

known_users = {'Bobik_Rubika': 'TheblastFormThepast'}
auth_users = []
codes = {'200': {"response": '200',
                 "alert": "OK"
                 },
         '409': {"response": '409',
                 "error": "Someone is already connected with the given user name"
                 },
         '402': {
    "response": '402',
    "error": "This could be 'wrong password' or 'no account with that name'"
}
}

msg_answer = {'authenticate': codes['200'],
              'already_connected': codes['409'],
              'presence': codes['200'],
              'wrong_user_pass': codes['402'],
              'quit': codes['200']
              }


action_cases = ('presence', 'quit')

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8008))
s.listen(5)

client, addr = s.accept()


msg = ''
act = ''
while True:

    if act == 'quit':
        client.close()
        act = ''
        break
    elif act != 'quit':

        data = json.loads(client.recv(2000000).decode("utf-8"))
        print('Сообщение: ', data, ' было отправлено клиентом: ', addr)
        act = data['action']

        if act == 'authenticate':

            if data['user']['account_name'] not in list(known_users.keys()):
                msg = msg_answer['wrong_user_pass']
            elif data['user']['account_name'] not in auth_users:
                auth_users.append([str(data['user']['account_name'])])
                msg = msg_answer['authenticate']
            elif data['user']['account_name'] in auth_users:
                msg = msg_answer['already_connected']
        else:

            for action_case in action_cases:
                if act == action_case:
                    msg = msg_answer[action_case]

        client.send(json.dumps(msg).encode('utf-8'))
        print(f'Отправлено сообщение: {msg}')
