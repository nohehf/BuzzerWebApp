import sys #on setup les différents paths (c un peu le bordel)
try:
    from lib.WebHook import buzz_webhook_send
except:
    from WebHook import buzz_webhook_send

class Player():
    def __init__(self, name, sid):
        self.name = name
        self.sid = sid

    def buzz(self):
        print(f'Player "{self.name}" Buzzed')
        buzz_webhook_send(self.name)



def addToPlayerLDict (player, playerDict):

    pass




if __name__ == "__main__":
    playersDict = []
    playerJson = {
        "name": "nohz"
    }
    timote = Player('timote','0')
    timote.buzz()
    
    pass
