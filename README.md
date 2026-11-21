# docker-practice

A tiny Django app used to practice Docker.

## What it does

Shows one web page with the Python version and the hostname of the machine it runs on.
Inside a container, the hostname is the container ID.

## Project structure

- `manage.py` - Django command-line entry point
- `requirements.txt` - Python dependencies
- `docker_demo/` - the Django project (settings, urls, views)

## How to run

## Run with Docker

Build the image:

```bash
docker build -t docker-practice .
```

Run the container:

```bash
docker run -d -p 8000:8000 --name web docker-practice
```

Open `http://localhost:8000` in the browser. The page shows the Python version and the container ID.

Stop and remove the container:

```bash
docker stop web
docker rm web
```