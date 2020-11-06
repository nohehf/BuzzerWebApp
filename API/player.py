class player():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def buzz(self):
        print(f'Player "{self.name}" Buzzed')

playersList = []

if __name__ == "__main__":
    timote = player('timote','000')
    timote.buzz()
    
    pass
