import sys #on setup les différents paths (c un peu le bordel)
import os
current_path = os.getcwd()
split = current_path.split('\\')
split.pop()
split.append('Discord_Bot')
discord_folder_path = '\\'.join(split)
sys.path.append(discord_folder_path)
from WebHook import buzz_webhook_send

class Player():
    def __init__(self, name):
        self.name = name

    def buzz(self):
        print(f'Player "{self.name}" Buzzed')
        buzz_webhook_send(self.name,discord_folder_path)



def addToPlayerLDict (player, playerDict):

    pass




if __name__ == "__main__":
    playersDict = []
    playerJson = {
        "name": "nohz"
    }
    timote = Player('timote')
    timote.buzz()
    
    pass
