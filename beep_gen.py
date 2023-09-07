#!/usr/bin/python3
import numpy as np
import threading
import sounddevice as sd
import time
import keyboard

audio_playing = False

def play_beep():
    global audio_playing

    def play_sound(frequency, duration):
        t = np.linspace(0, duration, int(44100 * duration), endpoint=False)
        audio_sig = 0.5 * np.sin(2 * np.pi * frequency * t)

        while audio_playing:
            sd.play(audio_sig, 44100)
            sd.wait()

    print("Press 't' to stop")
    
    while True:
        if not audio_playing:
            audio_playing = True
            audio_thread = threading.Thread(target=play_sound, args=(2400, 1))
            audio_thread.start()
        
        if keyboard.is_pressed('t'):
            audio_playing = False
            audio_thread.join()
            sd.stop()
            print("Beep stopped.")
            break

if __name__ == "__main__":
    play_beep()
