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
def psngs(songName):
    # play all the songs that match a given name
    search = client.search(songName, type='Songs')
    for song in search:
            print(song)
            subprocess.call(['mplayer', song.stream.url])


# play from queue
# this seems to be working but it's not very elegant 
def pq():
    q = open('queue', 'r')
    next = q.readline()
    while next:
        # add the current song to the history file
        h = open('history', 'a')
        h.write(next)
        h.close()

        # get the tail of the queue
        rest = q.read()
        q.close()

        # overwrte the queue file with the tail of the queue
        q = open('queue', 'w')
        q.write(rest)
        q.close()

        # play the next song in the queue
        psng(next)
        
        # open the queue file and get the next song to be played 
        q = open('queue', 'r')
        next = q.readline()
    q.close()


# read the current list of songs in the queue
def rq():
    q = open('queue', 'r')
    next = q.readline()
    while next:
        print(next)
        next = q.readline()


# show the history of songs previously played from the queue
def hist():
    h = open('history', 'r')
    next = h.readline()
    while next:
        print(next)
        next = h.readline()


# enqueue a search string
def enq(songName):
    q = open('queue', 'a')
    q.write(songName + "\n")
    q.close()


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
    # find all playlists that match a given name
    search = client.search(plName, type='Playlists')
    for pl in search:
        for song in pl.songs:
            print(song)
