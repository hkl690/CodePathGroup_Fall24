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

node1 = SongNode("Bad Romance")
node2 = SongNode("Party Rock Anthem")
node2.next = node1
node3 = SongNode("Uptown Funk")
node3.next = node2
top_hits_2010s = node3
print_linked_list(top_hits_2010s)

# Problem 2: Top Artists
# Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.

# Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def get_artist_frequency(playlist):
    artists = {}
    current = playlist

    while current:
        artist = current.artist
        if artist in artists:
            artists[artist] += 1
        else:
            artists[artist] = 1
        current = current.next
    print(artists)

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

get_artist_frequency(playlist)

# Problem 3: Glitching Out
# The following code attempts to remove the first node with a given song from a singly linked list with head playlist_head but it contains a bug!

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))

# Problem 4: On Repeat
# A variation of the two-pointer technique introduced in previous units is to have a slow and a fast pointer that increment at different rates.

# We would like to check whether our playlist loops or not. Given the head of a linked list playlist_head, return True if the playlist has a cycle in it and False otherwise. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

def on_repeat(playlist_head):
    fast_p = playlist_head.next
    slow_p = playlist_head

    while slow_p.next or fast_p.next:
        if fast_p == slow_p:
            return True
        slow_p = slow_p.next
        if not fast_p.next or not fast_p.next.next:
            return False
        fast_p = fast_p.next.next

song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
#song4.next = song2

print(on_repeat(song1))

def loop_length(playlist_head):
    fast_p = playlist_head.next
    slow_p = playlist_head
    count = 0

    while slow_p.next or fast_p.next:
        if fast_p == slow_p:
            save_p = slow_p
            slow_p = slow_p.next
            count += 1
            while not slow_p == save_p:
                slow_p = slow_p.next
                count += 1
            return count
        slow_p = slow_p.next
        if not fast_p.next or not fast_p.next.next:
            return 0
        fast_p = fast_p.next.next

song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))