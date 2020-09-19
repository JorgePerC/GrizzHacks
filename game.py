import json
from random import randint

#           _____                _____                    _____                _____                    _____          
#          /\    \              /\    \                  /\    \              /\    \                  /\    \         
#         /::\    \            /::\    \                /::\    \            /::\    \                /::\    \        
#        /::::\    \           \:::\    \              /::::\    \           \:::\    \              /::::\    \       
#       /::::::\    \           \:::\    \            /::::::\    \           \:::\    \            /::::::\    \      
#      /:::/\:::\    \           \:::\    \          /:::/\:::\    \           \:::\    \          /:::/\:::\    \     
#     /:::/__\:::\    \           \:::\    \        /:::/__\:::\    \           \:::\    \        /:::/__\:::\    \    
#     \:::\   \:::\    \          /::::\    \      /::::\   \:::\    \          /::::\    \       \:::\   \:::\    \   
#   ___\:::\   \:::\    \        /::::::\    \    /::::::\   \:::\    \        /::::::\    \    ___\:::\   \:::\    \  
#  /\   \:::\   \:::\    \      /:::/\:::\    \  /:::/\:::\   \:::\    \      /:::/\:::\    \  /\   \:::\   \:::\    \ 
# /::\   \:::\   \:::\____\    /:::/  \:::\____\/:::/  \:::\   \:::\____\    /:::/  \:::\____\/::\   \:::\   \:::\____\
# \:::\   \:::\   \::/    /   /:::/    \::/    /\::/    \:::\  /:::/    /   /:::/    \::/    /\:::\   \:::\   \::/    /
#  \:::\   \:::\   \/____/   /:::/    / \/____/  \/____/ \:::\/:::/    /   /:::/    / \/____/  \:::\   \:::\   \/____/ 
#   \:::\   \:::\    \      /:::/    /                    \::::::/    /   /:::/    /            \:::\   \:::\    \     
#    \:::\   \:::\____\    /:::/    /                      \::::/    /   /:::/    /              \:::\   \:::\____\    
#     \:::\  /:::/    /    \::/    /                       /:::/    /    \::/    /                \:::\  /:::/    /    
#      \:::\/:::/    /      \/____/                       /:::/    /      \/____/                  \:::\/:::/    /     
#       \::::::/    /                                    /:::/    /                                 \::::::/    /      
#        \::::/    /                                    /:::/    /                                   \::::/    /       
#         \::/    /                                     \::/    /                                     \::/    /        
#          \/____/                                       \/____/                                       \/____/         


class stats:
    def __init__(self, money : int = 0, trust : int = 0, political : int = 0, social : int = 0, environmental : int = 0, economic : int = 0):
        '''
        a container of information for the 6 game stats:
        money 
        trust 
        political 
        social 
        enviormental 
        economic
        '''
        self.money = money
        self.trust = trust
        self.political = political
        self.social = social
        self.environmental = environmental
        self.economic = economic
    
    def returnArray(self):
        '''
        makes array of stats:
        money 
        trust 
        political 
        social 
        enviormental 
        economic

        and returns them in same order
        '''
        toReturn = []
        toReturn.append(self.money)
        toReturn.append(self.trust)
        toReturn.append(self.political)
        toReturn.append(self.social)
        toReturn.append(self.environmental)
        toReturn.append(self.economic)

        return toReturn

    def loadFromArray(self, array : list):
        '''
        makes from array of stats:
        money 
        trust 
        political 
        social 
        enviormental 
        economic

        into seperate variables inside of object
        '''
        self.money = array[0]
        self.trust = array[1]
        self.political = array[2]
        self.social = array[3]
        self.environmental = array[4]
        self.economic = array[5]
    
    def addStuff(self, toAdd):
        '''
        add the toAdd stats object into self.

        toAdd -> stats(Object)
        '''
        self.money += toAdd.money
        self.trust += toAdd.trust
        self.political += toAdd.political
        self.social += toAdd.social
        self.environmental += toAdd.environmental
        self.economic += toAdd.economic

