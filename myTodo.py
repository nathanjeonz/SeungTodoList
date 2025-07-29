import flask




app = flask.Flask(__name__)

tasks = ['i have to go to school','i have to sleep 10pm sharp','i have to complete my homew']

@app.route('/')
def home():
    return flask.render_template('index.html',seung_task=tasks)



@app.route('/seung')
def hello():
    return 'hello'

@app.route('/umair')
def bye():
    return 'bye'


app.run(debug=True)