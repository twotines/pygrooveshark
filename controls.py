from __future__ import print_function
import subprocess
from grooveshark import Client
from grooveshark.classes import Radio
client = Client()
client.init()


def getFirst(iterable):
    for item in iterable:
        print(item)
        return item


# play the first song that matches a query string
def psng(songName):
    search = client.search(songName, type='Songs')
    song = getFirst(search)
    subprocess.call(['mplayer', song.stream.url])


# search for a song 
def ssng(songName):
    search = client.search(songName, type='Songs')
    song = getFirst(search)

# search for a song 
def ssngs(songName):
    search = client.search(songName, type='Songs')
    for song in search:
            print(song)

# find all playlists containing an item with a matching term and play all of them
def ppls(plName):
    # play all playlists that match a given name
    search = client.search(plName, type='Playlists')
    for pl in search:
        for song in pl.songs:
            print(song)
            subprocess.call(['mplayer', song.stream.url])


# find all playlists containing an item with a matching term and list all of the tracks
def spls(plName):
    # play all playlists that match a given name
    search = client.search(plName, type='Playlists')
    for pl in search:
        for song in pl.songs:
            print(song)


