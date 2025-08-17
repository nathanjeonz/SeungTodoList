import flask
import json

def load_tasks():
    try:
        with open("todos.json") as file:
            res = json.load(file)
            return res['todos']
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("todos.json", "w") as file:
        json.dump({"todos": tasks}, file)

app = flask.Flask(__name__)



@app.route('/')
def home():
    tasks = load_tasks()
    return flask.render_template('index.html',seung_task=tasks)

@app.route('/submit',methods=['POST'])
def submitf():
    todo = flask.request.form['entertodo']
    tasks = load_tasks()
    tasks.append(todo)
    save_tasks(tasks)
    
    return flask.redirect('/')

@app.route('/delete/<int:index>',methods=['POST'])
def remove(index):
    tasks = load_tasks()
    tasks.pop(index)
    save_tasks(tasks)

    return flask.redirect('/')



if __name__ == '__main__':
    app.run(debug=True)