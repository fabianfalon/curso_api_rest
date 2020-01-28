# Paso 4: Serializers

Según la [documentacion de DRF](https://www.django-rest-framework.org/api-guide/serializers/) los serializers son contenedores que nos permiten tomar tipos de datos complejos y convertirlos a tipos de datos nativos de python para luego usarlo como JSON, XML u otro tipo de datos.
Los serializadores también proporcionan deserialización, permitiendo que los datos analizados se conviertan nuevamente en tipos complejos, después de validar primero los datos entrantes.

Los serializadores en DRF funciona muy similar a los forms de django

Ahora creamos nuestro serializers para publicaciones, para ello agregamos una carpeta serializers la cual contendra dos archivos, uno para categorias y otro para publicaciones

Nuestro serializador de publicaciones quedaria como se muestra en el ejemplo siguiente

En la documentacion de drf podemos ver los [tipos de datos](https://www.django-rest-framework.org/api-guide/fields/#booleanfield) disponibles para usar en los serializadores.

```
from rest_framework import serializers

class PublicationSerializer(serializers.Serializer):
    """PublicationSerializer"""
    title = serializers.CharField()
    description = serializers.CharField()
    type_of_publication = serializers.CharField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    is_active = serializers.BooleanField()
```

Tambien crearemos el serializador para categorias, el cual utilizaremos luego.

```
from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    """CategorySerializer"""
    id = serializers.IntegerField()
    name = serializers.CharField()
```

Nuestra vista de publicaciones cambiara un poco, ahora importaremos el serializer de publicaciones
y lo usaremos para serializar la informacion dentro del for.

```
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from curso_api_rest.publications.models import Publication

# Serializers
from curso_api_rest.publications.serializers import PublicationSerializer


@api_view(["GET"])
def list_publications(request):
    """List publications"""
    publications = Publication.objects.all()
    data = []
    for publication in publications:
        serializer = PublicationSerializer(publication)
        data.append(serializer.data)
    return Response(data)
```

Hasta ahora las publicaciones no estabamos mostrando toda su información, faltaban datos como categorias y profile, para agregar la informacion de categorias solamente necesitamos hacer uso de CategorySerializer en PublicationSerializer. De esta forma podremos ver la informacion de la categoria a la que pertenece la publicación

```
from rest_framework import serializers

from curso_api_rest.publications.serializers.categories import CategorySerializer

class PublicationSerializer(serializers.Serializer):
    """PublicationSerializer"""
    title = serializers.CharField()
    description = serializers.CharField()
    type_of_publication = serializers.CharField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    is_active = serializers.BooleanField()
    category = CategorySerializer()
```

Podemos ver que con el uso de serializer nos ahorramos varias lineas de codigo en nuestra view, pero podemos simplificar la vista aun mas de la siguiente forma.

```
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from curso_api_rest.publications.models import Publication

# Serializers
from curso_api_rest.publications.serializers import PublicationSerializer


@api_view(["GET"])
def list_publications(request):
    """List publications"""
    publications = Publication.objects.all()
    serializer = PublicationSerializer(publications, many=True) 
    return Response(serializer.data)
```