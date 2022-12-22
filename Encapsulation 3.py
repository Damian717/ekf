class score():
    def __init__(self):
        self._score = 1
        
    def showscore(self):
        print(self._score)
        
    def update_score(self):
        self._score = self._score +1
        print(self._score)
        
player = score()
player.score = 100
player.update_score()
player.update_score()