import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    new_game_library = json_data["GameLibrary"]

    #Loop through the json_data
    for game in new_game_library:
        platforms = game["Platform"]

        c_platform = test_data.Platform()
        for platform in platforms:
            c_platform.name = platform["Name"]
            c_platform.launch_year = platform["Launch_Year"]


        new_game = test_data.Game(game["Title"],c_platform, game["Year"])
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
        game_library.add_game(new_game)
    ### End Add Code Here ###
    return game_library


#Part 2
json_file_name = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
with open(json_file_name, "r") as reader:
    # Use the json module to load the data from the file
    game_library_json_data = json.load(reader)
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
gameLibrary = make_game_library_from_json(game_library_json_data)
#Print out the resulting GameLibrary data using print()
print(gameLibrary)
### End Add Code Here ###
