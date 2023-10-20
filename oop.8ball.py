import random

class Dice:
    def __init__(self, responses):
        self.responses = responses
        
    def roll(self):
        return random.choice(list(self.responses.keys()))
    
dice = Dice({'1': 'nope', '2' :'i mean i guess', '3' :'if the sky turns into an apple then yes', '4' : 'yeahhhhhhhhhhh no', '5' : 'oh goddness no', '6' : 'sure?', '7' : 'try again', '8' : 'why are you asking an object?', '9' :'YESSSSS', '10' : 'YAHHHHHHH ABSOLUTLY', '11' : "yes", '12' : 'no', '13' : 'maybe', '14' :'if you have hiccups rn then yes', '15' :'im on break', '16' :'as long as your favorite color isnt blue then yes', '17' :'umm its up to you', '18' :"don't ask me", '19' :'yes if your on an airplane', '20' :'no if you went swimming today'})
print(dice.roll())