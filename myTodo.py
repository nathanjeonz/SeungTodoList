import flask




app = flask.Flask(__name__)

tasks = ['i have to go to school','i have to sleep 10pm sharp','i have to complete my homework']

@app.route('/')
def home():
    return flask.render_template('index.html',seung_task=tasks)

@app.route('/submit',methods=['POST'])
def submitf():
    todo = flask.request.form['entertodo']
    tasks.append(todo)
    return flask.redirect('/')

@app.route('/delete/<int:index>',methods=['POST'])
def remove(index):
    tasks.pop(index)
    return flask.redirect('/')



if __name__ == '__main__':
    app.run(debug=True)