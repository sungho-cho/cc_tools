import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
    for game_data in json_data["games"]:
        #Create a new Game object from the json_data by reading
        game = test_data.Game()
        #  title
        game.title = game_data["title"]
        #  year
        game.year = game_data["year"]
        #  platform (which requires reading name and launch_year)
        game.platform = test_data.Platform()
        game.platform.name = game_data["platform"]["name"]
        game.platform.launch_year = game_data["platform"]["launch year"]
        #Add that Game object to the game_library
        game_library.add_game(game)
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
with open(input_json_file, "r") as reader:
    #Use the json module to load the data from the file
    data = json.load(reader)
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
result = make_game_library_from_json(data)
#Print out the resulting GameLibrary data using print()
print(result)
### End Add Code Here ###
