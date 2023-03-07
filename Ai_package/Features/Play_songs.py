import os
import random
from random import randint

def play_songs():
    n = random.randint(0,2)
    print(n)
    music_dir = 'E:\Ratanabh\Ratanabh\Vlogs\Music'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir,songs[n]))

play_songs()