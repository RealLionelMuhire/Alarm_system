#!/usr/bin/python3
import numpy as np
import keyboard
import threading
import pyaudio


def play_beep():
    audio_playing = False

    def play_sound(frequency, duration):
        nonlocal audio_playing

        p = pyaudio.PyAudio()

        stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

        t = np.linspace(0, duration, int(44100 * duration), endpoint=False)
        audio_sig = 0.5 * np.sin(2 * np.pi * frequency * t)

        for _ in range(5):
            if keyboard.is_pressed('t'):
                break
            elif not audio_playing:
                print("ALARM")
                stream.write(audio_sig.tobytes())

        stream.stop_stream()
        stream.close()
        p.terminate()
        audio_playing = False

    print("Press 't' to stop")
    audio_thread = threading.Thread(target=play_sound, args=(2400, 1))
    while True:
        if not audio_playing and not audio_thread.is_alive():
            audio_thread = threading.Thread(target=play_sound, args=(2400, 1))
            audio_thread.start()
            audio_playing = True

        if keyboard.is_pressed('t'):
            audio_playing = False
            audio_thread.join()
            print("Beep stopped.")
            break


if __name__ == "__main__":
    play_beep()
