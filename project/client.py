import inspect
import logging
import pickle
import time
from socket import *
from sys import argv
from functools import wraps
from log.client_log import setup as get_logger


pickle.DEFAULT_PROTOCOL
# addr, port = argv[1], argv[2]

DEBUG = True


def mockable(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func.__name__ = func.__name__ + "_mock" if DEBUG else func.__name__        
        result = func.__name__(*args, **kwargs)
        return result
    return wrapper


class Log:
    def __init__(self):
        pass

    def __call__(self, func):
        def decorated(*args, **kwargs):
            upper_func = None
            res = func(*args, **kwargs)

            for i in inspect.stack():
                if i[4][0].find(func.__name__) != -1:
                    upper_func = i[3]
                    break
            log.info(
                f"Функция {func.__name__}, {args, kwargs} была вызвана из функции {upper_func}"
            )

            return res

        return decorated


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

logger_path = "Education_Client-server-applications-in-Python/project/log/client_log.py"


def install_logs():
    return get_logger(logger_path)


def set_case(act):
    try:
        global case
        case = act
    except Exception as e:
        log.exception(e)
        return


def connect():
    try:
        s = socket(AF_INET, SOCK_STREAM)
        # s.connect((addr, int(port)))
        s.connect(("localhost", 8008))
        s.send(
            pickle.dumps(
                action_tosend[0], protocol=None, fix_imports=True, buffer_callback=None
            )
        )
        return s
    except Exception as e:
        log.exception(e)
        return


# @mockable
def msg_recieve():
    try:
        data = pickle.loads(
            s.recv(2000000),
            fix_imports=True,
            encoding="utf-8",
            errors="strict",
            buffers=None,
        )

        log.info(f"Сообщение от сервера: {data} длиной {len(data)} байт")

        return data

    except Exception as e:
        log.exception(e)
        return


def msg_recieve_mock():
    try:
        data = {"response": "200", "alert": "OK"}

        log.debug(f"Сообщение от сервера: {data} длиной {len(data)} байт")

        return data

    except Exception as e:
        log.exception(e)
        return


@Log()
def send(msg):
    s.send(pickle.dumps(msg, protocol=None, fix_imports=True, buffer_callback=None))
    log.info(f"Сообщение {msg} отправлено на сервер.")


def answer_send(msg):
    try:
        send(msg)
    except Exception as e:
        log.exception(e)
        return


def answer_choise(data, msg=""):
    try:
        for action in list(action_on_response.keys()):
            if action.find(case) != -1 and action.find(data["response"]) != -1:
                msg = action_on_response[f'{case}_{data["response"]}']
                set_case(msg["action"])
                break
        return msg

    except Exception as e:
        log.exception(e)
        return


def fake_case():
    for i in range(action_tosend[1], action_tosend[2]):
        yield i


fake_msg = fake_case()


def answer_choise_mock(data, msg=""):
    try:
        set_case(next(fake_msg["action"]))
        return msg

    except Exception as e:
        log.exception(e)
        return


@Log()
def keepitrolling():
    try:
        while case != "quit":
            answer_send(answer_choise(msg_recieve()))
        s.close()
    except Exception as e:
        log.exception(e)
        return


if __name__ == "__main__":
    log = install_logs()
    case = action_tosend[0]["action"]
    s = connect()
    keepitrolling()
