from socket import *
from sys import argv
import pickle
import time


pickle.DEFAULT_PROTOCOL
addr, port = argv[1], argv[2]

action_tosend = [
    {
        "action": "authenticate",
        "time": str(int(time.time())),
        "user": {"account_name": "Bobik_Rubika", "password": "TheblastFormThepast"},
    },
    {
        "action": "presence",
        "time": str(int(time.time())),
        "type": "status",
        "user": {"account_name": "Bobik_Rubika", "password": "TheblastFormThepast"},
    },
    {"action": "quit"},
]

action_on_response = {
    "authenticate_200": action_tosend[1],
    "authenticate_409": action_tosend[1],
    "authenticate_402": action_tosend[2],
    "presence_200": action_tosend[2],
}


def set_case(act):
    global case
    case = act


def connect():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, int(port)))
    # s.connect(('localhost', 8008))
    s.send(
        pickle.dumps(
            action_tosend[0], protocol=None, fix_imports=True, buffer_callback=None
        )
    )
    return s


def msg_recieve():
    data = pickle.loads(
        s.recv(2000000),
        fix_imports=True,
        encoding="utf-8",
        errors="strict",
        buffers=None,
    )

    print("Сообщение от сервера: ", data, ", длиной ", len(data), " байт")

    return data


def answer_send(msg):
    s.send(pickle.dumps(msg, protocol=None, fix_imports=True, buffer_callback=None))
    print(f"Сообщение {msg} отправлено на сервер.")


def answer_choise(data, msg=""):
    for action in list(action_on_response.keys()):
        if action.find(case) != -1 and action.find(data["response"]) != -1:
            msg = action_on_response[f'{case}_{data["response"]}']
            set_case(msg["action"])
            return msg


def keepitrolling():
    while case != "quit":
        answer_send(answer_choise(msg_recieve()))
    s.close()


if __name__ == "__main__":
    case = action_tosend[0]["action"]
    s = connect()
    keepitrolling()
