from flask.globals import request
from todo_app.data.trello_items import add_item, get_trello_list, mark_item_done, mark_item_not_done, markid_item_done, markid_item_undone
from flask import Flask, render_template, redirect

import requests

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html', items=get_trello_list())

@app.route("/complete_item/<string:id>")
def complete_item(id):
    markid_item_done(id)
    return redirect('/')

@app.route("/uncomplete_item/<string:id>")
def uncomplete_item(id):
    markid_item_undone(id)
    return redirect('/')

@app.route("/add_todo_item", methods=['GET', 'POST'])
def add_todo_item():
    print("Banana")
    print(request.form)
    new_todo_item = request.form.get('new_todo_item')
    if isvalid(new_todo_item):
        add_item(new_todo_item)
    return redirect('/')

def isvalid(new_todo_item):
    return len(new_todo_item) != 0

if __name__ == '__main__':
    app.run()
