import logging
from logging.handlers import TimedRotatingFileHandler
logging.basicConfig(
    filename="Education_Client-server-applications-in-Python/project/log/app.log",
    format="%(asctime)s %(levelname)s %(module)s %(message)s",
    level=logging.INFO 
)


def setup(logger_name):
    log = log = logging.getLogger(logger_name)
    fh = TimedRotatingFileHandler("Education_Client-server-applications-in-Python/project/log/app.log", when='D', interval=1, backupCount=5)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s")
    fh.setFormatter(formatter)
    log.addHandler(fh)

    return log
