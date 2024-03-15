from flask import Flask, render_template, request
import json
import random

app = Flask(__name__,static_folder=".",static_url_path='',template_folder='.')

@app.route('/') # première page où l'utilisateur saisit ses préférences
def home():
  return app.send_static_file('index.html')
  
@app.route('/quiz')
def quiz():
  if request.method == 'POST':
    difficulte = request.form['difficulte']
    theme = request.form['theme']
  else:
    difficulte = request.args.get('difficulte')
    theme = request.args.get('theme')

  print("Questionnaire commencé avec le thème : " + theme)

  theme = "animaux"
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
                         correction = json.dumps(corrections))

if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')