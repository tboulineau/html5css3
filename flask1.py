from flask import Flask, render_template, request
import json

app = Flask(__name__,static_folder=".",static_url_path='',template_folder='.')

@app.route('/') # première page où l'utilisateur saisit ses préférences
def home():
  return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
  return "Hello : %s" % thing
  
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
    #print(data)
  #print(data)
  for question in data["animaux"]:
    print(question["question"])

  # Accéder à l'attribut "question"*
  #print("ANINAMUXNLFKJSLFKJQSDMLDFKQHSFDLM")
  #print(data["animaux"])
  #for question in data["animaux"]:
  #    print(question["question"])
    
  question = data["animaux"][0]["question"]
  reponse1 = data["animaux"][0]["options"][0]
  reponse2 = data["animaux"][0]["options"][1]
  reponse3 = data["animaux"][0]["options"][2]
  reponse4 = data["animaux"][0]["options"][3]

  return render_template('question_template.html',
                         question=question,
                         reponse1=reponse1,
                         reponse2=reponse2,
                         reponse3=reponse3,
                         reponse4=reponse4)
  #return render_template('quiz_json.html',nombre=nombre,apellido=apellido)

if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')