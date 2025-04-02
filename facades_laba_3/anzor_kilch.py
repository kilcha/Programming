import os
import time

class FileReader:
    def read(self, file_path):
        script_dir=os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "input.txt")
        with open(file_path, 'r', encoding='UTF-8') as file:
            content = file.read()
        return content
        
class TextProcessor:
    def process(self, text):
        text = text.lower()
        text = self.remove_stop_words(text)
        return text
    
    def remove_stop_words(self, text):
        stop_words = set(['и', 'в', 'на', 'с', 'по', 'для', 'а', 'но', 'или', 'это'])
        words = text.split()
        filtered_words = [word for word in words if word not in stop_words]
        return ' '.join(filtered_words)
    
class FileWriter:
    def write(self, file_path, text):
        script_dir=os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "input.txt")
        with open(file_path, 'w', encoding='UTF-8') as file:
            content = file.write(text)
        return content

def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения {func.__name__}: {end_time - start_time:.4f} секунд")
        return result
    return wrapper

def validate_text(func):
    def wrapper(*args, **kwargs):
        text = args[1] if len(args) > 1 else kwargs.get('text', '')
        if not text.strip():
            raise ValueError("Текст не может быть пустым")
        return func(*args, **kwargs)
    return wrapper

def word_count_statistics(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        words = result.split()
        print(f"Статистика: {len(words)} слов")
        return result
    return wrapper

class TextProcessingFacade:
    def __init__(self):
        self.file_reader = FileReader()
        self.text_processor = TextProcessor()
        self.file_writer = FileWriter()

    @log_time
    @validate_text
    @word_count_statistics
    def processing_text(self, input_file, output_file):
        text = self.file_reader.read(input_file)
        processed_text = self.text_processor.process(text)
        self.file_writer.write(output_file, processed_text)

if __name__ == "__main__":
    facade = TextProcessingFacade()
    facade.processing_text('input.txt', 'output.txt')
