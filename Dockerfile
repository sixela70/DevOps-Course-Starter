FROM python:3.8.12-slim-buster as base

RUN apt-get update 

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

FROM base as build-dependencies

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for installing poetry
        curl \
        # deps for building python deps
        build-essential


RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python 

WORKDIR /workdir

COPY pyproject.toml poetry.toml poetry.lock ./

#RUN poetry config virtualenvs.create false \
#  && poetry install --no-dev  --no-interaction --no-ansi



# #############################################################
# PRODUCTION  docker run -dp 8000:8000 todo-app:prod ######
FROM build-dependencies AS production

COPY todo_app ./todo_app 

RUN poetry install

EXPOSE $PORT

CMD [ "sh", "-c", "poetry run gunicorn -w 4 -b 0.0.0.0:$PORT 'todo_app.app:create_app()'" ]


# #############################################################
# DEVELOPMENT docker run --env-file <env_file> -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/my-work-dir/todo_app todo-app:dev
FROM build-dependencies as development

COPY todo_app ./todo_app 

RUN poetry install

EXPOSE 5000

# Setup run command : docker run -dp 5000:5000 todo-app:dev
CMD [ "poetry", "run", "flask", "run", "--host=0.0.0.0"]


# #############################################################
# TEST
FROM build-dependencies as test

COPY todo_app ./todo_app 

RUN apt-get update -qqy && apt-get install -qqy wget gnupg unzip
# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install google-chrome-stable \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Install Chrome WebDriver
RUN CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E "s/.* ([0-9]+)(\.[0-9]+){3}.*/\1/") \
  && CHROME_DRIVER_VERSION=$(wget --no-verbose -O - "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR_VERSION}") \
  && echo "Using chromedriver version: "$CHROME_DRIVER_VERSION \
  && wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
  && unzip /tmp/chromedriver_linux64.zip -d /usr/bin \
  && rm /tmp/chromedriver_linux64.zip \
  && chmod 755 /usr/bin/chromedriver

RUN poetry install

ENTRYPOINT ["poetry", "run", "pytest"]




