import time
from functools import wraps

# Декоратор для логирования времени выполнения
def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} выполнен за {end_time - start_time:.4f} секунд")
        return result
    return wrapper

# Декоратор для проверки корректности данных
def validate_text(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text = args[0] if args else kwargs.get('text', '')
        if not text.strip():
            raise ValueError("Текст не должен быть пустым")
        return func(*args, **kwargs)
    return wrapper

# Декоратор для подсчета статистики слов
def word_statistics(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text = args[0] if args else kwargs.get('text', '')
        words = text.split()
        word_count = len(words)
        print(f"Статистика: {word_count} слов")
        return func(*args, **kwargs)
    return wrapper

# Класс для чтения текста из файла
class FileReader:
    @log_time
    def read(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

# Класс для обработки текста
class TextProcessor:
    @log_time
    @validate_text
    @word_statistics
    def process(self, text):
        # Пример обработки: приведение к нижнему регистру и удаление стоп-слов
        stop_words = {'и', 'в', 'на', 'с', 'по', 'для'}
        text = text.lower()
        words = text.split()
        filtered_words = [word for word in words if word not in stop_words]
        return ' '.join(filtered_words)

# Класс для записи текста в файл
class FileWriter:
    @log_time
    @validate_text
    def write(self, file_path, text):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)

# Фасад для объединения всех этапов
class TextProcessingFacade:
    def __init__(self):
        self.reader = FileReader()
        self.processor = TextProcessor()
        self.writer = FileWriter()

    def process_text(self, input_file, output_file):
        text = self.reader.read(input_file)
        processed_text = self.processor.process(text)
        self.writer.write(output_file, processed_text)

# Пример использования
if __name__ == "__main__":
    facade = TextProcessingFacade()
    facade.process_text('input.txt', 'output.txt')
