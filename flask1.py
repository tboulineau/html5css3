from flask import Flask, render_template, request, make_response
import json
import random
import os

app = Flask(__name__,static_folder=".",static_url_path='',template_folder='.')

@app.route('/') # première page où l'utilisateur saisit ses préférences
def home():
  resp = make_response(render_template('index.html'))
  resp.set_cookie("score", '0')
  return resp
  # return app.send_static_file('index.html')

@app.route('/fin')
def fin():
  '''
  if request.method == 'POST':
    score = request.form['score']
  else:
    score = request.args.get('score')
  '''
  return render_template('fin.html')

@app.route('/enregistrer', methods=['GET', 'POST'])
def enregistrer():
  nom = ""
  score = ""
  temps = ""
  if request.method == 'POST':
    nom = request.form['nom']
    score = request.cookies.get("score")
    temps = request.cookies.get("temps")
  else:
    nom = request.args.get('nom')
    score = request.cookies.get("score")
    temps = request.cookies.get("temps")
  if nom != "" and score != "" and temps != "":
    with open("scores.txt", "r+") as fichier_scores:
      fichier_scores.seek(0, os.SEEK_END)
      fichier_scores.write(nom+"\t"+score+"\t"+temps+"\n")
      fichier_scores.close()
  else:
    print("Erreur enregistrement")
    print("nom : " + nom)
    print("score : " + score)
    print("temps : " + temps)
  return render_template('confirmation.html')


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
      return app.send_static_file('index.html')
  
  with open(fichierJSON,"r", encoding='utf-8') as fichier:
    data = json.load(fichier)
    
  questions = []
  reponses = []
  corrections = []

  print(difficulte)
  match difficulte:
    case "debutant":
      indice=0
    case "intermediaire":
      indice=1
    case "confirme":
      indice=2
  
  valeurs = random.sample(range(0, len(data["content"][indice])), 3)

  for i in valeurs:
    questions.append(data["content"][indice][i]["question"])
    reponses.append(data["content"][indice][i]["options"])
    corrections.append(data["content"][indice][i]["answer"])
  
  return render_template('question_template.html',
                         questions = json.dumps(questions),
                         reponses = json.dumps(reponses),
                         corrections = json.dumps(corrections))

if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')