#           _____                    _____                    _____                    _____          
#          /\    \                  /\    \                  /\    \                  /\    \         
#         /::\    \                /::\    \                /::\____\                /::\    \        
#        /::::\    \              /::::\    \              /::::|   |               /::::\    \       
#       /::::::\    \            /::::::\    \            /:::::|   |              /::::::\    \      
#      /:::/\:::\    \          /:::/\:::\    \          /::::::|   |             /:::/\:::\    \     
#     /:::/  \:::\    \        /:::/__\:::\    \        /:::/|::|   |            /:::/__\:::\    \    
#    /:::/    \:::\    \      /::::\   \:::\    \      /:::/ |::|   |           /::::\   \:::\    \   
#   /:::/    / \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______    /::::::\   \:::\    \  
#  /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \  /:::/\:::\   \:::\    \ 
# /:::/____/  ___\:::|    |/:::/  \:::\   \:::\____\/:::/    |:::::::::\____\/:::/__\:::\   \:::\____\
# \:::\    \ /\  /:::|____|\::/    \:::\  /:::/    /\::/    / ~~~~~/:::/    /\:::\   \:::\   \::/    /
#  \:::\    /::\ \::/    /  \/____/ \:::\/:::/    /  \/____/      /:::/    /  \:::\   \:::\   \/____/ 
#   \:::\   \:::\ \/____/            \::::::/    /               /:::/    /    \:::\   \:::\    \     
#    \:::\   \:::\____\               \::::/    /               /:::/    /      \:::\   \:::\____\    
#     \:::\  /:::/    /               /:::/    /               /:::/    /        \:::\   \::/    /    
#      \:::\/:::/    /               /:::/    /               /:::/    /          \:::\   \/____/     
#       \::::::/    /               /:::/    /               /:::/    /            \:::\    \         
#        \::::/    /               /:::/    /               /:::/    /              \:::\____\        
#         \::/____/                \::/    /                \::/    /                \::/    /        
#                                   \/____/                  \/____/                  \/____/         

class mainGameMannager:
    def __init__(self):
        '''
        mannages the internal game. 
        All backend calculations should be done here!
        '''
        self.allJSONids = []
        self.questionaireJSONids = []
        self.playerValues = stats()
        self.current = None
        self.all = self.loadAllJSON() # start with a JSON
        self.questionaire = None
        self.questions = 0
        self.currentCuestionNumber = 0
        self.calcStats = stats()

    def loadRandomJSON(self):
        '''
        loads a random JSON from self.all.

        returns 2 variables:
            title -> str
            questions -> array(one element per possible answer).
                each element of the array has 4 parts, [ID, question string, type(select/input), mods(class type stats)]
        
        '''
        if self.questionaire == None:
            print('there is no info to use...')
            return False
        else:
            if len(self.questionaire) == 0:
                # codigo por si acaso queremos agregar otra cosa
                return 'no more questions', self.playerValues.returnArray() # podemos regresar calculos aqui!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            questionToRemove = self.questionaireJSONids.pop(randint(0,len(self.questionaireJSONids)-1))
            self.current = self.questionaire.pop(questionToRemove) # cambiar a otro
            questions = []
            for name in self.current:
                if name == 'question':
                    title = self.current[name]
                else:
                    questions.append([name, self.current[name]['answer'], self.current[name]['type'], self.current[name]['mods']])

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

        self.allJSONids = []
        for JSONid in data:
            self.allJSONids.append(JSONid)
        
        return data

    def startGame(self, amountOfQuestions : int):
        '''
        chooses random questions from master JSON, and stores them in questionaire
        the amount of questions it chooses is defined by amountOfQuestions
        '''
        # first, select things
        self.questionaire = {}
        self.questionaireJSONids = []

        for i in range(amountOfQuestions):
            idToAppend = self.allJSONids.pop(randint(0,len(self.allJSONids)-1))
            toAppend = self.all.pop(idToAppend)
            self.questionaire[idToAppend] = toAppend
            self.questionaireJSONids.append(idToAppend)
            print(idToAppend)
        
        # second, choose a random one
        print(self.questionaireJSONids)
        return self.loadRandomJSON()

    def updateMetricsAndReturnNext(self, metrics : list = [0,0,0,0,0,1]):
        '''
        adds metrics into playerValues

        returns randomJSON
        if no more JSON files are in current play session, returns 'no more questions', playerValues as array
        '''
        self.calcStats.loadFromArray(metrics)
        self.playerValues.addStuff(self.calcStats)

        return game.loadRandomJSON()

game = mainGameMannager()

print(game.startGame(2))
print(game.updateMetricsAndReturnNext())
print(game.updateMetricsAndReturnNext())