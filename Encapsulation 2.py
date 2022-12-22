class score():
    def __init__(self):
        self.score = 1
        
    def showscore(self):
        print(self.score)
        
    def update_score(self):
        self.score = self.score +1
        print(self.score)
        
player = score()
player.score = 100
player.update_score()
player.update_score()