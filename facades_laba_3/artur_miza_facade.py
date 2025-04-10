class TV:
    def on(self):
        print("Телевизор включен.")

    def off(self):
        print("Телевизор выключен.")

class DVDPlayer:
    def on(self):
        print("DVD-плеер включен.")

    def off(self):
        print("DVD-плеер выключен.")

    def play(self, movie):
        print(f"Воспроизведение фильма: {movie}")

class SoundSystem:
    def on(self):
        print("Акустическая система включена.")

    def off(self):
        print("Акустическая система выключена.")

    def set_volume(self, level):
        print(f"Уровень громкости установлен на: {level}")

class HomeTheaterFacade:
    def __init__(self):
        self.tv = TV()
        self.dvd_player = DVDPlayer()
        self.sound_system = SoundSystem()

    def watch_movie(self, movie):
        print("Подготовка к просмотру фильма...")
        self.tv.on()
        self.sound_system.on()
        self.sound_system.set_volume(10)
        self.dvd_player.on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print("Завершение просмотра фильма...")
        self.dvd_player.off()
        self.sound_system.off()
        self.tv.off()

if __name__ == "__main__":
    home_theater = HomeTheaterFacade()
    home_theater.watch_movie("Властелин колец")
    home_theater.end_movie()
