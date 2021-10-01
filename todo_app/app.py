import os
import requests
from todo_app.data.mongodb import MongoDb
from todo_app.data.user import User
from flask.globals import request
from flask import Flask, render_template, redirect, session, abort
from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user
from flask_login import current_user

from oauthlib.oauth2 import WebApplicationClient

from todo_app.view_models.view_model import ViewModel 

def create_app():
    app = Flask(__name__, template_folder="templates")

    disable_login = os.getenv('LOGIN_DISABLED')
    if disable_login:
      print("Github authentication disabled")
      app.config['LOGIN_DISABLED'] = True      

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    github_client_id = os.getenv('GITHIB_CLIENT_ID')
    github_secret_id = os.getenv('GITHUB_CLIENT_SECRET')
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    client = WebApplicationClient(github_client_id)

    @login_manager.unauthorized_handler
    def unauthenticated():
        authorize_endpoint = 'https://github.com/login/oauth/authorize'
        authorize_url = client.prepare_request_uri(authorize_endpoint, "http://127.0.0.1:5000/login/callback")
        return redirect(authorize_url)
    
    @login_manager.user_loader
    def load_user(user_id):
        user = MongoDb.get_user(user_id)
        return user
   
    @app.route('/login/callback', methods=['GET', 'POST'])
    def login_callback():                                                            
        # Get authorization code from github 
        code = request.args.get("code")
        token_url, headers, body = client.prepare_token_request(token_url = 'https://github.com/login/oauth/access_token', code = code )
        token_response = requests.post(token_url, headers=headers, data=body, auth= (github_client_id ,github_secret_id ),)
        client.parse_request_body_response(token_response.text)['access_token']
        
        uri, headers, body = client.add_token('https://api.github.com/user')
        userinfo_response = requests.get(uri, headers=headers, data=body)
        username = userinfo_response.json()['login']
        user = MongoDb.get_user(username)
        if user is None:
            user = MongoDb.add_user(username,User.readerRole)

        # Begin user session
        session['username'] = username
        #user = MongoDb.get_user(username)
        login_user(user)

        return redirect("/")

    def user_write_access(func):
        def wrap(*args, **kwargs):
            if current_user.is_readonly or app.config.get('LOGIN_DISABLED'):
                abort(403,"User does not have write permissions")
            else:
                return func(*args, **kwargs)
        wrap.__name__ = func.__name__   # Fixed off internet still do not get this ask tutors     
        return wrap 

    @app.route("/", methods=['GET', 'POST'])
    @login_required
    def index():
        item_view_model = ViewModel(MongoDb.get_all_items())  
        return render_template('index.html', view_model=item_view_model)

    @app.route("/complete_item/<string:id>")
    @login_required
    @user_write_access
    def complete_item(id):
        MongoDb.markid_item_done(id)
        return redirect('/')

    @app.route("/doing_item/<string:id>")
    @login_required
    @user_write_access
    def doing_item(id):
        MongoDb.markid_item_doing(id)
        return redirect('/')

    @app.route("/uncomplete_item/<string:id>")
    @login_required
    @user_write_access
    def uncomplete_item(id):
        MongoDb.markid_item_undone(id)
        return redirect('/')

    @app.route("/add_todo_item", methods=['GET', 'POST'])
    @login_required
    @user_write_access
    def add_todo_item():
        new_todo_item = request.form.get('new_todo_item')
        if isvalid(new_todo_item):
            MongoDb.add_item(new_todo_item)
        return redirect('/')

    def isvalid(new_todo_item):
        return len(new_todo_item) != 0

    return app

if __name__ == '__main__':
    app = create_app().run(host='0.0.0.0', debug=True)
