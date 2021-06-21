import logging
from socket import *
import pickle
import inspect
from functools import wraps
from log.server_log import setup as get_logger


DEBUG = True

pickle.DEFAULT_PROTOCOL

known_users = {"Bobik_Rubika": "TheblastFormThepast"}
auth_users = []
codes = {
    "200": {"response": "200", "alert": "OK"},
    "409": {
        "response": "409",
        "error": "Someone is already connected with the given user name",
    },
    "402": {
        "response": "402",
        "error": "This could be 'wrong password' or 'no account with that name'",
    },
    "404": {"response": "404", "error": "Unknown message"},
}

msg_answer = {
    "authenticate": codes["200"],
    "already_connected": codes["409"],
    "presence": codes["200"],
    "wrong_user_pass": codes["402"],
    "quit": codes["200"],
    "not_found": codes["404"],
}


action_cases = ("presence", "quit")

logger_path = "Education_Client-server-applications-in-Python/project/log/server_log.py"


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


def mockable(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func.__name__ = func.__name__+'_mock' if DEBUG else func.__name__
        result = func.__name__(*args, **kwargs)
        return result
    return wrapper


def install_logs():
    return get_logger(logger_path)


def recieve_msg(client, addr):
    try:
        data = pickle.loads(
            client.recv(2000000), fix_imports=True, encoding="utf-8", errors="strict")
        log.info("Сообщение: ", data, " было отправлено клиентом: ", addr)
        return data
    except Exception as e:
        log.exception(e)
        return


def auth_case(data, msg=codes["404"]):
    try:
        if data["user"]["account_name"] not in list(known_users.keys()):
            msg = msg_answer["wrong_user_pass"]
        elif data["user"]["account_name"] not in auth_users:
            auth_users.append([str(data["user"]["account_name"])])
            msg = msg_answer["authenticate"]
        elif data["user"]["account_name"] in auth_users:
            msg = msg_answer["already_connected"]
        return msg
    except Exception as e:
        log.exception(e)
        return


# @mockable
def roll_my_cases(act, msg=codes["404"]):
    try:
        for action_case in action_cases:
            if act == action_case:
                msg = msg_answer[action_case]
        return msg
    except Exception as e:
        log.exception(e)
        return


def roll_my_cases_mock(act, msg=codes["404"]):
    try:
        return codes['200']
    except Exception as e:
        log.exception(e)
        return


def keepitrolling(act=""):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.bind(("", 8008))
        s.listen(5)

        log.info("Сокет открыт")

        client, addr = s.accept()

        log.info(f"Соединение установлено с: {addr}")

        while act != "quit":
            data = recieve_msg(client, addr)
            act = data["action"]
            log.info(f"Входящее сообщение: {data} ")
            if act == "authenticate":
                msg = auth_case(data)
            else:
                msg = roll_my_cases(act)

            client.send(
                pickle.dumps(msg, protocol=None, fix_imports=True,
                             buffer_callback=None)
            )

            log.info(f"Отправлено сообщение: {msg}")

        client.close()

    except Exception as e:
        log.exception(e)
        return


if __name__ == "__main__":
    log = install_logs()
    keepitrolling()
