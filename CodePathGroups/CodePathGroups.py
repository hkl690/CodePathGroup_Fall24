#   live share link:
#   https://prod.liveshare.vsengsaas.visualstudio.com/join?97E9181CCA5EF950A773E31C93577CA37AE9


print("hello")


# Problem 1: Festival Lineup
# Given two lists of strings artists and set_times of length n, write a function lineup() 
# that maps each artist to their set time.

# An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

def lineup(artists, set_times):
    schedule = zip(artists, set_times)
    return dict(schedule)


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

# Example Output:
# {"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}
# {}



# Problem 2: Planning App
# You are designing an app for your festival to help attendees have the best experience possible! 
# As part of the application, users will be able to easily search their favorite artist and find out the day, 
# time, and stage the artist is playing at. Write a function get_artist_info() that accepts a string artist 
# and a dictionary festival_schedule mapping artist's names to dictionaries containing the day, time, 
# and stage they are playing on. Return the dictionary containing the information about the given artist.

# If the artist searched for does not exist in festival_schedule, 
# return the dictionary {"message": "Artist not found"}.

def get_artist_info(artist, festival_schedule):
    not_found = {"message": "Artist not found"}
    if artist not in festival_schedule:
        return not_found
    else:
        return festival_schedule.get(artist)


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
# Example Output:
# {'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}
# {'message': 'Artist not found'}