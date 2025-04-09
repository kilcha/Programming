from abc import ABC, abstractmethod
import time

class NewMediaPlayer(ABC):
    @abstractmethod
    def play_video(self, file_name: str) -> None:
        pass
    
    @abstractmethod
    def play_audio(self, file_name: str) -> None:
        pass

class OldVideoPlayer:
    def play(self, file_name: str, format_type: str) -> None:
        if format_type not in ['mp4', 'avi']:
            raise ValueError(f"Unsupported format: {format_type}")
        print(f"Playing video file: {file_name}.{format_type}")
        time.sleep(1)

class OldPlayerAdapter(NewMediaPlayer):
    def __init__(self, old_player: OldVideoPlayer):
        self.old_player = old_player
    
    def play_video(self, file_name: str) -> None:
        if '.' in file_name:
            name, format_type = file_name.split('.')
        else:
            name, format_type = file_name, 'mp4'
        
        self.old_player.play(name, format_type)
    
    def play_audio(self, file_name: str) -> None:
        raise NotImplementedError("Old player doesn't support audio")

class RealMediaPlayer(NewMediaPlayer):
    def play_video(self, file_name: str) -> None:
        print(f"Real player: Streaming video {file_name} in high quality")
        time.sleep(2)
    
    def play_audio(self, file_name: str) -> None:
        print(f"Real player: Playing audio {file_name} with surround sound")
        time.sleep(1)

class MediaPlayerProxy(NewMediaPlayer):
    def __init__(self, real_player: NewMediaPlayer, user_role: str = "user"):
        self.real_player = real_player
        self.user_role = user_role
    
    def play_video(self, file_name: str) -> None:
        start_time = time.time()
        
        if self.user_role not in ['admin', 'premium_user']:
            print("Access denied: You need premium subscription to watch videos")
            return
        
        if 'ultra_hd' in file_name and self.user_role != 'admin':
            print("Access denied: Only admin can watch Ultra HD content")
            return
        
        print(f"Proxy: Checking video file {file_name} for viruses...")
        self.real_player.play_video(file_name)
        print(f"Proxy: Video playback completed. Time: {time.time() - start_time:.2f}s")
    
    def play_audio(self, file_name: str) -> None:
        start_time = time.time()
        print(f"Proxy: Logging audio playback request for {file_name}")
        self.real_player.play_audio(file_name)
        print(f"Proxy: Audio playback completed. Time: {time.time() - start_time:.2f}s")

def test_media_system():
    print("\nTesting Adapter Pattern:")
    old_player = OldVideoPlayer()
    adapter = OldPlayerAdapter(old_player)
    
    try:
        adapter.play_video("movie.avi")
        adapter.play_video("presentation.mp4")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting Proxy Pattern:")
    real_player = RealMediaPlayer()
    proxy = MediaPlayerProxy(real_player, "premium_user")
    
    proxy.play_audio("podcast.mp3")
    proxy.play_video("movie_hd.mp4")
    
    print("\nTesting Proxy with restricted access:")
    free_user_proxy = MediaPlayerProxy(real_player, "user")
    free_user_proxy.play_video("movie_hd.mp4")
    free_user_proxy.play_audio("song.mp3")

if __name__ == "__main__":
    test_media_system()