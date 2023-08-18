FROM python:3

# Make a app folder and move current proyect
RUN mkdir /app
COPY . /app
COPY pyproject.toml /app 

# Make folder working directory
WORKDIR /app

# Intall poetry on image
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 8000

#TODO: FALTA TERMINAR

# 1) correr migrations
# 2) correr poetry uvicorn...





