class Amplifier:
    def on(self):
        print("Усилитель включен.")

    def off(self):
        print("Усилитель выключен.")

    def set_volume(self, level):
        print(f"Установка громкости на уровень {level}.")

class DVDPlayer:
    def on(self):
        print("DVD-плеер включен.")

    def off(self):
        print("DVD-плеер выключен.")

    def play(self, movie):
        print(f"Воспроизведение фильма: {movie}")

    def stop(self):
        print("Остановка фильма.")

class Projector:
    def on(self):
        print("Проектор включен.")

    def off(self):
        print("Проектор выключен.")

    def wide_screen_mode(self):
        print("Проектор в режиме широкого экрана.")

class HomeTheaterFacade:
    def __init__(self, amplifier, dvd_player, projector):
        self.amplifier = amplifier
        self.dvd_player = dvd_player
        self.projector = projector

    def watch_movie(self, movie):
        print("Приготовьтесь к просмотру фильма...")
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amplifier.on()
        self.amplifier.set_volume(5)
        self.dvd_player.on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print("Выключение домашнего кинотеатра...")
        self.dvd_player.stop()
        self.dvd_player.off()
        self.amplifier.off()
        self.projector.off()

# Использование фасада
if __name__ == "__main__":
    amplifier = Amplifier()
    dvd_player = DVDPlayer()
    projector = Projector()

    home_theater = HomeTheaterFacade(amplifier, dvd_player, projector)

    home_theater.watch_movie("Начало")
    home_theater.end_movie()
