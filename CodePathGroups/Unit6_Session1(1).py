# Problem 1: Building a Playlist
# The assignment statement to the top_hits_2010s variable below creates the linked list Uptown Funk -> Party Rock Anthem -> Bad Romance. Break apart the assignment statement into multiple lines with one call to the Node constructor per line to recreate the list.

from platform import node


class SongNode:
	def __init__(self, song, next=None):
		self.song = song
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
		
top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

# break up the assignment into different lines
# use the next pointers

node3 = SongNode("Bad Romance")
node2 = SongNode("Party Rock Anthem", node3)
node1 = SongNode("Uptown Funk", node2)

print_linked_list(node1)

# Problem 2: Top Artists
# Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.

# Understand: use a dictionary to map the artist frequency. If there is an artist in the dictionary, increase the value ( += 1), else add it to the dictionary ( = 1)

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def get_artist_frequency(playlist):
    frequency = {}
    current = playlist
    while current:
        if current.artist in frequency:
            frequency[current.artist] += 1
        else:
            frequency[current.artist] = 1
        current = current.next
    return frequency


playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

get_artist_frequency(playlist)