from models.AbilityScoreList import AbilityScoreList
from models.SkillList import SkillList
import random, json

class Character:

    Name: str
    Race: str
    Class: str
    Scores: AbilityScoreList
    Skills: SkillList
    Background: str

    def __init__(self, name="", race="", charClass="", scores=AbilityScoreList(), skills=SkillList(), background=""):
        self.Name = name
        self.Race = race
        self.Class = charClass
        self.Scores = scores
        self.Skills = skills
        self.Background = background

    def generateID(self):
        chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        finalStr = ""
        rand = random.Random()
        for x in range(16):
            finalStr += chars[rand.randint(0, len(chars) - 1)]
        
        return finalStr

    def data(self):
        return { "name": self.Name, "race": self.Race, "class": self.Class, "scores": self.Scores.data(), "skills": self.Skills.data(), "background": self.Background}