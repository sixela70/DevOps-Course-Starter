from flask.globals import request
from todo_app.data.session_items import add_item, get_items
from flask import Flask, render_template
from todo_app.flask_config import Config

app = Flask(__name__,template_folder="templates")
app.config.from_object(Config)


@app.route("/", methods=['GET', 'POST'])
def index():
    if "add_todo_item" in request.form:
        return "additem"
    else:
        return render_template('index.html',items=get_items()) 

@app.route("/additem", methods=['GET', 'POST'])
def additem():
    print(request.form)
    new_todo_item = request.form.get('new_todo_item')
    if isvalid(new_todo_item):
        add_item(new_todo_item)
    return render_template('index.html',items=get_items()) 

def isvalid( new_todo_item):
    return len(new_todo_item) != 0

if __name__ == '__main__':
    app.run()
