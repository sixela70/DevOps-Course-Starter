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

COPY todo_app ./my-work_dir
COPY pyproject.toml poetry.lock .env ./

RUN poetry install 


# DEVELOPMENT
FROM base as development

# Setup run command 
CMD [ "poetry", "run", "flask", "run", "--host=0.0.0.0"]

