class mainGameMannager:
    def __init__(self):
        self.money = 0
        self.points = {
            'trust': 0,
            'political': 0, 
            'social' : 0,
            'environmental' : 0,
            'economic' : 0
        }
        self.current = None

    def leadIndependentJSON(self, JSONfile):
        self.current = JSONfile



