import json
from random import randint

class stats:
    def __init__(self, money : int = 0, trust : int = 0, political : int = 0, social : int = 0, environmental : int = 0, economic : int = 0):
        self.money = money
        self.trust = trust
        self.political = political
        self.social = social
        self.environmental = environmental
        self.economic = economic
    
    def returnArray(self):
        toReturn = []
        toReturn.append(self.money)
        toReturn.append(self.trust)
        toReturn.append(self.political)
        toReturn.append(self.social)
        toReturn.append(self.environmental)
        toReturn.append(self.economic)

        return toReturn

    def loadFromArray(self, array):
        self.money = array[0]
        self.trust = array[1]
        self.political = array[2]
        self.social = array[3]
        self.environmental = array[4]
        self.economic = array[5]
    
    def addStuff(self, toAdd):
        self.money += toAdd.money
        self.trust += toAdd.trust
        self.political += toAdd.political
        self.social += toAdd.social
        self.environmental += toAdd.environmental
        self.economic += toAdd.economic

class mainGameMannager:
    def __init__(self):
        self.playerValues = stats()
        self.current = None
        self.all = self.loadAllJSON()

    def loadRandomJSON(self):
        '''
        loads a random JSON from self.all.

        returns 2 variables:
            title -> str
            questions -> array(one element per possible answer).
                each element of the array has 4 parts, [ID, question string, type(select/input), mods(class type stats)]
        
        '''
        self.current = self.all['q{}'.format(randint(0,len(self.all)-1))]
        questions = []
        temp = stats()
        for name in self.current:
            if name == 'question':
                title = self.current[name]
            else:
                temp.loadFromArray(self.current[name]['mods'])
                questions.append([name, self.current[name]['answer'], self.current[name]['type'], temp])

        return title, questions

    def updateStats(self, statClass : stats):
        '''
        updates current player values
        '''
        self.playerValues.addStuff(statClass)

    def loadAllJSON(self):
        '''
        returns json as dictionary
        '''
        with open("static/data/levels.json") as f:
            data = json.load(f)
        
        return data

game = mainGameMannager()
game.updateStats(stats(1,2,3,4,5,6))
print(game.playerValues.returnArray())