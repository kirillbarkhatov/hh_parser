import logging


# Настройки логгирования вызовов функций для декоратора
logger_func_call = logging.getLogger(__name__)
logger_func_call.setLevel(logging.DEBUG)
fh = logging.FileHandler(f"logs/funcs_calls.log", mode="w")
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger_func_call.addHandler(fh)


# Настройки логгирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(f"logs/{__name__}.log", mode="w")
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
