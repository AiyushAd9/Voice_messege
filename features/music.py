import os
import random
import pygame

# Initialize pygame mixer once
pygame.mixer.init()

pygame.mixer.music.set_volume(1.0)  # Max volume

# Music folder path
MUSIC_DIR = os.path.join("assets", "music")

def play_music():
    try:
        songs = [song for song in os.listdir(MUSIC_DIR) if song.endswith(('.mp3', '.wav'))]
        if not songs:
            print("❌ No music files found.")
            return

        song = random.choice(songs)
        song_path = os.path.join(MUSIC_DIR, song)

        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        print(f"🎵 Now playing: {song}")

    except Exception as e:
        print(f"❌ Error playing music: {e}")

def stop_music():
    try:
        pygame.mixer.music.stop()
        print("⏹️ Music stopped.")
    except Exception as e:
        print(f"❌ Error stopping music: {e}")
