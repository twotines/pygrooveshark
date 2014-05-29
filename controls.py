from __future__ import print_function
import subprocess
from grooveshark import Client
from grooveshark.classes import Radio
client = Client()
client.init()


#   execfile('notes.py')
   

def getFirst(iterable):
    for item in iterable:
        print(item)
        return item



# search for a song 
def psng(songName):
    search = client.search(songName, type='Songs')
    song = getFirst(search)
    subprocess.call(['mplayer', song.stream.url])


# search for a song 
def ssng(songName):
    search = client.search(songName, type='Songs')
    song = getFirst(search)


# find all playlists matching a term and play all of them  :)
def ppls(plName):
    """play all playlists that match a given name"""
    search = client.search(plName, type='Playlists')
    for pl in search:
        for song in pl.songs:
            print(song)
            subprocess.call(['mplayer', song.stream.url])


# find all playlists matching a term and list the tracks
def spls(plName):
    """play all playlists that match a given name"""
    search = client.search(plName, type='Playlists')
    for pl in search:
        for song in pl.songs:
            print(song)


