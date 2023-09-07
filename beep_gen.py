#!/usr/bin/python3
import numpy as np
import keyboard
import threading
import pyaudio
import wave

audio_playing = False

def play_sound(frequency, duration):
    global audio_playing
    
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

    t = np.linspace(0, duration, int(44100 * duration), endpoint=False)
    audio_sig = 0.5 * np.sin(2 * np.pi * frequency * t)

    for _ in range(5):#playing 5 consecutive beeps
        if keyboard.is_pressed('t'):
            break
        else:
            print("ALARM")
            stream.write(audio_sig.tobytes())

    stream.stop_stream()
    stream.close()
    p.terminate()
    audio_playing = False

if __name__ == "__main__":
    print("Press 't' to stop")
    audio_thread = threading.Thread(target=play_sound, args=(2400, 1))
    audio_thread.start()
    keyboard.wait('t')
    audio_thread.join()
    print("Beep stopped.")
