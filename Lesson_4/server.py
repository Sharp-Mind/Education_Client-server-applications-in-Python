from socket import *
import pickle


pickle.DEFAULT_PROTOCOL

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
},
    '404': {
    "response": '404',
                "error": "Unknown message"}
}

msg_answer = {'authenticate': codes['200'],
              'already_connected': codes['409'],
              'presence': codes['200'],
              'wrong_user_pass': codes['402'],
              'quit': codes['200'],
              'not_found': codes['404']
              }


action_cases = ('presence', 'quit')


def recieve_msg(client, addr):
    data = pickle.loads(client.recv(2000000), fix_imports=True,
                        encoding='utf-8', errors="strict")
    print('Сообщение: ', data, ' было отправлено клиентом: ', addr)
    return(data)


def auth_case(data, msg=codes['404']):
    if data['user']['account_name'] not in list(known_users.keys()):
        msg = msg_answer['wrong_user_pass']
    elif data['user']['account_name'] not in auth_users:
        auth_users.append([str(data['user']['account_name'])])
        msg = msg_answer['authenticate']
    elif data['user']['account_name'] in auth_users:
        msg = msg_answer['already_connected']
    return msg


def roll_my_cases(act, msg=codes['404']):
    for action_case in action_cases:
        if act == action_case:
            msg = msg_answer[action_case]
    return msg


def keepitrolling(a=''):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 8008))
    s.listen(5)

    client, addr = s.accept()

    while act != 'quit':
        data = recieve_msg(client, addr)
        act = data['action']
        if act == 'authenticate':
            msg = auth_case(data)
        else:
            msg = roll_my_cases(act)

        client.send(pickle.dumps(msg, protocol=None,
                                 fix_imports=True, buffer_callback=None))

        print(f'Отправлено сообщение: {msg}')

    client.close()


if __name__ == "__main__":
    keepitrolling()
