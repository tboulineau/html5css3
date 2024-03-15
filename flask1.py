from flask import Flask, render_template, request
import json
import random
import os

app = Flask(__name__,static_folder=".",static_url_path='',template_folder='.')

@app.route('/') # première page où l'utilisateur saisit ses préférences
def home():
  return app.send_static_file('index.html')

@app.route('/fin')
def fin():
  if request.method == 'POST':
    score = request.form['score']
  else:
    score = request.args.get('score')

  return render_template('fin.html', score=score)

@app.route('/enregistrer',methods=['POST','GET'])
def enregistrer():
   if request.method == 'POST':
       nom = request.form['nom']
       score = request.form['score']
   else:
       nom = request.args.get('nom')
       score = request.args.get('score')
   if nom != "" and score != "":
    with open("scores.txt", "r+") as fichier_scores:
        fichier_scores.seek(0, os.SEEK_END)
        fichier_scores.write(nom+"\t"+score+"\n")
        fichier_scores.close()


@app.route('/quiz')
def quiz():
  if request.method == 'POST':
    difficulte = request.form['difficulte']
    theme = request.form['theme']
  else:
    difficulte = request.args.get('difficulte')
    theme = request.args.get('theme')

  print("Questionnaire commencé avec le thème : " + theme)

  match theme:
    case "avions":
      fichierJSON = "sujet_avions.json"
    case "animaux":
      fichierJSON = "sujet_animaux.json"
    case "cinema":
      fichierJSON = "sujet_cinema.json"
    case "geographie":
      fichierJSON = "sujet_geographie.json"
    case "politique":
      fichierJSON = "sujet_politique.json"
    case _:
      home()
  
  with open(fichierJSON,"r", encoding='utf-8') as fichier:
    data = json.load(fichier)
    
  questions = []
  reponses = []
  corrections = []

  valeurs = random.sample(range(0, len(data["content"])), 3)

  for i in valeurs:
     questions.append(data["content"][i]["question"])
     reponses.append(data["content"][i]["options"])
     corrections.append(data["content"][i]["answer"])
  
  return render_template('question_template.html',
                         questions = json.dumps(questions),
                         reponses = json.dumps(reponses),
                         corrections = json.dumps(corrections))

if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')