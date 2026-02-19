from pybaseball import playerid_lookup

# Look up a player (Last Name, First Name)
# It is not case-sensitive, but spelling matters
player = playerid_lookup('miller', 'mason')

# Display the result
print(player)