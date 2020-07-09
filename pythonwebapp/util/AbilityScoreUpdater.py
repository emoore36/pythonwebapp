from models.Character import Character
from models.AbilityScoreList import AbilityScoreList

class AbilityScoreUpdater:

    def __init__(self):
        super().__init__()

    def update(self, char=Character()):
        race:str = char.Race
        scores:AbilityScoreList = char.Scores
        
        # let's start with race
        if race.__contains__("hill_dwarf"):
            print(str.format("Contitution is {}"), scores.Constitution)
            exit()
            scores.Constitution += 2
            scores.Wisdom += 1
        if race.__contains__("mountain_dwarf"):
            scores.Constitution += 2
            scores.Strength += 2
        if race.__contains__("high_elf"):
            scores.Dexterity += 2
            scores.Intelligence += 1
        if race.__contains__("wood_elf"):
            scores.Dexterity += 2
            scores.Wisdom += 1
        if race.__contains__("drow"):
            scores.Dexterity += 2
            scores.Charisma += 1
        if race.__contains__("lightfoot_halfling"):
            scores.Dexterity += 2
            scores.Charisma += 1
        if race.__contains__("stout_halfling"):
            scores.Dexterity += 2
            scores.Constitution += 1
        if race.__contains__("human"):
            scores.Strength += 1
            scores.Dexterity += 1
            scores.Constitution += 1
            scores.Intelligence += 1
            scores.Wisdom += 1
            scores.Charisma += 1
        if race.__contains__("dragonborn"):
            scores.Strength += 2
            scores.Charisma += 1
        if race.__contains__("forest_gnome"):
            scores.Intelligence += 2
            scores.Dexterity += 1
        if race.__contains__("rock_gnome"):
            scores.Intelligence += 2
            scores.Constitution += 1
        if race.__contains__("half-elf"):
            scores.Charisma += 2
        if race.__contains__("half-orc"):
            scores.Strength += 2
            scores.Constitution += 1
        if race.__contains__("tiefling"):
            scores.Charisma += 2
            scores.Intelligence += 1

        return char



