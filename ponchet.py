import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.01):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nCause you're the one that I like", 0.07),
        ("I can't deny", 0.08),
        ("Every night you're on my mind", 0.09),
        ("So if I call you tonight", 0.09),
        ("Will you pick up and give me your time?", 0.08),
        ("Miss you every night", 0.09),
        ("Miss you all the time", 0.10),

        ("\nNo, I don't even know", 0.08),
        ("Where to start", 0.09),

        ("\nCause you're the one that I like", 0.08),
        ("I can't deny", 0.08),
        ("Everything I feel inside", 0.09),
        ("Will you tell me I'm the one?", 0.09),
        ("The one inside of your heart", 0.10),
        ("Used to brush aside", 0.08),
        ("Now I can't deny", 0.09),
        ("That baby you're my special one", 0.09),
        ("Cause you're the one that I like", 0.08),
    ]

    delays = [
        0.0,    # Cause you're the one that I like
        2.1,    # I can't deny
        3.5,    # Every night you're on my mind
        5.3,    # So if I call you tonight
        7.0,   # Will you pick up and give me your time?
        8.5,   # Miss you every night
        8.9,   # Miss you all the time

        10.9,   # No, I don't even know
        11.7,   # Where to start

        13.0,   # Cause you're the one that I like
        14.4,   # I can't deny
        18.9,   # Everything I feel inside
        20.7,   # Will you tell me I'm the one?
        25.8,   # The one inside of your heart
        29.9,   # Used to brush aside
        33.5,   # Now I can't deny
        35.9,   # That baby you're my special one
        37.9,   # Cause you're the one that I like
    ]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
