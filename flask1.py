from flask import Flask, render_template, request
import json

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

  with open("questions.json","r") as fichier:
    data = json.load(fichier)

  # Accéder à l'attribut "question"*
  #print("ANINAMUXNLFKJSLFKJQSDMLDFKQHSFDLM")
  #print(data["animaux"])
  #for question in data["animaux"]:
  #    print(question["question"])
    
  questions = []
  reponses = []
  '''
  print("affichage test")
  for i in range(0, 4):
     print("question " + str(i) + " : " + data["animaux"][i]["question"])
     print("reponses " + str(i) + " : " + str(data["animaux"][i]["options"]))
  '''
  
  for i in range(0, 3):
     print(i)
     questions.append(data["animaux"][i]["question"])
     print(questions[i])
     reponses.append(data["animaux"][i]["options"])
     print(reponses[i])

  print("questions : " + str(questions))
  print("réponses : " + str(reponses))
  
  return render_template('question_template.html',
                         questions = questions,
                         reponses = reponses)

if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')