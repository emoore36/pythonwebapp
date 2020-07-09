from flask import Blueprint, render_template, request
from models.Character import Character
from models.AbilityScoreList import AbilityScoreList
from util.AbilityScoreUpdater import AbilityScoreUpdater
from models.SkillList import SkillList

print = Blueprint(__name__, __name__, template_folder='templates')

@print.route('/create', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':

        charName = request.form.get('name')
        charRace = request.form.get('race')
        charClass = request.form.get('class')

        charStr = int(request.form.get('str'))
        charDex = int(request.form.get('dex'))
        charCon = int(request.form.get('con'))
        charInt = int(request.form.get('int'))
        charWis = int(request.form.get('wis'))
        charCha = int(request.form.get('cha'))
        abilityScores = AbilityScoreList(charStr, charDex, charCon, charInt, charWis, charCha)
        skills = SkillList()

        charBack = request.form.get('background')

        formChar = Character(charName, charRace, charClass, abilityScores, skills, charBack)
        
        updater = AbilityScoreUpdater()
        updater.update(formChar)

        return str(formChar.data())

        file = open('pythonwebapp/characters/{}.dndchar'.format(formChar.generateID()), "w")
        file.write(str(formChar.data()))
        file.close()
    
        return "Character created successfully."
        
    return render_template("create.html")