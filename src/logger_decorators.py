from time import time
from src.logger_settings import logger_func_call
from functools import wraps
from typing import Any


def func_call_logging(func: Any) -> Any:
    """Декоратор для логирования вызова функции"""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        wrapper.call_count += 1
        logger_func_call.info(f"Функция {func.__module__}.{func.__name__}. Вызов № {wrapper.call_count}")
        time_1 = time()
        result = func(*args, **kwargs)
        time_2 = time()
        logger_func_call.info(f"Функция {func.__module__}.{func.__name__} завершила работу. Время работы: {round(time_2 - time_1, 3)} сек.")
        return result
    wrapper.call_count = 0
    return wrapper
