from flask.globals import request
from flask import Flask, render_template, redirect
from todo_app.trello.trello_api import TrelloAPI
from todo_app.view_models.trello_view_model import TrelloViewModel 


app = Flask(__name__, template_folder="templates")

@app.route("/", methods=['GET', 'POST'])
def index():
    item_view_model = TrelloViewModel(TrelloAPI.get_all_trello_items())  
    return render_template('index.html', view_model=item_view_model)

@app.route("/complete_item/<string:id>")
def complete_item(id):
    TrelloAPI.markid_item_done(id)
    return redirect('/')

@app.route("/uncomplete_item/<string:id>")
def uncomplete_item(id):
    TrelloAPI.markid_item_undone(id)
    return redirect('/')

@app.route("/add_todo_item", methods=['GET', 'POST'])
def add_todo_item():
    new_todo_item = request.form.get('new_todo_item')
    if isvalid(new_todo_item):
        TrelloAPI.add_item(new_todo_item)
    return redirect('/')

def isvalid(new_todo_item):
    return len(new_todo_item) != 0

if __name__ == '__main__':
    app.run()
