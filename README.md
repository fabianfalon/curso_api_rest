# Paso 2: Creamos nuestra aplicación de Django "publicaciones"

La aplicacion publicaciones tendrá 3 modelos, Category, Publication y PublicationPicture.

    ├── ...
    ├── publications
    │   ├── migrations          # migraciones
    │   ├── models              # models
    |   |   ├── __init.py
    |   |   ├── categories.py
    |   |   ├── publications.py
    │   ├── tests               # tests
    │   ├── views               # views
    │   ├── admin.py
    │   ├── apps.py
    │   ├── serializers.py
    │   ├── urls.py
    │   ├── __init__.py


### Correr migraciones
    $ docker-compose -f local.yml run --rm django python manage.py makemigrations
    $ docker-compose -f local.yml run --rm django python manage.py migrate