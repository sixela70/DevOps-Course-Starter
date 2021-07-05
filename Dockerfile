FROM python:3 as base

#Docker always runs a root 
# SO by default /root/.poetry/bin 
# From get-poetry.py
# HOME = expanduser("~")
# POETRY_HOME = os.environ.get("POETRY_HOME") or os.path.join(HOME, ".poetry")
# POETRY_BIN = os.path.join(POETRY_HOME, "bin")
# POETRY_ENV = os.path.join(POETRY_HOME, "env")
# POETRY_LIB = os.path.join(POETRY_HOME, "lib")
# POETRY_LIB_BACKUP = os.path.join(POETRY_HOME, "lib-backup")

ENV POETRY_HOME=/usr/poetry 
ENV PATH=$PATH:$POETRY_HOME/bin

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python 

WORKDIR /my-work-dir

# DEVELOPMENT #############################################
FROM base as development

COPY pyproject.toml poetry.toml poetry.lock ./

RUN poetry install 

EXPOSE 5000

# Setup run command : docker run -dp 5000:5000 todo-app:dev
CMD [ "poetry", "run", "flask", "run", "--host=0.0.0.0"]

# PRODUCTION  docker run -dp 8000:8000 todo-app:prod ######
FROM base AS production

COPY pyproject.toml poetry.toml poetry.lock ./

RUN poetry install --no-dev

COPY todo_app ./todo_app

EXPOSE 8000

CMD [ "poetry" , "run" , "gunicorn","--bind", "0.0.0.0:8000", "todo_app.app:create_app()" ]

