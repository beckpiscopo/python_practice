# TODO Create an empty list to maintain the player names
roster = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'

add_players = input("Would you like to add a player to the list? (y/n)  ")
while add_players.lower() == "yes":
    name = input("What's the player's name?  ")
    roster.append(name)
    add_players = input(
        "Would you like to add another player to the list? (y/n)  ")

# TODO print the number of players on the team
print("There are {} players on the team.".format(len(roster)))

# TODO Print the player number and the player name
# The player number should start at the number one
player_number = 1
for player in roster:
    print("player {}: {}".format(player, player_number))
    player_number += 1


# TODO Select a goalkeeper from the above roster
keeper = input(
    "Please select a goal keeper by selecting player number. (1 - {})  ".format(len(roster)))
keeper = int(keeper)

# TODO Print the goal keeper's name
# Remember that lists use a zero based index

print("The goalkeeper's names is {}".format(roster[keeper - 1]))
