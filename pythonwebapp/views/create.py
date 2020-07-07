from flask import Blueprint, render_template, request
from pythonwebapp.models.Character import Character
from pythonwebapp.models.AbilityScoreList import AbilityScoreList

print = Blueprint(__name__, __name__, template_folder='templates')

@print.route('/create', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        formChar = Character(request.form.get('name'), request.form.get('race'), request.form.get('class'), AbilityScoreList(request.form.get('str'),request.form.get('dex'),request.form.get('con'),request.form.get('int'),request.form.get('wis'),request.form.get('cha')), request.form.get('background'))
        

        file = open('pythonwebapp/characters/{}.dndchar'.format(formChar.generateID()), "w")
         
        file.write(str(formChar.data()))


        file.close()
    
        return "Character created successfully."
        
        
        
        


    return render_template("create.html")