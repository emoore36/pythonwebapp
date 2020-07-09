class Skill:

    Proficiency: bool
    Number: int
    Name: str
    Ability: str    

    def __init__(self, proficiency=False, number=0, name="", ability=""):
        self.Proficiency = proficiency
        self.Number = number
        self.Name = name
        self.Ability = ability
    
    def __init__(self, name='', ability=''):
        self.Proficiency=False
        self.Number = 0
        self.Name = name
        self.Ability = ability

    
    def data(self):
        return {"Proficiency": self.Proficiency, "Number": self.Number, "Name": self.Name, "Ability": self.Ability }


class SkillList:

    
    Acrobatics: Skill
    Animal_Handling: Skill
    Arcana: Skill
    Athletics: Skill
    Deception: Skill
    History: Skill
    Insight: Skill
    Investigation: Skill
    Medicine: Skill
    Nature: Skill
    Perception: Skill
    Performance: Skill
    Persuasion: Skill
    Religion: Skill
    Sleight_of_Hand: Skill
    Stealth: Skill
    Survival: Skill

    def __init__(self, acrobatics=Skill("Acrobatics", "DEX"), animal_handling=Skill("Animal Handling", "WIS"), arcana=Skill("Arcana", "INT"), athletics=Skill("Athletics", "STR"), deception=Skill("Deception", "CHA"), history=Skill("History", "INT"), insight=Skill("Insight", "WIS"), investigation=Skill("Investigation", "INT"), medicine=Skill("Medicine", "WIS"), nature=Skill("Nature", "WIS"), perception=Skill("Perception", "WIS"),performance=Skill("Performance", "CHA"), persuasion=Skill("Persuasion", "CHA"), religion=Skill("Religion", "INT"), sleight_of_hand=Skill("Sleight of Hand", "DEX"), stealth=Skill("Stealth", "DEX"), survival=Skill("Survival", "WIS")):
        self.Acrobatics = acrobatics
        self.Animal_Handling = animal_handling
        self.Arcana = arcana
        self.Athletics = athletics
        self.Deception = deception
        self.History = history
        self.Insight = insight
        self.Investigation = investigation
        self.Medicine = medicine
        self.Nature = nature
        self.Perception = perception
        self.Performance = performance
        self.Persuasion = persuasion
        self.Religion = religion
        self.Sleight_of_Hand = sleight_of_hand
        self.Stealth = stealth
        self.Survival = survival

    def data(self):
        return { 
            "Acrobatics": self.Acrobatics.data(), 
            "Animal Handling": self.Animal_Handling.data(), 
            "Arcana": self.Arcana.data(), 
            "Athletics": self.Athletics.data(), 
            "Deception": self.Deception.data(), 
            "History": self.History.data(), 
            "Insight": self.Insight.data(), 
            "Investigation": self.Investigation.data(), 
            "Medicine": self.Medicine.data(), 
            "Nature": self.Nature.data(), 
            "Perception": self.Perception.data(), 
            "Performance": self.Performance.data(), 
            "Persuasion": self.Persuasion.data(), 
            "Religion": self.Religion.data(), 
            "Slight of Hand": self.Sleight_of_Hand.data(), 
            "Stealth": self.Stealth.data(), 
            "Survival": self.Survival.data() }

    


        