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

Testing 

1. The application NEEDS a trello board called ToDo case sensitive 
2. To run the unit tests >> poetry run pytest todo_app/tests

End to End Tests

To run the end to end tests you will need 

1. To ensure the GeckoDrive.exe is downloaded and placed in the root of your project 
2. To Install the Firefox Browers as this is the driver that the code is referencing 
3. The e2e tests create a new board called E2E test Board, which will be destroyed at the end of the test. 
4. To run the e2e tests >> poetry run pytest todo_app/tests_e2e


To build the docker images run the below 
docker build --target development --tag todo-app:dev .
docker build --target production --tag todo-app:prod .

To run the docker images 

docker run --env-file <env_file> -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/my-work-dir/todo_app todo-app:dev
{ 
    Note to self ${pwd} did not work for me I got 
    docker: Error response from daemon: invalid mount config for type "bind": invalid mount path: '$(pwd)/todo_app' mount path must be absolute.
    Added docker_run_dev_mount.bat
}

docker run --env-file <env_file> -dp 8000:8000 todo-app:prod

The env_file should conform to the .env.template in the project WITHOUT QUOTES
Example : command_line_env.env


=======
Running within Vagrant VM

This project runs Vagrant on Hyper-V please follow these instructions for setup https://techcommunity.microsoft.com/t5/virtualization/vagrant-and-hyper-v-tips-and-tricks/ba-p/382373

Within the root directory of the project open a powershell window as Administrator and execute the following commands;

vagrant up

You will see the below, you see in the below the allocated IP address you can access the application using this IP address (172.20.214.27:5000) 
During startup you will be prompte for your windows username and password so that vagrant can mount the share. 

C:\DevOps-Course-Starter [exercise-4 ↑1 +0 ~1 -0 !]> vagrant up
Bringing machine 'default' up with 'hyperv' provider...
==> default: Verifying Hyper-V is enabled...
==> default: Verifying Hyper-V is accessible...
    default: Configuring the VM...
    default: Setting VM Enhanced session transport type to disabled/default (VMBus)

Vagrant requires administrator access for pruning SMB shares and
may request access to complete removal of stale shares.
==> default: Starting the machine...
==> default: Waiting for the machine to report its IP address...
    default: Timeout: 120 seconds
    default: IP: 172.20.214.27
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 172.20.214.27:22
    default: SSH username: vagrant
    default: SSH auth method: private key
==> default: Machine booted and ready!
==> default: Preparing SMB shared folders...
    default: You will be asked for the username and password to use for the SMB
    default: folders shortly. Please use the proper username/password of your
    default: account.
    default:
    default: Username (user[@domain]): alexis
    default: Password (will be hidden):

Vagrant requires administrator access to create SMB shares and
may request access to complete setup of configured shares.
==> default: Mounting SMB shared folders...
    default: C:/Google Drive/DevOps/DevOps-Course-Starter => /vagrant
==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
==> default: flag to force provisioning. Provisioners marked to run always will still run.
==> default: Running action triggers after up ...
==> default: Running trigger: Launching App...
==> default: Running the TODO app setup script
    default: Running: C:/Users/alexi/AppData/Local/Temp/vagrant-shell20210520-2100-1x5is6x.sh
    default: Installing dependencies from lock file
    default: No dependencies to install or update
    default: Installing the current project: todo-app (0.1.0)
C:\DevOps-Course-Starter [exercise-4 ↑1 +0 ~1 -0 !]>


