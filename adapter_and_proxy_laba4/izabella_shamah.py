class Target:
    def request(self) -> str:
        return "Целевое поведение"

class Adaptee:
    def specific_request(self) -> str:
        return ".еинедеов еономис яадазипА"

class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Адаптированное поведение: {self.adaptee.specific_request()[::-1]}"

def client_code(target: Target):
    print(target.request())

if __name__ == "__main__":
    print("Клиент работает с Target:")
    target = Target()
    client_code(target)
    
    print("\nКлиент работает с Adaptee через Adapter:")
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client_code(adapter)

class Subject:
    def request(self) -> None:
        pass


class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Обработка запроса.")


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Проверка доступа перед выполнением запроса.")
        return True

    def log_access(self) -> None:
        print("Proxy: Логирование времени запроса.", end="")


def client_code(subject: Subject):
    subject.request()

if __name__ == "__main__":
    print("Клиент работает с RealSubject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("\nКлиент работает с Proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)

class MediaPlayer:
    def play(self, audio_type: str, file_name: str) -> None:
        pass


class AdvancedMediaPlayer:
    def play_vlc(self, file_name: str) -> None:
        pass
    
    def play_mp4(self, file_name: str) -> None:
        pass

class VlcMp4Player(AdvancedMediaPlayer):
    def play_vlc(self, file_name: str) -> None:
        print(f"Воспроизведение VLC файла: {file_name}")
    
    def play_mp4(self, file_name: str) -> None:
        print(f"Воспроизведение MP4 файла: {file_name}")

class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type: str):
        self._advanced_player = VlcMp4Player()
        self._audio_type = audio_type

    def play(self, audio_type: str, file_name: str) -> None:
        if audio_type.lower() != self._audio_type.lower():
            print(f"MediaAdapter: Неподдерживаемый тип {audio_type}")
            return
            
        print("MediaAdapter (Proxy): Проверка прав доступа к файлу...")
        if audio_type.lower() == "vlc":
            self._advanced_player.play_vlc(file_name)
        elif audio_type.lower() == "mp4":
            self._advanced_player.play_mp4(file_name)
        print("MediaAdapter (Proxy): Завершение воспроизведения.")

if __name__ == "__main__":
    player = MediaAdapter("mp4")
    
    print("\nПопытка воспроизвести MP3:")
    player.play("mp3", "song.mp3")
    
    print("\nВоспроизведение MP4:")
    player.play("mp4", "movie.mp4")
    
    print("\nВоспроизведение VLC:")
    vlc_player = MediaAdapter("vlc")
    vlc_player.play("vlc", "presentation.vlc")
