# movierama
A movie social sharing platform that utilizes


- Django 2.2 ( Python 3.7)
- Twitter Bootstrap 4
- Docker
- Redis
- PostgreSQL

[Cookiecutter Django](https://github.com/pydanny/cookiecutter-django) has been used for the initial setup

## Requirements
- [Docker](https://docs.docker.com/install/#supported-platforms)
- [Docker Compose](https://docs.docker.com/compose/install/)



## Local setup

Build the stack:
```
$ docker-compose -f local.yml build
```
Run the stack:
```
docker-compose -f local.yml up
```
Django's runserver will be available in http://127.0.0.1:8000/

[Browsersync](https://www.browsersync.io/) is available in http://127.0.0.1:3000/
  (UI version is on http://127.0.0.1:3001)
  
Import initial data:
```
docker-compose -f local.yml run --rm django python manage.py loaddata users.json
docker-compose -f local.yml run --rm django python manage.py loaddata movies.json
```

```
Note: Credentials for the example users following the below format: 
username: firstnamelastname
password: 123asd456
```
e.g Jon Snow is jonsnow with 123asd456 as password 
  


## Testing
In order to run the BDD tests you need to do the following:

Run the stack:
```
docker-compose -f local.yml up
```
Execute django-behave command: 
```
docker-compose -f local.yml run --rm django python manage.py behave
```


## Todo

- Add caching
- Add more BDD scenarios
- Test the production config with [AWS Elasticbeanstalk](https://aws.amazon.com/elasticbeanstalk/)
- Handle the case where a user tries to add a Movie that exists already (Need more data on that. Release date etc)
- Add pagination on the list of pages
- Change form submissions (ordering, like/hate etc) to be asynchronous
- Use an external Movie database to fetch information for added movies (cover, cast, rating etc)

