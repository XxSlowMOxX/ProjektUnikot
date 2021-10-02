import gameclassmo

class Command:

    name = "EMPTY"

    #Commands should be initialized with only the Gamestate
    def __init__(self, Game : gameclassmo.Game):
        self.Game = Game
        pass

    #Input the Data
    def create(self):
        return

    #Turns the Command into a String
    def serialize(self) -> str:
        return "EMPTY#"

    #Gets Data from a serialized String
    def deserialize(self, data : str):
        return

    #Handles the Command via Access of the Gamestate
    #This could return other Commands
    def handle(self) -> None:
        return