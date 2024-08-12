from abc import ABC, abstractmethod
from typing import Any


class FileWorker(ABC):
    """Абстрактный класс, предъявляющий требования к подклассам, работающими с файлами"""

    @abstractmethod
    def save_to_file(self, *args: Any, **kwargs: Any) -> Any:
        """Общий функционал для сохранения данных в файл"""

        pass

    @abstractmethod
    def get_from_file(self, *args: Any, **kwargs: Any) -> Any:
        """Общий функционал для получения данных из файла"""

        pass

    @abstractmethod
    def delete_from_file(self, *args: Any, **kwargs: Any) -> Any:
        """Общий функционал для удаления данных из файла"""

        pass
