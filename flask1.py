from flask import Flask 

app = Flask(__name__,static_folder=".",static_url_path='')

@app.route('/')
def home():
  return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
  return "Hello : %s" % thing
  
@app.route('/quiz')
def quiz():
  return app.send_static_file('quiz_json.html')

app.run(port=8080, debug=True)