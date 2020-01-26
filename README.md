# Paso 3: Primera aproximación a la vista de publicaciones

Crearemos una vista para listar todas las publiciones, para esto tenemos que instalar django rest framework, en nuestro archivo de requirementes ya lo habiamos incluido, tambien lo agregamos en la parte de THIRD_PARTY_APPS

```
THIRD_PARTY_APPS = [
    'rest_framework',
]
```

Creamos la vista para mostrar nuestras publicaciones

```
from rest_framework.decorators import api_view
from rest_framework.response import Response

from curso_api_rest.publications.models import Publication


@api_view(["GET"]) # decorador
def list_publications(request):
    """List publications"""
    publications = Publication.objects.all()
    data = []
    for publication in publications:
        data.append({
            "title": publication.title,
            "description": publication.description,
            "type_of_publication": publication.type_of_publication,
            "price": publication.price,
            "is_active": publication.is_active
        })
    return Response(data)
```

en nuestra funcion list_publications agregamos el decorador @api_view, le decimos que por ahora solo permitira recibir peticiones del tipo GET, al agregar este decorador, response ya no es el response de django sino el que provee DRF y este se encarga de hacer el parseo de la data.

En el archivo de urls de la aplicacion publications, agregamos la url para listar las publicaciones

```
# Django
from django.urls import path

# Views
from curso_api_rest.publications.views.publications import list_publications

urlpatterns = [
    path("publications/", list_publications)
]
```
Con esto ya tendriamos nuestra primer vista usando DRF.
