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

  with open("questions.json","r+") as fichier:
    json.load(fichier)

  return render_template('quiz_json.html', question="question", answer="answer", options="options")
  #return render_template('quiz_json.html',nombre=nombre,apellido=apellido)

if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')