from models.AbilityScoreList import AbilityScoreList
import random, json

class Character:

    Name: str
    Race: str
    Class: str
    Scores: AbilityScoreList
    Background: str

    def __init__(self, name="", race="", charClass="", scores=AbilityScoreList(0,0,0,0,0,0), background=""):
        self.Name = name
        self.Race = race
        self.Class = charClass
        self.Scores = scores
        self.Background = background

    def print(self):
        return str.format("Character: Name: {}, Race: {}, Class: {}, Scores: {}, Background: {}", self.Name, self.Race, self.Class, self.Scores.print(), self.Background)

    def generateID(self):
        chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        finalStr = ""
        rand = random.Random()
        for x in range(16):
            finalStr += chars[rand.randint(0, len(chars) - 1)]
        
        return finalStr

    def data(self):
        return { "name": self.Name, "race": self.Race, "class": self.Class, "scores": self.Scores.data(), "background": self.Background}