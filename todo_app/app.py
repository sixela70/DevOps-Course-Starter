from flask.globals import request
from todo_app.data.session_items import add_item, get_items, mark_item_done, mark_item_not_done
from flask import Flask, render_template, redirect
from todo_app.flask_config import Config

app = Flask(__name__,template_folder="templates")
app.config.from_object(Config)


@app.route("/", methods=['GET', 'POST'])
def index():
        return render_template('index.html',items=get_items()) 

@app.route("/additem", methods=['GET', 'POST'])
def additem():
    print(request.form)
    new_todo_item = request.form.get('new_todo_item')
    if isvalid(new_todo_item):
        add_item(new_todo_item)
    return redirect('/')

@app.route("/update", methods=['GET', 'POST'])
def update():
    print(request.form)
    new_todo_item = request.form.get('new_todo_item')
    if isvalid(new_todo_item):
        add_item(new_todo_item)
    updateDoneStatus()
    return redirect('/')

def updateDoneStatus():
    items = get_items()
    for item in items:
        print(item['id'] )
        ischeckedkey = "to_do_chk_"+str(item['id']) 
        if request.form.get(ischeckedkey):
            mark_item_done(item)
        else:
            mark_item_not_done(item)

def isvalid( new_todo_item):
    return len(new_todo_item) != 0

if __name__ == '__main__':
    app.run()
