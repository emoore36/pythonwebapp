class AbilityScoreList:
    # Strength = 0
    # Dexterity = 0
    # Constitution = 0
    # Intelligence = 0
    # Wisdom = 0
    # Charisma = 0

    def __init__(self, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0):
        self.Strength = strength
        self.Dexterity = dexterity
        self.Constitution = constitution
        self.Intelligence = intelligence
        self.Wisdom = wisdom
        self.Charisma = charisma

    def print(self):
        return str.format("AbilityScoreList: STR: {}, DEX: {}, CON: {}, INT: {}, WIS: {}, CHA: {}", self.Strength, self.Dexterity, self.Constitution, self.Intelligence, self.Wisdom, self.Charisma)

    def data(self):
        return {"STR": self.Strength, "DEX": self.Dexterity, "CON": self.Constitution, "INT": self.Intelligence, "WIS": self.Wisdom, "CHA": self.Charisma}