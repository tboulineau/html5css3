from flask import Flask, render_template, request
import json
import random

app = Flask(__name__,static_folder=".",static_url_path='',template_folder='.')

@app.route('/') # première page où l'utilisateur saisit ses préférences
def home():
  return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
  return "Hello : %s" % thing

@app.route('/quizanimaux')
def quiztestanimaux():
  return render_template('quiztestanimaux.html')
  
@app.route('/quiz')
def quiz():
  if request.method == 'POST':
    difficulte = request.form['difficulte']
    theme = request.form['theme']
  else:
    difficulte = request.args.get('difficulte')
    theme = request.args.get('theme')

  with open("questions.json","r", encoding='utf-8') as fichier:
    data = json.load(fichier)

  # Accéder à l'attribut "question"*
  #print("ANINAMUXNLFKJSLFKJQSDMLDFKQHSFDLM")
  #print(data["animaux"])
  #for question in data["animaux"]:
  #    print(question["question"])
    
  questions = []
  reponses = []
  corrections = []
  '''
  print("affichage test")
  for i in range(0, 4):
     print("question " + str(i) + " : " + data["animaux"][i]["question"])
     print("reponses " + str(i) + " : " + str(data["animaux"][i]["options"]))
  '''

  valeurs = random.sample(range(0, len(data["animaux"])), 3)

  for i in valeurs:
     questions.append(data["animaux"][i]["question"])
     reponses.append(data["animaux"][i]["options"])
     corrections.append(data["animaux"][i]["answer"])

  #print("questions : " + str(questions))
  #print("réponses : " + str(reponses))
  
  return render_template('question_template.html',
                         questions = json.dumps(questions),
                         reponses = json.dumps(reponses),
                          correction = json.dumps(corrections))

if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')