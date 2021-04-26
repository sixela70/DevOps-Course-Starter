# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). 
## In the .env file you will need to put in your trello keys, if you do not already have a trello account go to trello.com and register
## In order for the application to work you should setup a My TODO board with three cards called Doing, DoneList and ToDoList
## These are currently hardcoded in trello_base.py for this demo.
## 
DEVELOPER_API_KEY="<your key>"
MY_SECRET="<your secret>"
SERVER_TOKEN="<your token>"

## Running the App

Once the all dependencies have been installed, start t he Flask app in development mode within the poetry environment by running:

```bash
$ poetry run flask run
```
or 
<Your DevOps-Course-Starter Directory>>poetry run flask run


You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```

C:\devops\DevOps-Course-Starter>poetry run flask run
 * Serving Flask app "todo_app/app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 234-412-872
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

End to End Tests

To run the end to end tests you will need 

1. To ensure the GeckoDrive.exe is downloaded and placed in the root of your project 
2. To Install the Firefox Browers as this is the driver that the code is referencing 



