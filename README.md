## Description
PoC Training DJango Mongodb Backend Topics Resources

## Create project

```sh
django-admin startproject poc_training_docker_django_backend
```

## Install some dependencies

Mongo dependency
```sh
pip install djangorestframework
pip install djongo
pip install django-cors-headers
```

Check the server on port 8001
```sh
python3 manage.py runserver 8001
```

Create Api DJango Application inside project
```sh
python3 manage.py startapp ApiApplication
```

Migrate Data Model
```sh
python3 manage.py makemigrations ApiApplication
```

Apply migrations 
```sh
python3 manage.py migrate ApiApplication
```

Start django service
```sh
python3 manage.py runserver 8081
```

## Build docker image
```sh
docker build -t poc-training-docker-django-backend .
```

## run image
```sh
docker run -d --name poc-training-docker-django-backend -p 8081:8081 poc-training-docker-django-backend
```