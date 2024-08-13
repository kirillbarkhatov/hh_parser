from abc import ABC, abstractmethod


class FileWorker(ABC):
    """Абстрактный класс, предъявляющий требования к подклассам, работающими с файлами"""

    @abstractmethod
    def save_to_file(self, vacancies: list[dict]) -> None:
        """Метод для сохранения в файл списка вакансий"""

        pass

    @abstractmethod
    def add_to_file(self, vacancies: list[dict]) -> None:
        """Метод для добавления в файл вакансий без дублирования"""

        pass

    @abstractmethod
    def get_from_file(self) -> list[dict]:
        """Метод для получения данных из файла"""

        pass

    @abstractmethod
    def delete_from_file(self, list_id_vacancies: list[str] | None = None) -> None:
        """Общий функционал для удаления данных из файла"""

        pass
