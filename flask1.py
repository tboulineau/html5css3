from flask import Flask, render_template 

app = Flask(__name__,static_folder=".",static_url_path='')

@app.route('/')
def home():
  return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
  return "Hello : %s" % thing
  
@app.route('/quiz')
def quiz():
  return render_template('quiz_json.html',question="question",options="opitons",
                         answer="answer")


app.run(port=8080, debug=True)