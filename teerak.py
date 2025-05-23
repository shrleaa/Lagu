import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
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
        ("\nMán màak kwà kham wâa thîi-rák", 0.06),
        ("Thîi chăn yók hâi thôe nà thîi-rák", 0.09),
        ("Khâe rao dâi jôe phîang dâi sòp-dtaa kô rúu wâa kham-níi", 0.10),
        ("Yang bpen khǒng chăn láe thôe sà-mǒe", 0.10),
        ("\nThîi-rák thúk-khráng thîi dâi yin kham wâa rák", 0.11),
        ("Nâi jai mán nûek-thǔeng phîang-khâe thôe, ohh", 0.09),
        ("Yàak hâi rúu ao-wái wâa", 0.10),
        ("Ôm-gòt níi bpen khǒng thôe ná thîi-rák", 0.11),
    ]

    delays = [
        0.3,  # Mán màak kwà kham wâa thîi-rák
        2.5,  # Thîi chăn yók hâi thôe nà thîi-rák
        3.5,  # Khâe rao dâi jôe phîang dâi sòp-dtaa kô rúu wâa kham-níi
        4.5,  # Yang bpen khǒng chăn láe thôe sà-mǒe
        5.5,  # Thîi-rák thúk-khráng thîi dâi yin kham wâa rák
        6.5,  # Nâi jai mán nûek-thǔeng phîang-khâe thôe
        7.5,  # Yàak hâi rúu ao-wái wâa
        8.5,  # Ôm-gòt níi bpen khǒng thôe ná thîi-rák
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